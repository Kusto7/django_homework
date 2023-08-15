from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
import uuid
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.views.generic import CreateView, UpdateView, FormView

from users.forms import UserRegisterForm, UserProfileForm, UserRecoveryPasswordForm
from users.models import User


# class RegisterView(CreateView):
#     model = User
#     form_class = UserRegisterForm
#     template_name = 'users/register.html'
#     success_url = reverse_lazy('users:login')

class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'

    # success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save()
            self.object.is_active = False
            self.object.register_uuid = uuid.uuid4().hex
            self.object.save()
            current_site = get_current_site(self.request)
            send_mail(
                subject='Подтверждение аккаунта',
                message=f'Для подтверждения перейдите по ссылке http://{current_site}{reverse_lazy("users:success_register", kwargs={"register_uuid": self.object.register_uuid})}',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[self.object.email]
            )
            return super().form_valid(form)

    def get_success_url(self):
        messages.add_message(self.request, messages.INFO,
                             f'Пользователь создан. Необходимо подтвердить аккаунт. '
                             f'Письмо отправлено на Email: {self.object.email}')
        return reverse_lazy('users:login')


def verification_user(request, *args, **kwargs):
    user = User.objects.get(register_uuid=kwargs['register_uuid'])
    if user.register_uuid == kwargs['register_uuid']:
        user.is_active = True
        user.save()
        messages.add_message(request, messages.INFO, f'Учетная запись {user.email} активирована')
    return redirect(reverse('users:login'))


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


class RecoveryPasswordView(FormView):
    model = User
    template_name = 'users/recovery_password.html'
    form_class = UserRecoveryPasswordForm

    def form_valid(self, form, *args, **kwargs):
        recovery_user = User.objects.get(email=form.cleaned_data['email_recovery'])
        self.object = form
        if recovery_user and form.is_valid():
            password = User.objects.make_random_password()
            recovery_user.set_password(password)
            recovery_user.save()
            send_mail(
                subject='Новый пароль',
                message=f'Ваш новый пароль: {password}',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[recovery_user.email]
            )

            return super().form_valid(form, *args, **kwargs)
        form.add_error('email_recovery', 'Почтовый ящик не существует')
        return super().form_invalid(form)

    def get_success_url(self):
        messages.add_message(self.request, messages.INFO,
                             f'Новый пароль отправлен на Email: {self.object.cleaned_data["email_recovery"]}')
        return reverse_lazy('users:login')

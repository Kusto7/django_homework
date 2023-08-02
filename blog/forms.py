from django import forms
from django.views.generic import CreateView, UpdateView
from pytils.translit import slugify

from blog.models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'body', 'preview',)

    def clean_title(self):
        cleaned_data = self.cleaned_data['title']
        danger_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        if cleaned_data in danger_words:
            raise forms.ValidationError('Название некорректное, придумайте другое.')

        return cleaned_data


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'body', 'preview',)

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'body', 'preview',)

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)

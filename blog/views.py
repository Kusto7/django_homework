from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView


from blog.forms import BlogForm
from blog.models import Blog


class BlogCreateView(CreateView):
    model = Blog
    form_class = BlogForm

    def get_success_url(self):
        return reverse('blog:detail', args=[self.kwargs.get('pk')])


class BlogUpdateView(UpdateView):
    model = Blog
    form_class = BlogForm

    def get_success_url(self):
        return reverse('blog:detail', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:list')


class BlogListView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


def toggle_published(request, pk):
    blog_item = get_object_or_404(Blog, pk=pk)
    if blog_item.is_published:
        blog_item.is_published = False
    else:
        blog_item.is_published = True

    blog_item.save()

    return redirect(reverse('blog:list'))

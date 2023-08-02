from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogListView, BlogCreateView, BlogDetailView, BlogUpdateView, BlogDeleteView, toggle_published

app_name = BlogConfig.name

urlpatterns = [
    path('', BlogListView.as_view(), name='list'),
    path('list/<int:pk>/', BlogListView.as_view(), name='list'),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('detail/<int:pk>/', BlogDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', BlogUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete'),
    path('published/<int:pk>/', toggle_published, name='published'),
]

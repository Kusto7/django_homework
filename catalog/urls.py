from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contacts, ProductListView, ProductDeleteView, ProductCreateView, ProductUpdateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    path('list', ProductListView.as_view(), name='list'),
    path('contacts/', contacts, name='contacts'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete'),
]

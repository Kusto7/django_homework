from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import contacts, ProductListView, ProductDeleteView, ProductCreateView, ProductUpdateView, \
    ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    path('list', ProductListView.as_view(), name='list'),
    path('contacts/', contacts, name='contacts'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete'),
    path('view/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='view'),
]

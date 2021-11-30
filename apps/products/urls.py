from apps.products.views import *
from django.urls import path
from django.utils.regex_helper import normalize


urlpatterns = [
    path('', ProductIndexView.as_view(), name='index_product'),
    path('detail/<str:slug>/', ProductDetailView.as_view(), name='detail_product'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update_product'), 
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
    path('image_create/', PhotoProductCreateView.as_view(), name='image_create')
]


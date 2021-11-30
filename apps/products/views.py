from django import forms
from django.db import models
from django.http import request
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse_lazy
from apps.products.models import ProductImage,Product
from apps.products.forms import ProductForm, ProductImageForm
from django.views import generic
from django.shortcuts import get_object_or_404, render, redirect
from apps.users.models import User


class ProductIndexView(generic.ListView):
    queryset = Product.objects.all()
    model = Product
    template_name = 'products/index.html'
    context_object_name = 'products'

class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'products/detail.html'
    
   
    context_object_name = 'products'

  

    


class ProductCreateView(generic.CreateView):
    form_class = ProductForm
    
    success_url = reverse_lazy('index_product')
    template_name = 'products/create.html'
    
    

    # def get_initial(self):
    #     product = get_object_or_404(Product, pk=self.kwargs['pk'])
    #     self.initial.update({
    #         'user': self.request.user.id,
    #         'price': product.price,
    #         'description': product.pk,
    #         'quantity': product.quantity,
    #         'title': product.quantity,
    #         'product': product.pk
    #     })
    #     return super(ProductCreateView,self).get_initial()

class ProductDeleteView(generic.DeleteView):
    model = Product
    success_url = reverse_lazy('index_product')
    template_name = 'products/delete.html'


class ProductUpdateView(generic.UpdateView):

    form_class = ProductForm
    queryset = Product.objects.all()
    
    success_url = reverse_lazy('index_product')
    template_name = 'products/update.html'

class PhotoProductCreateView(generic.CreateView):
    
    form_class = ProductImageForm
    success_url = reverse_lazy('index_product')
    template_name = 'products/createimage.html'

from django.db import models
from django.forms import fields, widgets
from apps.products.models import Product,ProductImage
from django import forms
from apps.users.models import User
from django.contrib import admin
class ProductForm(forms.ModelForm):


    # def __init__(self, *args, **kwargs):
    #     super(ProductForm, self).__init__(*args, **kwargs)
    #     self.fields['user'].required = False
    #     self.fields['user'].widgets.attrs['disabled'] = 'disabled'

    # def clean_user(self):
    #     instance = getattr(self, 'instane', None)
    #     if instance:
    #         return instance.user
    #     else:
    #         return self.cleaned_data.get('user', None)

    class Meta:
        model = Product
        exclude = ['is_stock', 'slug']
        
        # widgets = {
        #     'title':forms.TextInput(attrs={'class':'form-control'}),
        #     'description':forms.Textarea(attrs={'class':'form-control'}),
        #     'price':forms.NumberInput(attrs={'class':'form-control'}),
            
        #     'quantity':forms.NumberInput(attrs={'class':'form-control'}),
            
        # }

class ProductImageForm(forms.ModelForm):

    class Meta:
        model=ProductImage
        fields = ['image',]
        widgets = {
            'image':forms.ClearableFileInput(attrs={'class':'form-control'}),
        }

# class UserChoiceField(forms.ModelChoiceField):
#     pass



# class Form_user(forms.ModelForm):
#     def formfield_for_foreignkey(self, db_field, request, **kwargs):
#         if db_field.name == 'product_user':
#             return UserChoiceField(User.objects.filter(slug = 'Isa_kov17'))
#         return super().formfield_for_foreignkey(db_field, request, **kwargs)
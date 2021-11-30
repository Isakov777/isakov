from django import forms
from apps.users.models import User
from django.contrib import admin
from apps.products.models import Product,ProductImage

admin.site.register(Product)
admin.site.register(ProductImage)

# class AdminChoiceField(forms.ModelChoiceField):
#     pass

# class Admin(admin.ModelAdmin):
    
#     def formfield_for_foreignkey(self, db_field, request, **kwargs):
#         if db_field.name == 'product_user':
#             return AdminChoiceField(User.objects.filter(slug = 'Isa_kov17'))
#         return super().formfield_for_foreignkey(db_field, request, **kwargs)


    # def formfield_for_foreignkey(self, db_field: ForeignKey, request: Optional[HttpRequest], **kwargs: Any) -> Optional[ModelChoiceField]:
    #     return super().formfield_for_foreignkey(db_field, request, **kwargs)
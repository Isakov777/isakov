
from django.db import models

from utils.slug_generator import unique_slug_generators
from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save

User = get_user_model()


class Product(models.Model):
    title = models.CharField(max_length=255, db_index=True, verbose_name='Название')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_user')
    price = models.PositiveIntegerField(verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    is_stock = models.BooleanField(default=True, db_index=True)
    slug = models.SlugField(blank=True, unique=True)
    
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['-id']



class ProductImage(models.Model):
    image = models.ImageField(upload_to = 'product',verbose_name = 'Картинка',blank = True,null = True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_image')
    def str(self):
        return self.product.title
    

def slug_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generators(instance)

pre_save.connect(slug_pre_save_receiver, sender=Product)
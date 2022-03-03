from django.db import models
from category.models import Category
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields

# Create your models here.
from django.urls import reverse


class Product(TranslatableModel):
    translations = TranslatedFields(
        product_name=models.CharField(max_length=200, unique=True, verbose_name=_('Product Name')),
        description=models.TextField(max_length=1500, blank=True, verbose_name=_('Description')),
    )
    slug = models.SlugField(max_length=200, unique=True, verbose_name=_('Slug'))
    price = models.IntegerField(verbose_name=_('Price'))
    image = models.ImageField(upload_to='photos/products', verbose_name=_('Images'))
    is_available = models.BooleanField(default=True, verbose_name=_('Is Available'))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_('Category'))
    created_date = models.DateTimeField(auto_now_add=True, verbose_name=_('Created Date'))
    modified_date = models.DateTimeField(auto_now=True, verbose_name=_('Modified Date'))

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
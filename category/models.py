from django.db import models
from django.utils.text import slugify
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields
from .managers import CategoryManager
from django.urls import reverse


class Category(MPTTModel, TranslatableModel):
    parent = TreeForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="children", verbose_name=_('Parent'))

    translations = TranslatedFields(
        name=models.CharField(max_length=255, verbose_name=_('Name'), null=True, blank=True),
    )
    slug = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('Slug'))

    objects = CategoryManager()

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    class MPTTMeta:
        order_insertion_by = ['id']

    def __str__(self):
        return self.name


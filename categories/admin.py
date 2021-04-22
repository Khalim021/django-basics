from django.contrib import admin

# Register your models here.
from categories.models import CategoryModel


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['genre']
    search_filter = ['genre']

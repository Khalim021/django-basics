from django.contrib import admin

# Register your models here.
from authors.models import AuthorModel


@admin.register(AuthorModel)
class AuthorModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'age']
    list_filter = ['name']

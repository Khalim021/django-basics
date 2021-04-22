from django.contrib import admin
from books.models import BookModel
# Register your models here.


@admin.register(BookModel)
class BookModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'page_count', 'author', 'category']
    search_fields = ['title', 'page_count', 'author', 'category']



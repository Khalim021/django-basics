from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.
from authors.models import AuthorModel
from categories.models import CategoryModel


class BookModel(models.Model):
    title = models.CharField(max_length=50, null=False)
    page_count = models.IntegerField(null=True, blank=True)
    published_year = models.IntegerField(default=False, null=False, blank=False)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    author = models.ForeignKey(AuthorModel, on_delete=models.PROTECT,
                               related_name='books')

    category = models.ForeignKey(CategoryModel, on_delete=models.PROTECT,
                                 related_name='books', null=True)
    description = RichTextUploadingField(null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'book'
        verbose_name_plural = 'books'










from django.db import models


# Create your models here.


class CategoryModel(models.Model):
    genre = models.CharField(max_length=35, null=True)

    def __str__(self):
        return self.genre

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

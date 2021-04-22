from django.db import models

# Create your models here.


class AuthorModel(models.Model):
    name = models.CharField(max_length=50, null=False)
    age = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'author'
        verbose_name_plural = 'authors'

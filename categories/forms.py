from django import forms

from categories.models import CategoryModel


class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = CategoryModel
        fields = ['genre']

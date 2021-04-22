
from django import forms
from books.models import BookModel


class ContactForm(forms.Form):
    name = forms.CharField(max_length=50)
    phone = forms.CharField(max_length=25, required=False)
    comments = forms.CharField(widget=forms.Textarea)


class BookModelForm(forms.ModelForm):
    class Meta:
        model = BookModel
        fields = ['title', 'page_count', 'author', 'category']
















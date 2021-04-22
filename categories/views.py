from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.views.generic import ListView, UpdateView, CreateView

from books.models import BookModel
from categories.forms import CategoryModelForm
from categories.models import CategoryModel


class CategoryCreateView(CreateView):
    template_name = 'form.html'
    form_class = CategoryModelForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create category'
        return context


class CategoryUpdateView(UpdateView):
    model = CategoryModel
    form_class = CategoryModelForm
    success_url = '/'
    template_name = 'form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update category'
        return context


class CategoriesListView(ListView):
    template_name = 'categories_list.html'
    model = CategoryModel


def category_delete(request, pk):
    get_object_or_404(BookModel, pk=pk).delete()
    return redirect('/')



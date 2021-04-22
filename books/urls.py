from django.urls import path
from books.views import BookCreateView, BookListView, BookUpdateView, delete_book
from categories.views import CategoriesListView, CategoryCreateView, CategoryUpdateView, category_delete

urlpatterns = [
    path('categories/', CategoriesListView.as_view()),
    path('categories/create/', CategoryCreateView.as_view()),
    path('categories/update/<int:pk>/', CategoryUpdateView.as_view()),
    path('categories/delete/<int:pk>/', category_delete),
    path('create/', BookCreateView.as_view()),
    path('update/<int:pk>/', BookUpdateView.as_view()),
    path('delete/<int:pk>/', delete_book),
    path('', BookListView.as_view()),


]





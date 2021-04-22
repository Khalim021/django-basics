
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import CreateView, ListView, UpdateView

from books.models import BookModel
from django.db.models import Q
from books.forms import BookModelForm


# Create your views here.


class BookListView(ListView):
    template_name = 'books_lists.html'

    def get_queryset(self):
        q = self.request.GET.get('q', '')
        books = BookModel.objects.filter(Q(title__icontains=q) |
                                         Q(author__name__icontains=q) |
                                         Q(category__genre__icontains=q))
        return books


# def books_list(request):
#     q = request.GET.get('q', '')
#     # books = BookModel.objects.all()
#     books = BookModel.objects.filter(Q(title__contains=q) |
#                                      Q(author__name__contains=q) |
#                                      Q(category__genre__contains=q))
#
#     context = {
#         'books': books
#     }
#     return render(request, 'books_lists.html', context)
#

class BookCreateView(CreateView):
    template_name = 'form.html'
    form_class = BookModelForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create Book'
        return context


class BookUpdateView(UpdateView):
    model = BookModel
    form_class = BookModelForm
    success_url = '/'
    template_name = 'form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update book'
        return context
# def update_book(request, pk):
#     if request.method == 'POST':
#         book = get_object_or_404(BookModel, pk=pk)
#         form = BookModelForm(instance=book, data=request.POST)
#
#         if form.is_valid():
#             form.save()
#         return redirect('/')
#
#     book = get_object_or_404(BookModel, pk=pk)
#     form = BookModelForm(instance=book)
#
#     context = {
#         'title': 'Update Book',
#         'form': form
#     }
#     return render(request, 'form.html', context)

# def create_book(request):
#     if request.method == 'POST':
#         title = request.POST.get('title')
#         page_count = request.POST.get('page_count', 0)
#
#         author = AuthorModel.objects.get(pk=request.POST.get('author'))
#         category = CategoryModel.objects.get(pk=request.POST.get('category'))
#
#         BookModel.objects.create(
#             title=title,
#             page_count=page_count,
#             author=author,
#             category=category
#         )
#
#         form = BookModelForm(request.POST)
#
#         if form.is_valid():
#             form.save()
#
#         return redirect('/')
#
#     else:
#
#         form = BookModelForm(request.POST)
#         context = {
#             'form': form
#         }
#
#         return render(request, 'create_book.html', context)


def delete_book(request, pk):
    get_object_or_404(BookModel, pk=pk).delete()
    return redirect('/')




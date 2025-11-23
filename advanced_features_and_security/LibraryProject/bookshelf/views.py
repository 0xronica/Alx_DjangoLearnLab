from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to my book store.")

# content_app/views.py
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Article

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    return HttpResponse("List of articles.")
    

@permission_required('bookshelf.can_create', raise_exception=True)
def article_create(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return HttpResponse("Article created successfully.")


@permission_required('bookshelf.can_edit', raise_exception=True)
def article_edit(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return HttpResponse("Article edited successfully.")

    

@permission_required('bookshelf.can_delete', raise_exception=True)
def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return HttpResponse("Article deleted successfully.")

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse
from .models import Book
from .forms import ExampleForm

# Secure list view
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()  # ORM safely handles queries
    return render(request, 'bookshelf/book_list.html', {'books': books})

# Secure create view
@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():  # Validation prevents malicious input
            form.save()
            return HttpResponse("Book created successfully.")
    else:
        form = ExampleForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})

# Secure detail/edit view
@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = ExampleForm(request.POST or None, instance=book)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return HttpResponse("Book updated successfully.")
    return render(request, 'bookshelf/form_example.html', {'form': form})

# Secure delete view
@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return HttpResponse("Book deleted successfully.")


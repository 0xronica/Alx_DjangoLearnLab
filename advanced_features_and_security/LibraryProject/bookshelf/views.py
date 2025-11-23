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

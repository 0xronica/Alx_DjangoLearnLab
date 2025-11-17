from django.http import HttpResponse
from django.shortcuts import render
from .models import Book, Library
from django.views.generic import DetailView


## Function-Based View: List all books

def list_books(request):
    """Retrieve all books and render a template displaying the list."""
    books = Book.objects.all()  # Fetch all book instances from the database
    context = {'list_books': books}
    return render(request, "relationship_app/list_books.html", context)


# Class-Based View: Display library details and its books
class LibraryDetailView(DetailView):
    model = Library
    template_name = "library_detail.html"
    context_object_name = "library"

# Create your views here.

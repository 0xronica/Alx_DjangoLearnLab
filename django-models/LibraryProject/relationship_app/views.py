from django.http import HttpResponse
from django.shortcuts import render
from .models import Book, Library
from django.views.generic import DetailView


## Function-Based View: List all books
def list_books(request):
      """Retrieves all books and renders a template displaying the list."""
      books = Book.objects.all()  # Fetch all book instances from the database
      context = {'list_books': books}  # Create a context dictionary with book list
      return render(request, 'books/list_books.html', context)

      output = ""
    for book in books:
        output += f"{book.title} by {book.author.name}\n"

    return HttpResponse(output, content_type="text/plain")


# Class-Based View: Display library details and its books
class LibraryDetailView(DetailView):
    model = Library
    template_name = "library_detail.html"
    context_object_name = "library"

# Create your views here.

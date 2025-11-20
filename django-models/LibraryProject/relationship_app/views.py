from django.http import HttpResponse
from django.shortcuts import render
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView



## Function-Based View: List all books

def list_books(request):
    """Retrieve all books and render a template displaying the list."""
    books = Book.objects.all()  # Fetch all book instances from the database
    context = {'list_books': books}
    return render(request, "relationship_app/list_books.html", context)


# Class-Based View: Display library details and its books
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"


from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

# Register user view
class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'relationship_app/register.html'
    success_url = reverse_lazy('login')


# Create your views here.

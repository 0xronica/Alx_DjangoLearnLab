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

from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

# Register user view
class RegisterView(CreateView):
    form_class = UserCreationForm()
    template_name = 'relationship_app/register.html'
    success_url = reverse_lazy('login')

def Logoutview(request):
    logout(request)
    return render(request, "relationship_app/logout.html")


from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

# Helper functions for access control
def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'


# ADMIN VIEW
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')


# LIBRARIAN VIEW
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')


# MEMBER VIEW
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

# Create your views here.

from django.shortcuts import render


from rest_framework import generics, permissions
from django_filters import rest_framework
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

class ListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# Book Detail View
# Retrieves a single book by its primary key (ID).
# This endpoint is publicly accessible (read-only for unauthenticated users)
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # Enable filtering by specific fields
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author__name', 'publication_year']  # Filter by title, author name, year
    search_fields = ['title', 'author__name']  # Allow text search on title and author name
    ordering_fields = ['title', 'publication_year']  # Allow ordering by title and year
    ordering = ['title']  # Default ordering


# Book Create View
# Allows authenticated users to create a new Book entry.
# Includes validation from the serializer.
class CreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

# Book Update View
# Allows authenticated users to modify an existing Book.
# Includes custom validation and permission checks.
# ------------------------------------------------------------
class UpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

# Book Delete View
# Allows authenticated users to delete a Book entry.
# ------------------------------------------------------------
class DeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

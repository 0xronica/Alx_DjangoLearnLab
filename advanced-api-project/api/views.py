from django.shortcuts import render


from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

class ListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

# Book Detail View
# Retrieves a single book by its primary key (ID).
# This endpoint is publicly accessible (read-only for unauthenticated users)
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

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

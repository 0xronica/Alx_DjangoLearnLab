from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Author, Book

class BookAPITestCase(APITestCase):

    def setUp(self):
        """
        Setup test data:
        - Create a test user for authenticated endpoints.
        - Create an author and some books for testing.
        """
        # Create a user
        self.user = User.objects.create_user(username="testuser", password="password123")

        # Create an author
        self.author = Author.objects.create(name="Chinua Achebe")

        # Create books
        self.book1 = Book.objects.create(
            title="Things Fall Apart",
            publication_year=1958,
            author=self.author
        )
        self.book2 = Book.objects.create(
            title="No Longer at Ease",
            publication_year=1960,
            author=self.author
        )

    # -------------------------------
    # Test: List all books
    # -------------------------------
    def test_list_books(self):
        url = reverse("book-list-create")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    # -------------------------------
    # Test: Retrieve a single book
    # -------------------------------
    def test_retrieve_book(self):
        url = reverse("book-detail", args=[self.book1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Things Fall Apart")

    # -------------------------------
    # Test: Create a new book (requires authentication)
    # -------------------------------
    def test_create_book_authenticated(self):
        self.client.login(username="testuser", password="password123")
        url = reverse("book-list-create")
        data = {
            "title": "Arrow of God",
            "publication_year": 1964,
            "author": self.author.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_create_book_unauthenticated(self):
        url = reverse("book-list-create")
        data = {
            "title": "Arrow of God",
            "publication_year": 1964,
            "author": self.author.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)  # Permission denied

    # -------------------------------
    # Test: Update a book
    # -------------------------------
    def test_update_book_authenticated(self):
        self.client.login(username="testuser", password="password123")
        url = reverse("book-update", args=[self.book1.id])
        data = {"title": "Things Fall Apart (Updated)"}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Things Fall Apart (Updated)")

    # -------------------------------
    # Test: Delete a book
    # -------------------------------
    def test_delete_book_authenticated(self):
        self.client.login(username="testuser", password="password123")
        url = reverse("book-delete", args=[self.book2.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    # -------------------------------
    # Test: Filtering books by title
    # -------------------------------
    def test_filter_books_by_title(self):
        url = reverse("book-list-create") + "?title=Things Fall Apart"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Things Fall Apart")

    # -------------------------------
    # Test: Searching books by author name
    # -------------------------------
    def test_search_books_by_author(self):
        url = reverse("book-list-create") + "?search=Achebe"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    # -------------------------------
    # Test: Ordering books by publication year
    # -------------------------------
    def test_order_books_by_publication_year(self):
        url = reverse("book-list-create") + "?ordering=publication_year"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [book['publication_year'] for book in response.data]
        self.assertEqual(years, sorted(years))


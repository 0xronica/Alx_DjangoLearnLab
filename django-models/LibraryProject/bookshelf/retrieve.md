```python3
from bookshelf import Book

books = Book.objects.all()

book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)

# Expected Output:
# 1984 George Orwell 1949
```

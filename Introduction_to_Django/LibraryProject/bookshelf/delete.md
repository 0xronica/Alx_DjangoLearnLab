```python
from bookshelf import Book


book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

books = Book.objects.all()

# Expected Output:
# [] # Book successfully deleted, no books remaining

```

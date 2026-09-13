# Test Failure Output

```text
Found 1 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
F
======================================================================
FAIL: test_book_appears_on_books_page (catalog.tests.BookListViewTests.test_book_appears_on_books_page)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Noah Ellis\OneDrive\cidm3312\book-catalog\catalog\tests.py", line 18, in test_book_appears_on_books_page
    self.assertContains(response, "The Maze Runner")
    ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: False is not true : Couldn't find 'The Maze Runner' in the following response
b'<!DOCTYPE html>\n<html lang="en">\n<head>\n    <meta charset="UTF-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <title>Book Catalog</title>\n</head>\n<body>\n    <header>\n        <h1>Book Catalog</h1>\n\n        <nav>\n            <a href="/">Books</a>\n            <a href="/publishers/">Publishers</a>\n            <a href="/reviews/">Reviews</a>\n        </nav>\n    </header>\n\n    <main>\n        \n    <h2>Books</h2>\n\n    \n      <p>No books are currently in the catalog.</p>\n    \n\n    </main>\n</body>\n</html>'

----------------------------------------------------------------------
Ran 1 test in 0.018s

FAILED (failures=1)
Destroying test database for alias 'default'...
```

This failure showed me that my test correctly detects when a book in the database is missing from the Books page.

# Question 1

The `Book` model carries the `ForeignKey` that points to the `Publisher` model because one publisher can publish many books, while each book belongs to one publisher. If I reversed it, each publisher could point to only one book, so I would not be able to represent one publisher having multiple books without entering duplicate publisher records.

# Question 2

I used an `IntegerField` for the book's publication year because a year is stored as a whole number. If I used a `CharField`, Django would treat the year as text, so I would lose proper numeric validation and numeric comparisons.
from django.test import TestCase
from django.urls import reverse

from .models import Book, Publisher


class BookListViewTests(TestCase):
    def test_book_appears_on_books_page(self):
        publisher = Publisher.objects.create(name="Delacorte Press")
        Book.objects.create(
            title="The Maze Runner",
            publication_year=2009,
            publisher=publisher,
        )

        response = self.client.get(reverse("book_list"))

        self.assertContains(response, "The Maze Runner")
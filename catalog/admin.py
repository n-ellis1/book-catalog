from django.contrib import admin

from .models import Book, Publisher, Review


admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(Review)
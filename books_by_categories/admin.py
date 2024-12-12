from django.contrib import admin
from books_by_categories.models import Tag, Book

admin.site.register(Tag)
admin.site.register(Book)
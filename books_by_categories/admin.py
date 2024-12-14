from django.contrib import admin
from books_by_categories.models import Tag, Books

admin.site.register(Tag)
admin.site.register(Books)
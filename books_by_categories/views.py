from django.shortcuts import render
from . import models


def all_books(request):
    if request.method == "GET":
        books = models.Book.objects.all().order_by('-id')
        context = {'books': books}
        return render(
            request,
            template_name='tags/all_books.html',
            context=context
        )

def kids_books(request):
    if request.method == "GET":
        books_kids = models.Book.objects.filter(tags__name='Книги для детей').order_by('-id')
        context = {'books_kids': books_kids}
        return render(
            request,
            template_name='tags/kids_books.html',
            context=context
        )

def teenagers_books(request):
    if request.method == "GET":
        books_teenagers = models.Book.objects.filter(tags__name='Книги для подростков').order_by('-id')
        context = {'books_teenagers': books_teenagers}
        return render(
            request,
            template_name='tags/teenagers_books.html',
            context=context
        )

def youth_books(request):
    if request.method == "GET":
        books_youth = models.Book.objects.filter(tags__name='Книги для молодежи').order_by('-id')
        context = {'books_youth': books_youth}
        return render(
            request,
            template_name='tags/youth_books.html',
            context=context
        )

def pensioners_books(request):
    if request.method == "GET":
        books_pensioners = models.Book.objects.filter(tags__name='Книги для пенсионеров').order_by('-id')
        context = {'books_pensioners': books_pensioners}
        return render(
            request,
            template_name='tags/pensioners_books.html',
            context=context
        )
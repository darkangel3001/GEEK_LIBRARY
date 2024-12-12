from django.urls import path
from . import views

urlpatterns = [
    path('all_books/', views.all_books, name='all_books'),
    path('kids/', views.kids_books, name='kids_books'),
    path('teenagers/', views.teenagers_books, name='teenagers_books'),
    path('youth/', views.youth_books, name='youth_books'),
    path('pensioners/', views.pensioners_books, name='pensioners_books'),
]
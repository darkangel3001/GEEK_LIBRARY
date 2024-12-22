from django.urls import path
from . import views

urlpatterns = [
    path('manas_film_list/', views.ManasListView.as_view(), name='manas_list'),
    path('form_parser_manas/', views.ManasFormView.as_view()),
]
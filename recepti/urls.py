from django.urls import path
from . import views

urlpatterns = [
    path('recepti_list/', views.ReceptiListView.as_view(), name='recepti_list'),
    path('recepti_list/<int:id>/', views.ReceptiDetailView.as_view(), name='recepti_detail'),
    path('recepti_list/<int:id>/delete/', views.DeleteReceptiView.as_view(), name='delete_recepti'),
    path('create_recepti/', views.CreateReceptiView.as_view(), name='createRecepti'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.gestionBarco, name='gestion-barco'),
    path('gestion-tripulantes/', views.gestionTripulantes, name='gestion-tripulante'),
    path('barco/<str:nombreBarco>/', views.barcoDetail, name='barco-detail'),
    path('borrar-barco/<pk>/', views.BarcoDeleteView.as_view(), name='delete-barco'),

    path('borrar-tripulante/<pk>/', views.TripulanteDeleteView.as_view(), name='delete-tripulante'),
    path('actualizar-tripulante/<pk>/', views.TripulanteUpdateView.as_view(), name='update-tripulante'),

]
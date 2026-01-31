from django.urls import path, include
from . import views
from .views import SignUpView, RecenzijaDeleteView 

urlpatterns = [
    path('', views.DjeloListView.as_view(), name='djelo-list'),
    path('djelo/<int:pk>/', views.DjeloDetailView.as_view(), name='djelo-detail'),
    path('autori/', views.AutorListView.as_view(), name='autor-list'),
    path('recenzije/', views.RecenzijaListView.as_view(), name='recenzija-list'),
    path("accounts/", include("django.contrib.auth.urls")), 
    path("accounts/signup/", SignUpView.as_view(), name="register"), 
    path('recenzija/<int:pk>/obrisi/', RecenzijaDeleteView.as_view(), name='obrisi-recenziju'),
]
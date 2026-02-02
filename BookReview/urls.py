from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.DjeloListView.as_view(), name='djelo-list'),
    path('djelo/<int:pk>/', views.DjeloDetailView.as_view(), name='djelo-detail'),

    path('djelo/dodaj/', views.DjeloCreateView.as_view(), name='djelo-create'),
    path('djelo/<int:pk>/uredi/', views.DjeloUpdateView.as_view(), name='djelo-update'),
    path('djelo/<int:pk>/obrisi/', views.DjeloDeleteView.as_view(), name='djelo-delete'),

    path('djelo/<int:pk>/recenzija/dodaj/', views.RecenzijaCreateView.as_view(), name='recenzija-create'),
    path('recenzija/<int:pk>/obrisi/', views.RecenzijaDeleteView.as_view(), name='obrisi-recenziju'),

    path('autori/', views.AutorListView.as_view(), name='autor-list'),
    path('autori/<int:pk>/', views.AutorDetailView.as_view(), name='autor-detail'),

    path('recenzije/', views.RecenzijaListView.as_view(), name='recenzija-list'),

    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/signup/", views.SignUpView.as_view(), name="register"),
]

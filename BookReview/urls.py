from django.urls import path
from . import views

urlpatterns = [
    path("", views.DjeloListView.as_view(), name="djelo-list"),
    path("djelo/<int:pk>/", views.DjeloDetailView.as_view(), name="djelo-detail"),
    path("autori/", views.AutorListView.as_view(), name="autor-list"),
]

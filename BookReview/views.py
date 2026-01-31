from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import Djelo, Autor, Recenzija
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class DjeloListView(ListView):
    model = Djelo
    template_name = "knjige/djelo_list.html"
    context_object_name = "djela"

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        if query:
            return Djelo.objects.filter(naslov__icontains=query)
        return Djelo.objects.all()

class DjeloDetailView(DetailView):
    model = Djelo
    template_name = "knjige/djelo_detail.html"

class AutorListView(ListView):
    model = Autor
    template_name = "knjige/autor_list.html"
    context_object_name = "autori"

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        if query:
            return Autor.objects.filter(ime__icontains=query) | Autor.objects.filter(prezime__icontains=query)
        return Autor.objects.all()

class AutorDetailView(DetailView):
    model = Autor
    template_name = "knjige/autor_detail.html"
    context_object_name = "autor"

class RecenzijaListView(ListView):
    model = Recenzija
    template_name = "knjige/recenzija_list.html"
    context_object_name = "recenzije"
    ordering = ['-datum'] 

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/register.html"

class RecenzijaDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Recenzija
    template_name = "registration/recenzija_confirm_delete.html"
    
    def get_success_url(self):
        return reverse_lazy('djelo-detail', kwargs={'pk': self.object.djelo.id})

    def test_func(self):
        obj = self.get_object()
        return obj.korisnik == self.request.user
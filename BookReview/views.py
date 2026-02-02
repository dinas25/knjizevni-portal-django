from django.shortcuts import render
from django.views.generic import (
    ListView, DetailView, CreateView, DeleteView, UpdateView
)
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Djelo, Autor, Recenzija
from .forms import DjeloForm, RecenzijaForm


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
            return (
                Autor.objects.filter(ime__icontains=query) |
                Autor.objects.filter(prezime__icontains=query)
            )
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


class DjeloCreateView(LoginRequiredMixin, CreateView):
    model = Djelo
    form_class = DjeloForm
    template_name = "knjige/djelo_form.html"
    success_url = reverse_lazy("djelo-list")

    def form_valid(self, form):
        form.instance.dodao = self.request.user
        return super().form_valid(form)


class DjeloUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Djelo
    form_class = DjeloForm
    template_name = "knjige/djelo_form.html"

    def get_success_url(self):
        return reverse_lazy("djelo-detail", kwargs={"pk": self.object.pk})

    def test_func(self):
        return self.request.user == self.get_object().dodao


class DjeloDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Djelo
    template_name = "knjige/djelo_confirm_delete.html"
    success_url = reverse_lazy("djelo-list")

    def test_func(self):
        return self.request.user == self.get_object().dodao


class RecenzijaCreateView(LoginRequiredMixin, CreateView):
    model = Recenzija
    form_class = RecenzijaForm
    template_name = "knjige/recenzija_form.html"

    def form_valid(self, form):
        form.instance.korisnik = self.request.user
        form.instance.djelo = Djelo.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            "djelo-detail",
            kwargs={"pk": self.kwargs['pk']}
        )


class RecenzijaDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Recenzija
    template_name = "knjige/recenzija_confirm_delete.html"

    def get_success_url(self):
        return reverse_lazy(
            "djelo-detail",
            kwargs={"pk": self.object.djelo.id}
        )

    def test_func(self):
        return self.get_object().korisnik == self.request.user


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/register.html"

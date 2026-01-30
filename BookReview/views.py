from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Djelo, Autor

class DjeloListView(ListView):
    model = Djelo
    template_name = "knjige/djelo_list.html"
    context_object_name = "djela"

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        if query:
            # __icontains traži slovo bilo gdje u naslovu, 
            # ako želiš samo na početku koristi __istartswith
            return Djelo.objects.filter(naslov__icontains=query)
        return Djelo.objects.all()


class DjeloDetailView(DetailView):
    model = Djelo
    template_name = "knjige/djelo_detail.html"


class AutorListView(ListView):
    model = Autor
    template_name = "knjige/autor_list.html"

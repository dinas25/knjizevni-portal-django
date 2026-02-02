from django import forms
from .models import Djelo, Recenzija

class DjeloForm(forms.ModelForm):
    class Meta:
        model = Djelo
        fields = ['naslov', 'opis', 'godina_izdanja', 'autor']
        labels = {
            'naslov': 'Naslov djela',
            'opis': 'Opis',
            'godina_izdanja': 'Godina izdanja',
            'autor': 'Autor'
        }


class RecenzijaForm(forms.ModelForm):
    class Meta:
        model = Recenzija
        fields = ['ocjena', 'komentar']
        labels = {
            'ocjena': 'Ocjena (1–5)',
            'komentar': 'Komentar'
        }


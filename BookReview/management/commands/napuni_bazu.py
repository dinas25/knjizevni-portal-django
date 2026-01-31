import factory
import random
import datetime
from django.core.management.base import BaseCommand
from django.db import transaction
from django.contrib.auth.models import User

from BookReview.models import Profil, Autor, Djelo, Recenzija
from BookReview.factory import (
    ProfilFactory,
    AutorFactory,
    DjeloFactory,
    RecenzijaFactory
)

NUM_PROFILS = 10
NUM_AUTORI = 15
NUM_RECENZIJE = 100

class Command(BaseCommand):
    help = "Generira logične testne (dummy) podatke"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Brisanje starih podataka...")
        Recenzija.objects.all().delete()
        Djelo.objects.all().delete()
        Autor.objects.all().delete()
        User.objects.filter(is_superuser=False).delete()

        self.stdout.write("Kreiranje novih podataka...")

        for _ in range(NUM_PROFILS):
            ProfilFactory()
        
        korisnici = User.objects.filter(is_superuser=False)

        for _ in range(NUM_AUTORI):
            AutorFactory(godina_rodenja=random.randint(1950, 2000))

        sva_djela = []
        for autor in Autor.objects.all():
            broj_djela = random.randint(1, 8)
            for _ in range(broj_djela):
                godina = random.randint(autor.godina_rodenja + 20, 2025)
                
                djelo = DjeloFactory(
                    autor=autor,
                    godina_izdanja=godina,
                    dodao=random.choice(korisnici)
                )
                sva_djela.append(djelo)

        self.stdout.write("Kreiranje recenzija...")
        danas = datetime.date.today()

        for _ in range(NUM_RECENZIJE):
            if sva_djela:
                izabrano_djelo = random.choice(sva_djela)
                
                g_izdanja = int(izabrano_djelo.godina_izdanja)
                pocetak = datetime.date(g_izdanja, 1, 1)
                
                razlika_dana = (danas - pocetak).days
                if razlika_dana <= 0:
                    logican_datum = danas
                else:
                    nasumicni_broj_dana = random.randint(0, razlika_dana)
                    logican_datum = pocetak + datetime.timedelta(days=nasumicni_broj_dana)

                RecenzijaFactory(
                    djelo=izabrano_djelo,
                    korisnik=random.choice(korisnici),
                    datum=logican_datum 
                )

        self.stdout.write(self.style.SUCCESS(f"Uspješno generirano {Autor.objects.count()} autora i {Djelo.objects.count()} djela!"))
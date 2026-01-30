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

NUM_PROFILS = 5
NUM_AUTORI = 10
NUM_DJELA = 30
NUM_RECENZIJE = 100


class Command(BaseCommand):
    help = "Generira testne (dummy) podatke"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Brisanje starih podataka...")

        Recenzija.objects.all().delete()
        Djelo.objects.all().delete()
        Autor.objects.all().delete()
        Profil.objects.filter(user__is_superuser=False).delete()

        self.stdout.write("Kreiranje novih podataka...")

        for _ in range(NUM_PROFILS):
            ProfilFactory()

        for _ in range(NUM_AUTORI):
            AutorFactory()

        for _ in range(NUM_DJELA):
            DjeloFactory()

        for _ in range(NUM_RECENZIJE):
            RecenzijaFactory()

        self.stdout.write(self.style.SUCCESS("Testni podaci uspješno generirani!"))

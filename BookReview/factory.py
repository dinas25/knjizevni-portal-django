import factory
from factory.django import DjangoModelFactory
from django.contrib.auth.models import User

from .models import Autor, Djelo, Recenzija, Profil


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("user_name")
    email = factory.Faker("email")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")


class ProfilFactory(DjangoModelFactory):
    class Meta:
        model = Profil

    user = factory.SubFactory(UserFactory)
    bio = factory.Faker("sentence", nb_words=10)


class AutorFactory(DjangoModelFactory):
    class Meta:
        model = Autor

    ime = factory.Faker("first_name")
    prezime = factory.Faker("last_name")
    godina_rodenja = factory.Faker("year")


class DjeloFactory(DjangoModelFactory):
    class Meta:
        model = Djelo

    naslov = factory.Faker("sentence", nb_words=4)
    opis = factory.Faker("text", max_nb_chars=300)
    godina_izdanja = factory.Faker("year")
    autor = factory.SubFactory(AutorFactory) 
    dodao = factory.SubFactory(UserFactory)

class RecenzijaFactory(DjangoModelFactory):
    class Meta:
        model = Recenzija

    djelo = factory.SubFactory(DjeloFactory)
    korisnik = factory.SubFactory(UserFactory)
    ocjena = factory.Faker("random_int", min=1, max=5)
    komentar = factory.Faker("sentence", nb_words=15)
    datum = factory.Faker("date_this_century")

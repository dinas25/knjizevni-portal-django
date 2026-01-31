from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    datum_registracije = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Autor(models.Model):
    ime = models.CharField(max_length=100)
    prezime = models.CharField(max_length=100)
    godina_rodenja = models.IntegerField()

    def __str__(self):
        return f"{self.ime} {self.prezime}"


class Djelo(models.Model):
    naslov = models.CharField(max_length=200)
    opis = models.TextField()
    godina_izdanja = models.IntegerField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    dodao = models.ForeignKey(User, on_delete=models.CASCADE)
    datum_dodavanja = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.naslov


class Recenzija(models.Model):
    djelo = models.ForeignKey(
        Djelo,
        on_delete=models.CASCADE,
        related_name="recenzije"
    )
    korisnik = models.ForeignKey(User, on_delete=models.CASCADE)
    ocjena = models.IntegerField()
    komentar = models.TextField()
    datum = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.djelo} - {self.ocjena}"

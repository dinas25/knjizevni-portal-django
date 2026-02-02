from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from .models import Autor, Djelo, Recenzija


class AutorModelTest(TestCase):
    def test_kreiranje_autora(self):
        autor = Autor.objects.create(
            ime="Ivo",
            prezime="Andrić",
            godina_rodenja=1892
        )

        self.assertEqual(autor.ime, "Ivo")
        self.assertEqual(autor.prezime, "Andrić")
        self.assertEqual(str(autor), "Ivo Andrić")


class DjeloModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="test12345"
        )

        self.autor = Autor.objects.create(
            ime="Miroslav",
            prezime="Krleža",
            godina_rodenja=1893
        )

    def test_kreiranje_djela(self):
        djelo = Djelo.objects.create(
            naslov="Gospoda Glembajevi",
            opis="Drama o raspadu obitelji",
            godina_izdanja=1929,
            autor=self.autor,
            dodao=self.user
        )

        self.assertEqual(djelo.naslov, "Gospoda Glembajevi")
        self.assertEqual(djelo.autor.prezime, "Krleža")
        self.assertEqual(djelo.dodao.username, "testuser")


class RecenzijaModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="recenzent",
            password="lozinka123"
        )

        self.autor = Autor.objects.create(
            ime="Ranko",
            prezime="Marinković",
            godina_rodenja=1913
        )

        self.djelo = Djelo.objects.create(
            naslov="Kiklop",
            opis="Roman o ratu",
            godina_izdanja=1965,
            autor=self.autor,
            dodao=self.user
        )

    def test_kreiranje_recenzije(self):
        recenzija = Recenzija.objects.create(
            djelo=self.djelo,
            korisnik=self.user,
            ocjena=5,
            komentar="Izvrsno djelo"
        )

        self.assertEqual(recenzija.djelo.naslov, "Kiklop")
        self.assertEqual(recenzija.ocjena, 5)
        self.assertEqual(recenzija.korisnik.username, "recenzent")


class DjeloListViewTest(TestCase):
    def test_djelo_list_view_status_code(self):
        response = self.client.get(reverse("djelo-list"))
        self.assertEqual(response.status_code, 200)

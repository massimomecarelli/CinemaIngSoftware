from unittest import TestCase

from film.model.Film import Film
from lista_film.model.ListaFilm import ListaFilm


class TestListaFilm(TestCase):

    def crea_ambiente_test(self):
        self.lista_film = ListaFilm()
        film = Film("Film", "descrizione", "Attore", "100")
        self.lista_film.aggiungi_film(film)

    def test_rimuovi_film_by_name(self):
        self.crea_ambiente_test()
        self.assertFalse(self.lista_film.rimuovi_film_by_name("Film123"))
        self.assertTrue(self.lista_film.rimuovi_film_by_name("Film"))

    def test_get_fim_by_name(self):
        self.crea_ambiente_test()
        self.assertIsNone(self.lista_film.get_film_by_name("Film123"))
        self.assertIsNotNone(self.lista_film.get_film_by_name("Film"))

    def test_get_lista_film(self):
        self.crea_ambiente_test()
        self.assertNotEqual(self.lista_film.get_lista_film(), []) # non deve essere una lista nulla

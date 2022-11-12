from lista_film.model.ListaFilm import ListaFilm


class ControlloreListaFilm:

    def __init__(self):
        self.model = ListaFilm()

    def aggiungi_film(self, film):
        self.model.aggiungi_film(film)

    def get_lista_film(self):
        return self.model.get_lista_film()

    def get_film_by_name(self, nome_film):
        return self.model.get_film_by_name(nome_film)

    def elimina_film_by_name(self, nome_film):
        self.model.rimuovi_film_by_name(nome_film)

    def save_data(self):
        self.model.save_data()


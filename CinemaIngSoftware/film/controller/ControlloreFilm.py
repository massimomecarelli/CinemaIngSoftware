from film.model.Film import Film


class ControlloreFilm:

    def __init__(self):
        self.model = Film()

    def get_nome_film(self):
        return self.model.get_nome_film()

    def get_attori(self):
        return self.model.get_attori()

    def get_descrizione (self):
        return self.model.get_descrizione()

    def get_durata(self):
        return self.model.get_durata()


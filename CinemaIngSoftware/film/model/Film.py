class Film:

    def __init__(self, nome_film, descrizione, attori, durata):
        self.nome_film = nome_film
        self.descrizione = descrizione
        self.attori = attori
        self.durata = durata

    def get_nome_film(self):
        return self.nome_film

    def get_attori(self):
        return self.attori

    def get_descrizione (self):
        return self.descrizione

    def get_durata(self):
        return self.durata


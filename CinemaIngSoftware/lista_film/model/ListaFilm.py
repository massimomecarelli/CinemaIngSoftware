import os
import pickle


class ListaFilm():

    def __init__(self):
        super(ListaFilm, self).__init__()
        # Carica la lista film dal file lista_film_data.pickle, se questo non esiste inizializza una lista vuota
        # Se invece il file esiste, inizializza la lista con il suo contenuto
        self.lista_film = []
        if os.path.isfile("lista_film/data/lista_film_data.pickle"):
            with open("lista_film/data/lista_film_data.pickle", "rb") as file:
                self.lista_film = pickle.load(file)

    def aggiungi_film(self, film):
        self.lista_film.append(film)

    def rimuovi_film_by_name(self, nome_film):
        for film in self.lista_film:
            if film.nome_film == nome_film:
                self.lista_film.remove(film)
                return True
        return False

    def get_lista_film(self):
        return self.lista_film

    def get_film_by_name(self, nome_film):
        for film in self.lista_film:
            if film.nome_film == nome_film:
                return film #se lo username già esiste a sistema, la funzione torna qualcosa (per la registrazione è interpretato come true, che quindi permette di entrare nel primo elif di registra_cliente in VistaRegistrazione)
        return None #cioè interpretato come false dagli if (quindi lo username non esiste già a sistema)

    def save_data(self):
        with open("lista_film/data/lista_film_data.pickle", "wb") as handle: #apre il pickle per la scrittura (come stream di byte)
            pickle.dump(self.lista_film, handle, pickle.HIGHEST_PROTOCOL)

import os
import pickle


class ListaPrenotazioni:

    def __init__(self):
        self.lista_prenotazioni = []
        if os.path.isfile("lista_prenotazioni/data/lista_prenotazioni_salvata.pickle"):
            with open("lista_prenotazioni/data/lista_prenotazioni_salvata.pickle", "rb") as file:
                self.lista_prenotazioni = pickle.load(file)

    # Aggiungo una prenotazione e riordino la lista in base alle date, in modo decrescente dalla più recente alla meno recente
    def aggiungi_prenotazione(self, prenotazione):
        self.lista_prenotazioni.append(prenotazione)
        self.lista_prenotazioni.sort(reverse=True)

    def get_lista_prenotazioni(self):
        return self.lista_prenotazioni

    #Ritorna una lista di prenotazioni con le sole prenotazioni effettuate dal cliente al quale è associato lo username passato
    def get_lista_prenotazioni_cliente(self, username):
        lista_ritorno = []
        for prenotazione in self.lista_prenotazioni:
            if prenotazione.username_cliente == username:
                lista_ritorno.append(prenotazione)
        return lista_ritorno

    #Elimina tutte le prenotazioni del cliente al quale è associato lo username passato come argomento
    def elimina_prenotazioni_cliente(self, username_cliente):
        for prenotazione in self.lista_prenotazioni:
            if prenotazione.username_cliente == username_cliente:
                self.lista_prenotazioni.remove(prenotazione)

    #Elimina la prenotazione del cliente al quale è associato lo username, nella data passata come argomento in formato datetime
    def elimina_prenotazione_singola(self, username, data):
        for prenotazione in self.lista_prenotazioni:
            if prenotazione.username_cliente == username and prenotazione.data == data:
                self.lista_prenotazioni.remove(prenotazione)
                return

    def save_data(self):
        with open("lista_prenotazioni/data/lista_prenotazioni_salvata.pickle", "wb") as handle:
            pickle.dump(self.lista_prenotazioni, handle, pickle.HIGHEST_PROTOCOL)

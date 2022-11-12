from lista_prenotazioni.model.ListaPrenotazioni import ListaPrenotazioni


class ControlloreListaPrenotazioni:

    def __init__(self):
        self.model = ListaPrenotazioni()

    def get_lista_prenotazioni(self):
        return self.model.get_lista_prenotazioni()

    def aggiungi_prenotazione(self, prenotazione):
        self.model.aggiungi_prenotazione(prenotazione)

    def get_lista_prenotazioni_cliente(self, username_cliente):
        return self.model.get_lista_prenotazioni_cliente(username_cliente)

    def elimina_prenotazioni_cliente(self, username_cliente):
        self.model.elimina_prenotazioni_cliente(username_cliente)

    def elimina_prenotazione_singola(self, username_cliente, data):
        self.model.elimina_prenotazione_singola(username_cliente, data)

    def save_data(self):
        self.model.save_data()

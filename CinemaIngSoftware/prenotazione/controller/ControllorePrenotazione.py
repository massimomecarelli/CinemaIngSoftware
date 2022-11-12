class ControllorePrenotazione:

    def __init__(self, prenotazione):
        self.model = prenotazione

    def get_username_prenotazione(self):
        return self.model.username_cliente

    def get_data_prenotazione(self):
        return self.model.data

    def get_film_prenotazione(self):
        return self.model.film

    def get_numero_spettacolo(self):
        return self.model.numero_spettacolo

    def get_numero_biglietti(self):
        return self.model.numero_biglietti

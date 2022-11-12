class Prenotazione:

    def __init__(self, username_cliente,  numero_biglietti, nome_film, data, numero_spettacolo):
        self.username_cliente = username_cliente
        self.data = data
        self.nome_film = nome_film
        self.numero_biglietti = numero_biglietti
        self.numero_spettacolo = numero_spettacolo

    def __lt__(self, other): #controlla la data di prenotazione
        return self.data < other.data

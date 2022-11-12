import os
import pickle


class ListaClienti():

    def __init__(self):
        super(ListaClienti, self).__init__()
        #Carica la lista clienti dal file lista_clienti_data.pickle, se questo non esiste inizializza una lista vuota
        #Se invece il file esiste, inizializza la lista con il suo contenuto
        self.lista_clienti = []
        if os.path.isfile("lista_clienti/data/lista_clienti_data.pickle"):
            with open("lista_clienti/data/lista_clienti_data.pickle", "rb") as file:
                self.lista_clienti = pickle.load(file)

    def aggiungi_cliente(self, cliente):
        self.lista_clienti.append(cliente)

    def rimuovi_cliente_by_user(self, username):
        for cliente in self.lista_clienti:
            if cliente.username == username:
                self.lista_clienti.remove(cliente)
                return True
        return False

    def get_lista_clienti(self):
        return self.lista_clienti

    def get_cliente_by_user(self, username):
        for cliente in self.lista_clienti:
            if cliente.username == username:
                return cliente #se lo username già esiste a sistema, la funzione torna qualcosa (per la registrazione è interpretato come true, che quindi permette di entrare nel primo elif di registra_cliente in VistaRegistrazione)
        return None #cioè interpretato come false dagli if (quindi lo username non esiste già a sistema)

    def save_data(self):
        with open("lista_clienti/data/lista_clienti_data.pickle", "wb") as handle: #apre il pickle per la scrittura (come stream di byte)
            pickle.dump(self.lista_clienti, handle, pickle.HIGHEST_PROTOCOL)

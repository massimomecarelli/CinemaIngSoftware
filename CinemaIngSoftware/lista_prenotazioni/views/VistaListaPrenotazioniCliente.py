from PyQt5 import QtCore
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QListView, QHBoxLayout, QPushButton, QMessageBox
from PyQt5.QtGui import QFont, QStandardItemModel, QStandardItem, QIcon, QCursor
from datetime import datetime

from lista_prenotazioni.controller.ControlloreListaPrenotazioni import ControlloreListaPrenotazioni
from prenotazione.views.VistaNuovaPrenotazione import VistaNuovaPrenotazione
from prenotazione.controller.ControllorePrenotazione import ControllorePrenotazione
from prenotazione.views.VistaPrenotazione import VistaPrenotazione


class VistaListaPrenotazioniCliente(QWidget):

    def __init__(self, username_cliente, parent=None):
        super(VistaListaPrenotazioniCliente, self).__init__(parent)
        self.controllore_lista_prenotazioni = ControlloreListaPrenotazioni()
        self.username_cliente = username_cliente

        self.v_layout = QVBoxLayout()
        self.setStyleSheet("background-color: rgb(65, 65, 65);")

        self.label_prenotazioni = QLabel("Storico Prenotazioni: ")
        self.label_prenotazioni.setFont(QFont("American Typewriter", 18, 50))
        self.label_prenotazioni.setStyleSheet("color: white;")
        self.v_layout.addWidget(self.label_prenotazioni)

        self.lista_prenotazioni = QListView()
        self.lista_prenotazioni.setStyleSheet("background-color: white;")
        self.aggiorna_dati_prenotazioni()
        self.v_layout.addWidget(self.lista_prenotazioni)

        self.h_layout = QHBoxLayout()

        self.create_button("Nuova Prenotazione", self.go_nuova_prenotazione, "background-color: rgb(200, 70, 70);")
        self.create_button("Dettagli", self.apri_prenotazione, "background-color: rgb(28,162,239);")
        self.create_button("Elimina", self.conferma_elimina_prenotazione, "background-color: rgb(184,239,2);")

        self.v_layout.addLayout(self.h_layout)
        self.setLayout(self.v_layout)
        self.resize(350, 550)
        self.setWindowTitle("Prenotazioni")

    #Crea un bottone con i parametri passati e lo aggiunge al layout dei bottoni
    def create_button(self, testo, comando, background_color):
        bottone = QPushButton(testo)
        bottone.setFont(QFont("American Typewriter", 14))
        bottone.setStyleSheet(background_color + " border-radius: 8;" + "padding: 2px")
        bottone.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        bottone.clicked.connect(comando)
        self.h_layout.addWidget(bottone)

    #Funzione di callback che aggiorna i dati delle prenotazioni visualizzate
    def aggiorna_dati_prenotazioni(self):
        self.modello_lista_prenotazioni = QStandardItemModel()
        self.controllore_lista_prenotazioni = ControlloreListaPrenotazioni()
        for prenotazione in self.controllore_lista_prenotazioni.get_lista_prenotazioni_cliente(self.username_cliente):
            item = QStandardItem()
            item.setText("Prenotazione del " + prenotazione.data.strftime("%d/%m/%Y"))
            item.setEditable(False)
            item.setFont(QFont("American Typewriter", 16))
            self.modello_lista_prenotazioni.appendRow(item)
        self.lista_prenotazioni.setModel(self.modello_lista_prenotazioni)

    #Visualizza la finestra per creare una nuova prenotazione
    def go_nuova_prenotazione(self):
        self.vista_nuova_prenotazione = VistaNuovaPrenotazione(self.username_cliente, self.aggiorna_dati_prenotazioni)
        self.vista_nuova_prenotazione.show()

    #Viuslizza i dettagli della prenotazione selezionata, se non è stata selezionata alcuna prenotazione mostra un messaggio di errore
    def apri_prenotazione(self):
        try:
            indice = self.lista_prenotazioni.selectedIndexes()[0].row()
            da_visualizzare = self.controllore_lista_prenotazioni.get_lista_prenotazioni_cliente(self.username_cliente)[indice]
        except:
            QMessageBox.critical(self, "Errore", "Seleziona la prenotazione da visualizzare", QMessageBox.Ok, QMessageBox.Ok)
            return

        self.vista_prenotazione = VistaPrenotazione(ControllorePrenotazione(da_visualizzare))
        self.vista_prenotazione.show()

    #Chiede conferma dell'eliminazione di una prenotazione, in caso affermativo la cancella
    def conferma_elimina_prenotazione(self):
        try:
            indice = self.lista_prenotazioni.selectedIndexes()[0].row()
            da_eliminare = self.controllore_lista_prenotazioni.get_lista_prenotazioni_cliente(self.username_cliente)[indice]
        except:
            QMessageBox.critical(self, "Errore", "Seleziona la prenotazione da eliminare", QMessageBox.Ok,QMessageBox.Ok)
            return

        if da_eliminare.data < datetime.now():
            QMessageBox.critical(self, "Errore", "Non puoi cancellare prenotazioni passate", QMessageBox.Ok, QMessageBox.Ok)
            return
        risposta = QMessageBox.question(self, "Elimina prenotazione",
                               "Sei sicuro di voler elimare la prenotazione selezionata?", QMessageBox.Yes,
                               QMessageBox.No)
        if risposta == QMessageBox.Yes:
            self.controllore_lista_prenotazioni.elimina_prenotazione_singola(self.username_cliente, da_eliminare.data)
            self.controllore_lista_prenotazioni.save_data()
            self.aggiorna_dati_prenotazioni()
        else:
            return

from PyQt5 import QtCore
from PyQt5.QtGui import QFont, QStandardItem, QStandardItemModel, QKeySequence, QCursor
from PyQt5.QtWidgets import QListView, QVBoxLayout, QLabel, QWidget, QPushButton, QMessageBox, QShortcut, \
    QAbstractItemView
from PyQt5.QtCore import Qt

from lista_prenotazioni.controller.ControlloreListaPrenotazioni import ControlloreListaPrenotazioni
from prenotazione.controller.ControllorePrenotazione import ControllorePrenotazione
from prenotazione.views.VistaPrenotazione import VistaPrenotazione



class VistaListaPrenotazioniAdmin(QWidget):

    def __init__(self, data=None, parent=None):
        super(VistaListaPrenotazioniAdmin, self).__init__(parent)
        self.controllore_lista_prenotazioni = ControlloreListaPrenotazioni()
        self.move(100, 0)
        self.data = data
        self.setStyleSheet("background-color: rgb(220, 220, 220);")

        self.v_layout = QVBoxLayout()
        self.font = QFont("Arial", 16, 15)

        # Se non è stata passata alcuna data visualizza tutte le prenotazioni, altrimenti visualizza le prenotazioni in quella data
        if data is not None:
            self.label_prenotazioni_by_data = QLabel("Prenotazioni per il giorno " + data.strftime("%d/%m/%Y") + ":")
        else:
            self.label_prenotazioni_by_data = QLabel("Tutte le prenotazioni: ")
        self.label_prenotazioni_by_data.setStyleSheet("font:  20pt \"American Typewriter\";")
        self.label_prenotazioni_by_data.setAlignment(Qt.AlignCenter)
        self.v_layout.addWidget(self.label_prenotazioni_by_data)
        self.v_layout.addSpacing(15)

        self.lista_prenotazioni = QListView()
        self.lista_prenotazioni.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.aggiorna_dati_prenotazioni()
        self.v_layout.addWidget(self.lista_prenotazioni)

        self.bottone_dettagli_prenotazione = QPushButton("Dettagli prenotazione")
        self.bottone_dettagli_prenotazione.setFont(self.font)
        self.bottone_dettagli_prenotazione.setStyleSheet("background-color: rgb(200, 70, 70);" "border-radius: 8;" "color: #FFFFFF;" "padding: 5px;")
        self.bottone_dettagli_prenotazione.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.bottone_dettagli_prenotazione.clicked.connect(self.dettagli_prenotazione)
        self.shortcut_open = QShortcut(QKeySequence('Return'), self)
        self.shortcut_open.activated.connect(self.dettagli_prenotazione)
        self.v_layout.addWidget(self.bottone_dettagli_prenotazione)
        self.v_layout.addSpacing(15)

        # Se è stata passata una data, verrà creato nella finestra un sezione con delle statistiche
        if data is not None:
            self.label_stats = QLabel("Statistiche sulle prenotazioni:")
            self.label_stats.setAlignment(Qt.AlignCenter)
            self.label_stats.setStyleSheet("font:  18pt \"American Typewriter\";" "background-color: rgb(255, 255, 255);")
            self.v_layout.addWidget(self.label_stats)
            self.lista_stats = QListView()
            self.get_stats(data)
            self.lista_stats.setAlternatingRowColors(True)
            self.lista_stats.setEditTriggers(QAbstractItemView.NoEditTriggers)
            self.v_layout.addWidget(self.lista_stats)

        self.setLayout(self.v_layout)
        self.resize(900, 800)
        self.setWindowTitle("Lista Prenotazioni")

    # Ottiene i dati delle prenotazioni e li mette nella lista visualizzata
    def aggiorna_dati_prenotazioni(self):
        self.modello_lista_prenotazioni = QStandardItemModel()

        for prenotazione in self.controllore_lista_prenotazioni.get_lista_prenotazioni():

            if self.data == prenotazione.data:
                item = QStandardItem()
                item.setText("Prenotazione del " + prenotazione.data.strftime("%d/%m/%Y") + " effettuata da " + prenotazione.username_cliente)
                item.setEditable(False)
                item.setFont(self.font)
                self.modello_lista_prenotazioni.appendRow(item)
            elif self.data is None:
                item = QStandardItem()
                item.setText("Prenotazione del " + prenotazione.data.strftime("%d/%m/%Y") + " effettuata da " + prenotazione.username_cliente)
                item.setEditable(False)
                item.setFont(self.font)
                self.modello_lista_prenotazioni.appendRow(item)

        self.lista_prenotazioni.setModel(self.modello_lista_prenotazioni)

    # Visualizza i dettagli della prenotazione selezionata, se non ne è stata selezionata alcuna data, mostra un messaggio di errore
    def dettagli_prenotazione(self):
        try:
            indice = self.lista_prenotazioni.selectedIndexes()[0].row()
            if self.data is not None:
                lista_prenotazioni_filtrata = []
                for prenotazione in self.controllore_lista_prenotazioni.get_lista_prenotazioni():
                    if prenotazione.data == self.data:
                        lista_prenotazioni_filtrata.append(prenotazione)
                da_visualizzare = lista_prenotazioni_filtrata[indice]
            else:
                da_visualizzare = self.controllore_lista_prenotazioni.get_lista_prenotazioni()[indice]
        except:
            QMessageBox.critical(self, "Errore", "Seleziona la prenotazione da visualizzare", QMessageBox.Ok, QMessageBox.Ok)
            return
        # viene visualizzata una vista prenotazione a cui viene passato come parametro il controllore con il parametro di tipo Prenotazione
        self.vista_prenotazione = VistaPrenotazione(ControllorePrenotazione(da_visualizzare))
        self.vista_prenotazione.show()

    # Crea un riepilogo con le statistiche nella data passata come argomento
    def get_stats(self, data_controllo_stats):
        self.modello_statistiche = QStandardItemModel()

        # Inizializza le statistiche a 0
        numero_biglietti_prenotati = 0
        numero_tot_prenotazioni = 0

        for prenotazione in self.controllore_lista_prenotazioni.get_lista_prenotazioni():

            # Controllo che prende le prenotazioni nella data usata per filtrare le statistiche
            if data_controllo_stats == prenotazione.data:

                # Se il controllo dà esito positivo, viene aggiunto il numero di biglietti alla statistica totale
                numero_biglietti = prenotazione.numero_biglietti
                numero_biglietti_prenotati = numero_biglietti_prenotati + numero_biglietti
                # numero di prenotazioni effettuate da account unici
                numero_tot_prenotazioni = numero_tot_prenotazioni + 1


        # I dati vengono aggiunti alla lista delle statistiche tramite degli item
        item_biglietti = QStandardItem()
        item_biglietti.setFont(self.font)
        item_biglietti.setEditable(False)
        item_biglietti.setText("Biglietti totali prenotati: " + str(numero_biglietti_prenotati))
        self.modello_statistiche.appendRow(item_biglietti)

        item_prenotazioni_tot = QStandardItem()
        item_prenotazioni_tot.setFont(self.font)
        item_prenotazioni_tot.setEditable(False)
        item_prenotazioni_tot.setText("Account che hanno effettuato prenotazioni: " + str(numero_tot_prenotazioni))
        self.modello_statistiche.appendRow(item_prenotazioni_tot)

        self.lista_stats.setModel(self.modello_statistiche)

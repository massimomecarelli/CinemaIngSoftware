from PyQt5.QtCore import QDate
from PyQt5.QtGui import QFont, QStandardItemModel, QStandardItem, QTextCharFormat, QColor, QKeySequence
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QCalendarWidget, QComboBox, QMessageBox, \
    QPushButton, QShortcut, QSpinBox
from datetime import datetime, timedelta


from lista_prenotazioni.controller.ControlloreListaPrenotazioni import ControlloreListaPrenotazioni
from lista_film.model.ListaFilm import ListaFilm
from prenotazione.model.Prenotazione import Prenotazione


class VistaNuovaPrenotazione(QWidget):

    def __init__(self, username_cliente, aggiorna_dati_prenotazioni, parent=None):
        super(VistaNuovaPrenotazione, self).__init__(parent)
        self.font = QFont("American Typewriter", 17)
        self.username_cliente = username_cliente
        self.aggiorna_dati_prenotazioni = aggiorna_dati_prenotazioni

        self.layout = QGridLayout()

        # prenotazione data spettacolo
        self.label_data = QLabel("Seleziona la data dello spettacolo:")
        self.label_data.setStyleSheet("font: 500 15pt \"American Typewriter\";\n""color: rgb(255, 255, 255);\n" "background-color: rgb(255, 75, 75);\n""selection-color: rgb(170, 255, 0);")
        self.layout.addWidget(self.label_data, 0, 0)

        self.calendario = QCalendarWidget()
        self.calendario.setGridVisible(True)
        self.calendario.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        if datetime.now() > datetime(2022, 11, 20):
            self.calendario.setMinimumDate(QDate(datetime.now().year, datetime.now().month, datetime.now().day))
        else:
            self.calendario.setMinimumDate(QDate(2022, 11, 20))
        self.calendario.setMaximumDate(QDate(2023, 2, 20))

        cell_start = QTextCharFormat()
        cell_start.setBackground(QColor("green"))
        cell_stop = QTextCharFormat()
        cell_stop.setBackground(QColor("red"))
        self.calendario.setDateTextFormat(self.calendario.selectedDate(), cell_start)
        self.calendario.setDateTextFormat(QDate(2023, 2, 20), cell_stop)

        self.layout.addWidget(self.calendario, 1, 0)


        # selezione spettacolo
        self.label_numero_spettacolo = QLabel("Seleziona l'orario dello spettacolo:")
        self.label_numero_spettacolo.setStyleSheet("font: 500 15pt \"American Typewriter\";\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "background-color: rgb(255, 75, 75);\n"
                                          "selection-color: rgb(170, 255, 0);")
        self.layout.addWidget(self.label_numero_spettacolo, 3, 0)

        # selezione film
        self.label_film = QLabel("Seleziona il film:")
        self.label_film.setStyleSheet("font: 500 15pt \"American Typewriter\";\n"
                                                      "color: rgb(255, 255, 255);\n"
                                                      "background-color: rgb(255, 75, 75);\n"
                                                      "selection-color: rgb(170, 255, 0);")
        self.layout.addWidget(self.label_film, 5, 0)

         # selezione numero di biglietti
        self.label_numero_biglietti = QLabel("Numero di biglietti:")
        self.label_numero_biglietti.setStyleSheet("font: 500 15pt \"American Typewriter\";\n"
                                                      "color: rgb(255, 255, 255);\n"
                                                      "background-color: rgb(255, 75, 75);\n"
                                                      "selection-color: rgb(170, 255, 0);")
        self.layout.addWidget(self.label_numero_biglietti, 7, 0)

        self.get_film()

        # bottone di conferma
        self.bottone_conferma = QPushButton("Prenota Ora")
        self.bottone_conferma.setFont(QFont("American Typewriter", 17, 100, True))
        self.bottone_conferma.setStyleSheet("background-color: rgb(31,219,6);")
        self.bottone_conferma.clicked.connect(self.conferma_prenotazione)
        self.shortcut_open = QShortcut(QKeySequence('Return'), self)
        self.shortcut_open.activated.connect(self.conferma_prenotazione)
        self.layout.addWidget(self.bottone_conferma, 9, 0)

        self.setLayout(self.layout)
        self.resize(1000, 600)
        self.setWindowTitle("Conferma Prenotazione")


    def get_film(self):
        self.lista_film = ListaFilm()

        self.font_combo_box = QFont("American Typewriter", 12)

        # menu a tendina per selezionare il film
        self.menu_film = QComboBox()
        self.menu_film.setFont(self.font_combo_box)
        self.model_menu_film = QStandardItemModel(self.menu_film)

        # menu a tendina per stabilire lo spettacolo giornaliero
        self.menu_numero_spettacolo = QComboBox()
        self.menu_numero_spettacolo.setFont(self.font_combo_box)
        self.model_menu_numero_spettacolo = QStandardItemModel(self.menu_numero_spettacolo)

        # Spin box per stabilire il numero di biglietti che si vogliono prendere
        self.menu_numero_biglietti = QSpinBox()
        self.menu_numero_biglietti.setRange(1, 10)
        self.menu_numero_biglietti.setFont(self.font_combo_box)
        self.model_menu_numero_biglietti = QStandardItemModel(self.menu_numero_biglietti)

        for film in self.lista_film.get_lista_film():
            item = QStandardItem()
            item.setText(film.nome_film)
            item.setEditable(False)
            self.model_menu_film.appendRow(item)
        self.menu_film.setModel(self.model_menu_film)

        self.orario=14
        for spettacolo in [1, 2, 3]:
            item = QStandardItem()
            item.setText(str(self.orario) + ":00")
            self.orario += 2
            item.setEditable(False)
            self.model_menu_numero_spettacolo.appendRow(item)
        self.menu_numero_spettacolo.setModel(self.model_menu_numero_spettacolo)

        self.layout.addWidget(self.menu_numero_spettacolo, 4, 0)
        self.layout.addWidget(self.menu_film, 6, 0)
        self.layout.addWidget(self.menu_numero_biglietti, 8, 0)


    # Controlla i dati inseriti nella prenotazione e se sono corretti registra la prenotazione
    def conferma_prenotazione(self):
        # Trasforma le date prese dal calendario da QDate a datetime
        data_selected = self.calendario.selectedDate()
        data = datetime(data_selected.year(), data_selected.month(), data_selected.day())

        # Controlla che la data della prenotazione sia almeno il giorno successivo a quando la si effettua
        if data == datetime(datetime.now().year, datetime.now().month, datetime.now().day):
            QMessageBox.critical(self, "Errore", "La prenotazione non può partire da oggi", QMessageBox.Ok, QMessageBox.Ok)
            return
    # prendo i valori selezionati in numero di biglietti e l'orario dello spettacolo
        film = self.menu_film.currentText()
        numero_biglietti = self.menu_numero_biglietti.value()
        numero_spettacolo = self.menu_numero_spettacolo.currentText()

        prenotazione = Prenotazione(self.username_cliente, numero_biglietti, film, data, numero_spettacolo)

        # Chiede la conferma per la prenotazione
        risposta = QMessageBox.question(self, "Confermare la prenotazione?", "", QMessageBox.Yes, QMessageBox.No)
        if risposta == QMessageBox.No:
            return
        else:
            controllore_lista_prenotazioni = ControlloreListaPrenotazioni()
            controllore_lista_prenotazioni.aggiungi_prenotazione(prenotazione)
            QMessageBox.about(self, "Confermata", "La Prenotazione è stata Confermata")
            controllore_lista_prenotazioni.save_data()
            self.aggiorna_dati_prenotazioni()
            self.close()

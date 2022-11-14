from PyQt5 import Qt
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QCalendarWidget, QHBoxLayout, QPushButton
from PyQt5.QtGui import QFont
from datetime import datetime

from lista_prenotazioni.views.VistaListaPrenotazioniAdmin import VistaListaPrenotazioniAdmin


class VistaListaPrenotazioni(QWidget):

    def __init__(self, parent=None):
        super(VistaListaPrenotazioni, self).__init__(parent)

        self.g_layout = QGridLayout()

        self.label_prenotazioni_by_data = QLabel("\nSeleziona una data\n")
        self.label_prenotazioni_by_data.setStyleSheet("font: 30 17pt \"American Typewriter\";\n""color: rgb(255, 255, 255);\n"
                                                    "background-color: rgb(200, 70, 70);\n"
                                                    "selection-color: rgb(170, 255, 0);" "border-radius: 8;")
        self.label_prenotazioni_by_data.setAlignment(Qt.AlignCenter)
        self.g_layout.addWidget(self.label_prenotazioni_by_data, 0, 0)

        self.calendario = QCalendarWidget()
        self.calendario.setGridVisible(True)
        self.calendario.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.calendario.setMinimumDate(QDate(2022, 11, 20))
        self.calendario.setMaximumDate(QDate(2023, 2, 15))

        self.g_layout.addWidget(self.calendario, 1, 0)

        self.h_layout = QHBoxLayout()

        self.create_button("Mostra tutte", self.go_lista_prenotazioni, "background-color: rgb(28,162,239);")
        self.create_button("Cerca", self.go_lista_prenotazioni_by_data, "background-color: rgb(200, 70, 70);")

        self.g_layout.addLayout(self.h_layout, 2, 0)

        self.setLayout(self.g_layout)
        self.resize(700, 600)
        self.setWindowTitle("Lista Prenotazioni")

    # Crea un bottone con i parametri passati e lo aggiunge al layout orizzontale dei bottoni
    def create_button(self, testo, comando, background_color):
        bottone = QPushButton(testo)
        bottone.setFont(QFont("American Typewriter", 15, 30))
        bottone.setStyleSheet(background_color + " " + " border-radius: 8;" "padding: 5px;" "color: #FFFFFF")
        bottone.clicked.connect(comando)
        self.h_layout.addWidget(bottone)

    # Visualizza la lista delle prenotazioni che iniziano nella data selezionata nel calendario
    def go_lista_prenotazioni_by_data(self):
        data = self.calendario.selectedDate()
        formato_data = datetime(data.year(), data.month(), data.day())
        self.lista_prenotazioni_by_data = VistaListaPrenotazioniAdmin(formato_data)
        self.lista_prenotazioni_by_data.show()

    # Visualizza la lista completa delle prenotazioni
    def go_lista_prenotazioni(self):
        self.lista_prenotazioni = VistaListaPrenotazioniAdmin()
        self.lista_prenotazioni.show()

from PyQt5 import QtCore, Qt
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtGui import QFont, QCursor

from film.model.Film import Film


class VistaNuovoFilm(QWidget):

    def __init__(self, controller_lista_film, aggiorna_lista, parent=None):
        super(VistaNuovoFilm, self).__init__(parent)
        self.controller = controller_lista_film
        self.aggiorna_lista = aggiorna_lista
        self.move(330, 180)
        self.setStyleSheet("background-color: rgb(65, 65, 65);")

        self.v_layout = QVBoxLayout()
        # fonts
        self.font_label1 = QFont("Arial", 15)               # font per i campi
        self.font_label2 = QFont("American Typewriter", 15, 15)     # font grassetto
        self.font_label2.setBold(True)
        self.font_label3 = QFont("American Typewriter", 18, 15, True) # font per il titolo

        # titolo
        self.label_alto = QLabel("NUOVA PROIEZIONE ")
        self.label_alto.setFont(self.font_label3)
        self.label_alto.setAlignment(Qt.AlignCenter)
        self.label_alto.setStyleSheet("color: rgb(255, 255, 255)")
        self.v_layout.addWidget(self.label_alto)

        self.v_layout.addSpacing(20)

        # campi proiezione
        self.campo_nome_film = self.create_format_campo("Nome Film")
        self.campo_attori = self.create_format_campo("Attori")
        self.campo_durata = self.create_format_campo("Durata")
        self.campo_descrizione = self.create_format_campo("Descrizione")


        self.v_layout.addSpacing(30)

        # bottone conferma
        self.bottone_conferma = QPushButton("Conferma")
        self.bottone_conferma.setStyleSheet("font: 200 16pt \"American Typewriter\";" "background-color: rgb(200, 70, 70);" "color: white;")
        self.bottone_conferma.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.bottone_conferma.clicked.connect(self.inserisci_film)
        self.v_layout.addWidget(self.bottone_conferma)

        self.setLayout(self.v_layout)
        self.rect = self.frameGeometry()
        self.setGeometry(self.rect)
        self.setWindowTitle("Nuovo Film")

    # Crea una label con la stringa passata come argomento al di sotto un campo editabile a li aggiunge al layout della finestra
    def create_format_campo(self, testo):
        label = QLabel(testo)
        label.setFont(self.font_label2)
        label.setStyleSheet("color: white;")
        self.v_layout.addWidget(label)

        campo = QLineEdit()
        campo.setStyleSheet("background-color: white;")
        campo.setFont(self.font_label1)
        self.v_layout.addWidget(campo)
        return campo


    # Controlla i dati inseriti e inserisce il nuovo film
    def inserisci_film(self):
        nome_film = self.campo_nome_film.text()
        descrizione = self.campo_descrizione.text()
        durata = self.campo_durata.text()
        attori = self.campo_attori.text()

        # Controlla che siano stati compilati tutti i campi della form
        if self.campo_nome_film.text() == "" or self.campo_attori.text() == "" or self.campo_durata.text() == "" or self.campo_descrizione.text() == "":
            QMessageBox.critical(self, "Errore", "Compila tutti i campi richiesti", QMessageBox.Ok, QMessageBox.Ok)
            return False

        # Controlla che il nome del film inserito non sia già registrato
        elif self.controller.get_film_by_name(self.campo_nome_film.text()) is not None:
            QMessageBox.critical(self, "Errore", "Il film inserito è già presente nel sistema", QMessageBox.Ok, QMessageBox.Ok)
            return False

        self.controller.aggiungi_film(Film(nome_film, descrizione, attori, durata))
        self.controller.save_data()
        QMessageBox.about(self, "Completato!", "Il film è stato inserito con successo")
        self.aggiorna_lista()
        self.close()
        return True


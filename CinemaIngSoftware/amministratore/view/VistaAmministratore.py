from PyQt5 import QtCore
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QFont, QIcon, QPixmap, QCursor
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QMessageBox

from lista_clienti.view.VistaListaClienti import VistaListaClienti
from lista_prenotazioni.views.VistaListaPrenotazioni import VistaListaPrenotazioni
from lista_film.view.VistaListaFilm import VistaListaFilm


class VistaAmministratore(QWidget):

    def __init__(self, nome, parent=None):
        super(VistaAmministratore, self).__init__(parent)
        self.font_bottone = QFont("American Typewriter", 15, 20)
        self.move(400, 200)

        self.v_layout = QVBoxLayout()
        self.setStyleSheet("background-color: rgb(5, 5, 5);")

        self.label_icona = QLabel("Amministratore")
        self.label_icona.setPixmap(QPixmap('images/profilo_utente.png').scaled(QSize(250,250), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.label_icona.setAlignment(Qt.AlignCenter)
        self.v_layout.addWidget(self.label_icona)

        self.label_nome = QLabel(nome)
        self.label_nome.setFont(QFont("American Typewriter", 20))
        self.label_nome.setStyleSheet("color: white;")
        self.label_nome.setAlignment(Qt.AlignCenter)
        self.v_layout.addWidget(self.label_nome)
        self.v_layout.addSpacing(20)

        # Horizontal layout for admin
        self.h_admin_layout = QHBoxLayout()

        self.label_admin = QLabel("Amministratore")
        self.label_admin.setFont(QFont("American Typewriter", 13, 20, True))
        self.label_admin.setStyleSheet("color: white;")

        self.h_admin_layout.addWidget(self.label_admin)

        self.v_layout.addLayout(self.h_admin_layout)
        self.v_layout.addSpacing(20)

        # Horizontal layout for buttons
        self.h_layout = QHBoxLayout()

        self.bottone_prenotazioni = self.create_button(" Lista Prenotazioni", self.go_lista_prenotazioni,
                                                       "background-color:#1e9fdb;")
        self.bottone_clienti = self.create_button(" Lista Clienti", self.go_lista_clienti,
                                                     "background-color:#1e9fdb;")
        self.bottone_film = self.create_button(" Lista Film", self.go_lista_film,
                                                     "background-color:#1e9fdb;")

        self.h_layout.addWidget(self.bottone_prenotazioni)
        self.h_layout.addWidget(self.bottone_clienti)
        self.h_layout.addWidget(self.bottone_film)

        self.v_layout.addLayout(self.h_layout)

        self.setLayout(self.v_layout)
        self.setWindowTitle("Profilo Amministratore")
        self.rect = self.frameGeometry()
        self.setGeometry(self.rect)

    # Crea bottoni ricevendo come parametri il testo, il comando da collegare, il colore di background
    def create_button(self, testo, comando, background_color):
        bottone = QPushButton(testo)
        bottone.setFont(self.font_bottone)
        bottone.setStyleSheet(background_color + " " + "border-radius: 6px;" "padding: 5px;")
        bottone.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        bottone.clicked.connect(comando)
        return bottone

    # Mostra la lista dei clienti
    def go_lista_clienti(self):
        self.vista_lista_clienti = VistaListaClienti()
        self.vista_lista_clienti.show()

    # Mostra la lista delle prenotazioni
    def go_lista_prenotazioni(self):
        self.vista_lista_prenotazioni = VistaListaPrenotazioni()
        self.vista_lista_prenotazioni.show()

    # Mostra la lista dei film
    def go_lista_film(self):
        self.vista_lista_film = VistaListaFilm()
        self.vista_lista_film.show()

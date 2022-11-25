from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QListView, QHBoxLayout, QPushButton, QMessageBox
from PyQt5.QtGui import QFont, QStandardItem, QStandardItemModel, QCursor

from lista_film.controller.ControlloreListaFilm import ControlloreListaFilm
from film.view.VistaNuovoFilm import VistaNuovoFilm


class VistaListaFilm(QWidget):

    def __init__(self, parent=None):
        super(VistaListaFilm, self).__init__(parent)
        self.controller = ControlloreListaFilm()
        self.setStyleSheet("background-color: rgb(65, 65, 65);")

        self.v_layout = QVBoxLayout()

        self.list_view = QListView()
        self.list_view.setStyleSheet("background-color: white;")
        self.aggiorna_dati()
        self.v_layout.addWidget(self.list_view)

        self.h_layout = QHBoxLayout()

        self.create_button("Nuovo", self.go_inserisci_film, "background-color: rgb(28,162,239);")
        self.create_button("Elimina Film", self.elimina_film, "background-color: rgb(184,239,2);")

        self.v_layout.addLayout(self.h_layout)
        self.setLayout(self.v_layout)
        self.resize(300, 500)
        self.move(300, 150)
        self.setWindowTitle("Lista Film")
        self.show()

    def create_button(self, testo, comando, background_color):
        bottone = QPushButton(testo)
        font_button = QFont("American Typewriter", 15)
        font_button.setBold(True)
        bottone.setFont(font_button)
        bottone.setStyleSheet(background_color + " " + " border-radius: 8;")
        bottone.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        bottone.clicked.connect(comando)
        self.h_layout.addWidget(bottone)

    # Funzione di callback che aggiorna i dati della lista dei film visualizzata
    def aggiorna_dati(self):
        self.list_view_model = QStandardItemModel(self.list_view)

        for film in self.controller.get_lista_film():
            item = QStandardItem()
            item.setText(film.nome_film)
            item.setEditable(False)
            item.setFont(QFont("American Typewriter", 16))
            self.list_view_model.appendRow(item)
        self.list_view.setModel(self.list_view_model)

    def go_inserisci_film(self):
        self.vista_inserisci_film = VistaNuovoFilm(self.controller, self.aggiorna_dati)
        self.vista_inserisci_film.show()


    # Chiede conferma di eliminare il film selezionato, in caso affermativo lo cancella
    def elimina_film(self):
        try:
            indice = self.list_view.selectedIndexes()[0].row()
            da_eliminare = self.controller.get_lista_film()[indice]
        except:
            QMessageBox.critical(self, "Errore", "Seleziona il film da eliminare", QMessageBox.Ok, QMessageBox.Ok)
            return
        risposta = QMessageBox.warning(self, "Conferma", "Sei sicuro di volere eliminare la proiezione?", QMessageBox.Yes, QMessageBox.No)
        if risposta == QMessageBox.Yes:
            self.controller.elimina_film_by_name(da_eliminare.nome_film)
            QMessageBox.about(self, "Eliminato", "Il film è stato eliminato")
            self.aggiorna_dati()
        else:
            return

    # Alla chiusura della finestra salva le modifiche apportate alla lista dei film
    def closeEvent(self, event):
        self.controller.save_data()

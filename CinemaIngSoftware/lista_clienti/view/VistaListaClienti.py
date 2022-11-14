from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QListView, QHBoxLayout, QPushButton, QMessageBox
from PyQt5.QtGui import QFont, QStandardItem, QStandardItemModel, QCursor

from lista_clienti.controller.ControlloreListaClienti import ControlloreListaClienti


class VistaListaClienti(QWidget):

    def __init__(self, parent=None):
        super(VistaListaClienti, self).__init__(parent)
        self.controller = ControlloreListaClienti()

        self.v_layout = QVBoxLayout()

        self.list_view = QListView()
        self.aggiorna_dati()
        self.v_layout.addWidget(self.list_view)

        self.h_layout = QHBoxLayout()

        self.create_button("Elimina Cliente", self.elimina_cliente, "background-color: rgb(200, 70, 70);")

        self.v_layout.addLayout(self.h_layout)
        self.setLayout(self.v_layout)
        self.resize(300, 500)
        self.move(300, 200)
        self.setWindowTitle("Lista Clienti")
        self.show()

    def create_button(self, testo, comando, background_color):
        bottone = QPushButton(testo)
        bottone.setFont(QFont("American Typewriter", 16, 20))
        bottone.setStyleSheet(background_color + " " + "border-radius: 8px;" "padding: 5px;" "color: #FFFFFF")
        bottone.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        bottone.clicked.connect(comando)
        self.h_layout.addWidget(bottone)

    # Funzione di callback che aggiorna i dati della lista clienti visualizzata
    def aggiorna_dati(self):
        self.list_view_model = QStandardItemModel(self.list_view)

        for cliente in self.controller.get_lista_clienti():
            item = QStandardItem()
            item.setText(cliente.nome + " " + cliente.cognome)
            item.setEditable(False)
            item.setFont(QFont("Arial", 16))
            self.list_view_model.appendRow(item)
        self.list_view.setModel(self.list_view_model)


    # Chiede conferma di eliminare il cliente selezionato, in caso affermativo lo cancella
    def elimina_cliente(self):
        try:
            indice = self.list_view.selectedIndexes()[0].row()
            da_eliminare = self.controller.get_lista_clienti()[indice]
        except:
            QMessageBox.critical(self, "Errore", "Seleziona il profilo cliente da eliminare", QMessageBox.Ok, QMessageBox.Ok)
            return
        risposta = QMessageBox.warning(self, "Conferma", "Sei sicuro di volere eliminare il cliente?", QMessageBox.Yes, QMessageBox.No)
        if risposta == QMessageBox.Yes:
            self.controller.elimina_cliente_by_user(da_eliminare.username)
            QMessageBox.about(self, "Eliminato", "Il cliente è stato eliminato")
            self.aggiorna_dati()
        else:
            return

    # Alla chiusura della finestra salva le modifiche apportate alla lista dei dipendenti
    def closeEvent(self, event):
        self.controller.save_data()

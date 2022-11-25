from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QLabel, QMessageBox, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QFont, QPixmap, QCursor
from PyQt5.QtCore import QSize, Qt

from lista_clienti.controller.ControlloreListaClienti import ControlloreListaClienti
from cliente.view.VistaModificaCliente import VistaModificaCliente
from lista_prenotazioni.views.VistaListaPrenotazioniCliente import VistaListaPrenotazioniCliente


class VistaCliente(QWidget):
# Il cliente è stato passato dal login al controllore, e il controllore è stato passato poi a questa vista
    def __init__(self, controllore_cliente, parent=None):
        super(VistaCliente, self).__init__(parent)
        self.move(400, 200)
        self.controllore_cliente = controllore_cliente

        self.v_layout = QVBoxLayout()

        # icona profilo cliente
        self.label_icona = QLabel("Cliente")
        self.label_icona.setAlignment(Qt.AlignCenter)
        self.pixmap = QPixmap('images/profilo_utente.png').scaled(QSize(250,250), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.label_icona.setPixmap(self.pixmap)

        self.v_layout.addWidget(self.label_icona)

        # label nome cliente
        self.label_nome = QLabel(self.controllore_cliente.get_nome_cliente() + " " + self.controllore_cliente.get_cognome_cliente())
        self.label_nome.setFont(QFont("American Typewriter", 30, 150))
        self.label_nome.setAlignment(Qt.AlignCenter)

        self.v_layout.addWidget(self.label_nome)
        self.v_layout.addSpacing(40)

        # labels contenenti dati del cliente
        self.create_label("Username:         ", self.controllore_cliente.get_username_cliente())
        self.create_label("Indirizzo:        ", self.controllore_cliente.get_indirizzo_cliente())
        self.create_label("Telefono:         ", self.controllore_cliente.get_telefono_cliente())

        self.v_layout.addSpacing(25)
        self.h_layout = QHBoxLayout()

        # bottoni profilo cliente collegati alle relative funzioni
        self.create_button("Prenotazioni", self.go_lista_prenotazioni)
        self.create_button("Elimina profilo", self.conferma_elimina_profilo)
        self.create_button("Modifica profilo", self.go_modifica_profilo)

        self.v_layout.addLayout(self.h_layout)

        self.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.setLayout(self.v_layout)
        self.setWindowTitle("Profilo Cliente")
        self.rect = self.frameGeometry()
        self.setGeometry(self.rect)


    def create_label(self, text, text_label):
        h_layout = QHBoxLayout()
        # Label sx con parametro text
        label = QLabel(text)
        label.setStyleSheet("color: rgb(255, 255, 255);\n""font: 200 18pt \"American Typewriter\";\n"
                            "background-color: rgb(200, 70, 70);" "border-radius: 5px;" "margin-right: 30px;")
        h_layout.addWidget(label)
        # Label dx con parametro text_label
        label_di_testo = QLabel(text_label)
        label_di_testo.setFont(QFont("Arial", 18))
        h_layout.addWidget(label_di_testo)
        # al v_layout della schermata aggiunge questo nuovo h_layout appena creato
        self.v_layout.addLayout(h_layout)

    # Crea un bottone e lo aggiunge al layout orizzontale dei bottoni
    # Riceve come argomenti il testo da mettere nei bottoni e la funzione da collegare
    def create_button(self, testo, comando):
        bottone = QPushButton(testo)
        bottone.setFont(QFont("American Typewriter", 15, 5))
        bottone.setStyleSheet("background-color:#1e9fdb;" "border-radius: 3px;" "padding: 5px")
        bottone.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        bottone.clicked.connect(comando)
        self.h_layout.addWidget(bottone)

    # Nelle prossime funzioni ci starà anche il controllore lista clienti che serve per salvare o aggiornare i dati

    # Visualizza la lista delle prenotazioni
    def go_lista_prenotazioni(self):
        self.vista_prenotazioni_cliente = VistaListaPrenotazioniCliente(self.controllore_cliente.get_username_cliente())
        self.vista_prenotazioni_cliente.show()



    # Chiede conferma per l'eliminazione del profilo e in caso affermativo lo cancella
    def conferma_elimina_profilo(self):
        self.controllore_lista_clienti = ControlloreListaClienti()
        risposta = QMessageBox.warning(self, "Elimina Profilo", "Sei sicuro di voler elimare il tuo profilo?\nL'azione è irreversibile", QMessageBox.Yes, QMessageBox.No)
        if risposta == QMessageBox.Yes:
            self.close()
            self.controllore_lista_clienti.elimina_cliente_by_user(self.controllore_cliente.get_username_cliente())
            self.controllore_lista_clienti.save_data()
        else:
            pass

    # Funzione che chiama la funzione per mostrare la modifica del profilo che poi ritorna l'aggiornamento di VistaCliente
    def go_modifica_profilo(self):
        self.vista_modifica_profilo = VistaModificaCliente(self.controllore_cliente)
        risposta = QMessageBox.warning(self, "Warning", "Accedere alla mdofica profilo?\nDovrai effettuare nuovamente il login", QMessageBox.Yes, QMessageBox.No)
        if risposta == QMessageBox.Yes:
            self.vista_modifica_profilo.show()
            self.close()
        else:
            return

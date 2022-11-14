from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QHBoxLayout, QPushButton, QMessageBox
from PyQt5.QtGui import QFont

from cliente.controller.ControlloreCliente import ControlloreCliente
from lista_clienti.controller.ControlloreListaClienti import ControlloreListaClienti


class VistaModificaCliente(QWidget):

    def __init__(self, controllore_cliente, parent=None):
        super(VistaModificaCliente, self).__init__(parent)
        self.controllore_cliente = controllore_cliente
        self.controllore_lista = ControlloreListaClienti()
        # prende il dato Cliente dalla lista
        self.cliente = self.controllore_lista.get_cliente_by_user(self.controllore_cliente.get_username_cliente())
        self.index = self.controllore_lista.get_lista_clienti().index(self.cliente) # prende l'indice del cliente nella lista
        # Prende lo username del cliente
        self.username = controllore_cliente.get_username_cliente()


        self.v_layout = QVBoxLayout()

        self.font_label = QFont("American Typewriter", 16)
        self.font_label.setBold(True)
        self.font_campi = QFont("Arial", 16)

        self.campo_username = self.create_format_campo("Username:", self.username)
        self.campo_nome = self.create_format_campo("Nome:", self.controllore_cliente.get_nome_cliente())
        self.campo_cognome = self.create_format_campo("Cognome:", self.controllore_cliente.get_cognome_cliente())
        self.campo_indirizzo = self.create_format_campo("Indirizzo:", self.controllore_cliente.get_indirizzo_cliente())
        self.campo_telefono = self.create_format_campo("Telefono:", str(self.controllore_cliente.get_telefono_cliente()))
        self.campo_password = self.create_format_campo("Password:", str(self.controllore_cliente.get_password_cliente()))

        self.h_layout = QHBoxLayout()

        self.create_button("Conferma Modifica", self.conferma_modifica_cliente, "background-color: rgb(75,200,75);")
        self.create_button("Chiudi", self.annulla, "background-color: rgb(255,20,20);")

        self.v_layout.addLayout(self.h_layout)
        self.setLayout(self.v_layout)
        self.setWindowTitle("Cliente")
        self.resize(450, 400)

    def conferma_modifica_cliente (self):
        if self.campo_username.text() == "" or self.campo_nome.text() == "" or self.campo_cognome.text() == "" or self.campo_indirizzo.text() == "" or self.campo_telefono.text() == "" or self.campo_password.text() == "":
            QMessageBox.critical(self, "Errore", "Compila tutti i campi", QMessageBox.Ok, QMessageBox.Ok)
            return
        else:
            risposta = QMessageBox.warning(self, "Warning", "Confermare le modifiche?", QMessageBox.Yes, QMessageBox.No)
            if risposta == QMessageBox.Yes:
                self.controllore_lista.get_lista_clienti()[self.index].username = self.campo_username.text()
                self.controllore_lista.get_lista_clienti()[self.index].password = self.campo_password.text()
                self.controllore_lista.get_lista_clienti()[self.index].nome = self.campo_nome.text()
                self.controllore_lista.get_lista_clienti()[self.index].cognome = self.campo_cognome.text()
                self.controllore_lista.get_lista_clienti()[self.index].indirizzo = self.campo_indirizzo.text()
                self.controllore_lista.get_lista_clienti()[self.index].telefono = self.campo_telefono.text()
                self.controllore_lista.save_data()
                self.close()
            else:
                return

    # Crea una label con la prima stringa passata la aggiunge al layout verticale della finestra, al di sotto aggiunge un
    # campo editabile con al suo interno la stringa passata come secondo argomento
    def create_format_campo(self, testo, get_campo):
        label = QLabel(testo)
        label.setStyleSheet("background-color: rgb(200, 70, 70);" "color: #FFFFFF;" "border-radius: 8px;" "margin: 10px;")
        label.setFont(self.font_label)
        self.v_layout.addWidget(label)

        campo = QLineEdit()
        campo.setFont(QFont("Arial", 16))
        campo.setText(get_campo)
        self.v_layout.addWidget(campo)
        self.v_layout.addSpacing(10)
        return campo

    # Crea un bottone con il testo, la funzione e il colore di abckground passati e lo aggiunge al layout dei bottoni
    def create_button(self, testo, comando, background_color):
        bottone = QPushButton(testo)
        bottone.setFont(QFont("Arial", 15, 10))
        bottone.setStyleSheet(background_color + " " + "color: #FFFFFF;"  "margin-top: 10px;")
        bottone.clicked.connect(comando)
        self.h_layout.addWidget(bottone)

    def annulla(self):
        self.close()


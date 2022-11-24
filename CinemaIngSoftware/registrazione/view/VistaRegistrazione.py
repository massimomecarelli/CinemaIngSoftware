from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtGui import QFont
from datetime import datetime
from qtwidgets import PasswordEdit

from cliente.model.Cliente import Cliente
from lista_clienti.controller.ControlloreListaClienti import ControlloreListaClienti


class VistaRegistrazione(QWidget):

    def __init__(self, parent=None):
        super(VistaRegistrazione, self).__init__(parent)
        self.controller = ControlloreListaClienti()

        self.move(400, 200)
        self.v_layout = QVBoxLayout()
        # fonts
        self.font_label1 = QFont("American Typewriter", 17)               # font per i campi del cliente
        self.font_label2 = QFont("American Typewriter", 15, 15, True)     # font grassetto per le password
        self.font_label2.setBold(True)
        self.font_label3 = QFont("American Typewriter", 17, 15, True)     # font per il titolo del form
        self.font_label_campo = QFont("Arial", 16)

        # titolo
        self.label_alto = QLabel("Compila il form di registrazione: ")
        self.label_alto.setFont(self.font_label3)
        self.label_alto.setStyleSheet("color: rgb(200, 70, 70)")
        self.v_layout.addWidget(self.label_alto)

        self.v_layout.addSpacing(20)

        # campi registrazione
        self.campo_nome = self.create_format_campo("Nome")
        self.campo_cognome = self.create_format_campo("Cognome")
        self.campo_indirizzo = self.create_format_campo("Indirizzo")
        self.campo_telefono = self.create_format_campo("Telefono")

        self.campo_user = self.create_format_campo("Username")
        self.campo_password = self.create_format_password("Password")
        self.campo_conferma_password = self.create_format_password("Conferma password")

        self.v_layout.addSpacing(30)

        # bottone conferma
        self.bottone_conferma = QPushButton("Conferma")
        self.bottone_conferma.setFont(self.font_label1)
        self.bottone_conferma.setStyleSheet("background-color: rgb(200, 70, 70);" "border-radius: 5px;" "color: white;" "padding: 4px;")
        self.bottone_conferma.clicked.connect(self.registra_cliente)
        self.v_layout.addWidget(self.bottone_conferma)

        self.setLayout(self.v_layout)
        self.rect = self.frameGeometry()
        self.setGeometry(self.rect)
        self.setWindowTitle("Registrazione")

    #Crea una label con la stringa passata come argomento al di sotto un campo editabile a li aggiunge al layout della finestra
    def create_format_campo(self, testo):
        label = QLabel(testo)
        label.setFont(self.font_label1)
        self.v_layout.addWidget(label)

        campo = QLineEdit()
        campo.setFont(self.font_label_campo)
        self.v_layout.addWidget(campo)
        return campo

    #Crea una label e al di sotto un campo con la possibilità di oscurare l'inserimento e li aggiunge al layout
    def create_format_password(self, testo):
        label = QLabel(testo)
        label.setFont(self.font_label2)
        self.v_layout.addWidget(label)

        campo = PasswordEdit()
        campo.setFont(self.font_label_campo)
        campo.setEchoMode(QLineEdit.Password)
        self.v_layout.addWidget(campo)
        return campo

    #Controlla i dati inseriti e registra il profilo nel sistema
    def registra_cliente(self):

        #Controlla che siano stati compilati tutti i campi della form
        if self.campo_nome.text() == "" or self.campo_cognome.text() == "" or self.campo_indirizzo.text() == "" or self.campo_telefono.text() == "" or self.campo_user.text() == "" or self.campo_password.text() == "" or self.campo_conferma_password.text() == "":
            QMessageBox.critical(self, "Errore", "Compila tutti i campi richiesti", QMessageBox.Ok, QMessageBox.Ok)

        #Controlla che l'username inserito non sia già in uso su un altro account
        elif self.controller.get_cliente_by_user(self.campo_user.text()) is not None:
            QMessageBox.critical(self, "Errore", "Il nome utente inserito non è disponibile", QMessageBox.Ok, QMessageBox.Ok)

        #Controlla che le password inserite corrispondano
        elif self.campo_password.text() != self.campo_conferma_password.text():
            QMessageBox.critical(self, "Errore", "Le password inserite non corrispondono, si prega di riprovare",
                                 QMessageBox.Ok, QMessageBox.Ok)
        else:
            nome = self.campo_nome.text()
            cognome = self.campo_cognome.text()
            indirizzo = self.campo_indirizzo.text()
            telefono = self.campo_telefono.text()
            username = self.campo_user.text()
            password = self.campo_password.text()

            try:
                nuovo_cliente = Cliente(nome, cognome, indirizzo, telefono, username, password)
                QMessageBox.about(self, "Completata", "La registrazione è avvenuta correttamente")
                self.controller.aggiungi_cliente(nuovo_cliente)
                self.close()
            except:
                QMessageBox.critical(self, "Errore", "La registrazione non è andata a buon fine", QMessageBox.Ok, QMessageBox.Ok)

    def closeEvent(self, event):
        self.controller.save_data()


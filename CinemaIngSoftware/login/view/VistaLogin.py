from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QPushButton, QMessageBox, QVBoxLayout, QLabel, QLineEdit, QShortcut
from PyQt5.QtGui import QKeySequence, QFont, QCursor, QIcon
from qtwidgets import PasswordEdit
import os
import json

from amministratore.view.VistaAmministratore import VistaAmministratore
from cliente.controller.ControlloreCliente import ControlloreCliente
from cliente.view.VistaCliente import VistaCliente
from lista_clienti.controller.ControlloreListaClienti import ControlloreListaClienti


class VistaLogin(QWidget):

    def __init__(self, parent=None):
        super(VistaLogin, self).__init__(parent)

        self.controllore = ControlloreListaClienti()

        self.font = QFont("American Typewriter", 15)

        self.v_layout = QVBoxLayout()


        # campo username
        self.label_username = QLabel("Username")
        self.label_username.setFont(self.font)
        self.v_layout.addWidget(self.label_username)

        self.campo_username = QLineEdit()
        self.campo_username.setFont(self.font)
        self.v_layout.addWidget(self.campo_username)

        # campo password
        self.label_password = QLabel("Password")
        self.label_password.setFont(self.font)
        self.v_layout.addWidget(self.label_password)

        self.campo_password = PasswordEdit()
        self.campo_password.setFont(self.font)
        self.campo_password.setEchoMode(QLineEdit.Password)
        self.v_layout.addWidget(self.campo_password)

        self.v_layout.addSpacing(30)

        # bottone login
        self.bottone_login = QPushButton("Login")
        self.bottone_login.setFont(self.font)
        self.bottone_login.setIcon(QIcon())
        self.bottone_login.setStyleSheet("background-color: rgb(200, 70, 70);" "padding-top: 3px;" "padding-bottom: 3px;" "border-radius: 8px;" "margin-left: 40px;" "margin-right: 40px;")
        self.bottone_login.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.bottone_login.clicked.connect(self.login)
        self.shortcut_open = QShortcut(QKeySequence('Return'), self)
        self.shortcut_open.activated.connect(self.login)
        self.v_layout.addWidget(self.bottone_login)

        self.setLayout(self.v_layout)
        self.resize(300, 230)
        self.setWindowTitle("Login")

    # Controlla le credenziali inserite dall'utente
    def login(self):
        username = self.campo_username.text()
        password = self.campo_password.text()

        # Controlla se le credenziali inserite sono quelle di un amministratore
        if self.controlla_admin(username, password):
            return

        # Controlla che le credenziali inserite corrispondano a quelle di un cliente
        if self.controllore.get_cliente_by_user(username) is not None:
            show_user = self.controllore.get_cliente_by_user(username)

            # In caso affermativo visualizza il profilo del cliente
            if show_user.password == password:
                self.vista_cliente = VistaCliente(ControlloreCliente(show_user))
                self.vista_cliente.show()
                self.close()
            # Altrimenti mostra un messaggio di errore
            else:
                QMessageBox.critical(self, "Errore", "La password è errata", QMessageBox.Ok,
                                     QMessageBox.Ok)
        else:
            QMessageBox.critical(self, "Errore", "Il nome utente inserito non esiste", QMessageBox.Ok,
                                 QMessageBox.Ok)

    # Controlla che l'email e la password inseriti coincidano con le credenziali di una admin, in caso affermativo
    # ritorna True e visualizza il profilo dell'amministratore, altrimenti ritorna False
    def controlla_admin(self, username, password):

        if os.path.isfile("amministratore/data/lista_admin.json"):
            with open("amministratore/data/lista_admin.json") as file:
                lista_admin = json.load(file)
                for admin in lista_admin:
                    if username == admin["username"] and password == admin["password"]:
                        self.vista_admin = VistaAmministratore(admin["nome"])
                        self.vista_admin.show()
                        self.close()
                        return True
        return False

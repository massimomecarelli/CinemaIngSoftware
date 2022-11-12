from PyQt5 import QtCore
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon, QFont, QPixmap, QCursor
from PyQt5.QtWidgets import QWidget, QTabWidget, QVBoxLayout, QLabel, QHBoxLayout, QPushButton, QGridLayout, \
    QListWidget, QListWidgetItem, QDialog, QTableWidget, QTableWidgetItem, QHeaderView, QCheckBox, QAbstractItemView

from lista_film.controller.ControlloreListaFilm import ControlloreListaFilm
from lista_film.model.ListaFilm import ListaFilm
from login.view.VistaLogin import VistaLogin
from registrazione.view.VistaRegistrazione import VistaRegistrazione


class HomeWidget(QWidget):

    def __init__(self):
        super(QWidget, self).__init__()
        self.font = QFont("American Typewriter", 17)
        self.layout = QVBoxLayout()

        # Horizontal layout for buttons and labels
        self.h_button_layout = QHBoxLayout()

        # Crea il bottone info
        self.bottone_info = self.create_button("", "", "", "Info", self.visualizza_info)
        self.bottone_info.setStyleSheet("color: 'black';" "border-radius: 10;")
        self.bottone_info.setIcon(QIcon("images/icon_info.png"))
        self.bottone_info.setIconSize(QSize(120, 50))

        # Crea i bottoni login e registrati
        self.bottone_login = self.create_button("Login", "rgb(255,255,255)", "rgb(0, 0, 0)",
                                                "login", self.go_vista_login)
        self.bottone_registrati = self.create_button("", "", "",
                                                "registrati", self.go_vista_registrazione)
        self.bottone_info.setStyleSheet("color: 'black';" "border-radius: 8;")
        self.bottone_registrati.setIcon(QIcon("images/register2.png"))
        self.bottone_registrati.setIconSize(QSize(140, 70))

        # add buttons to the horizontal layout on the top
        self.h_button_layout.addStretch(1)
        self.h_button_layout.addWidget(self.bottone_info)
        self.h_button_layout.addWidget(self.bottone_login)
        self.h_button_layout.addWidget(self.bottone_registrati)

        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab1.setStyleSheet("background-color: #000000;")
        self.tab2 = QWidget()
        self.tab2.setStyleSheet("background-color: #000000;")
        self.tab3 = QWidget()
        self.tab3.setStyleSheet("background: url(images/contacts.jpeg);")

        # Add tabs
        self.tabs.addTab(self.tab1, QIcon("images/icon_home.png"), "Home")
        self.tabs.addTab(self.tab2, QIcon("images/icon_film.png"), "Film")
        self.tabs.addTab(self.tab3, QIcon("images/icon_contatti.png"), "Contatti")
        self.tabs.setIconSize(QSize(45, 45))

        self.tabs.setFont((QFont("American Typewriter", 17)))
        self.tabs.setStyleSheet("QTabBar::tab { height: 70px; width: 200px; }")

        # Create first tab HOME
        self.tab1.layout = QHBoxLayout(self)
        self.v_layout = QVBoxLayout()
        self.h_title_layout = QHBoxLayout()

        # widgets

        self.label_logo = QLabel()
        self.label_logo.setPixmap(QPixmap("images/icon_cinema.png").scaled(300, 300))
        self.label_logo.setContentsMargins(0, 50, 0, 0)


        # add widgets to horizontal title layout
        self.h_title_layout.setAlignment(Qt.AlignCenter)
        self.h_title_layout.addWidget(self.label_logo)


        self.label_descrizione = QLabel("Benvenuto nel portale del nostro cinema multisala\n   "
                                        "Offriamo programmazioni differenti in ben 4 sale di proiezione,\n "
                                        "registrati per avere la possibilità di prenotare i biglietti comodamente da casa tua!")
        self.label_descrizione.setWordWrap(True)
        self.label_descrizione.setMargin(15)
        self.label_descrizione.setMinimumWidth(400)
        self.label_descrizione.setStyleSheet("font: 16pt \"Papyrus\";" "color: #FFFFFF")
        self.label_descrizione.setAlignment(Qt.AlignCenter)

        # add horizontal_title_layout and label_descrizione to v_layout (vertical layout)
        self.v_layout.addLayout(self.h_title_layout)
        self.v_layout.addWidget(self.label_descrizione)

        self.label_image = self.create_label_image('images/sala2.jpg')
        self.label_image.setMargin(5)
        self.label_image.setFixedSize(1000, 650)

        # add v_layout and label_image to tab1
        self.tab1.layout.addLayout(self.v_layout)
        self.tab1.layout.addWidget(self.label_image)

        self.tab1.setLayout(self.tab1.layout)



        # Create second tab FILM
        self.tab2.layout = QVBoxLayout(self)
        self.v2_layout = QVBoxLayout()

        # list to insert into tab2
        list2 = QListWidget()
        list2.setStyleSheet("border: none;" "color: #FFFFFF;" "padding-left: 50px;" "padding-right: 50px;")
        self.bacheca(list2)
        self.v2_layout.addWidget(list2)

        self.tab2.layout.addLayout(self.v2_layout)
        self.tab2.setLayout(self.tab2.layout)

        self.tab2.setLayout(self.tab2.layout)


        # Create third tab CONTATTI
        self.tab3.layout = QVBoxLayout(self)

        self.v3_layout = QVBoxLayout()

        # horizontal layout che contiene le schede dei contatti

        list1 = QListWidget()
        list1.setAlternatingRowColors(True)
        list1.setStyleSheet("background-color: #FFFFFF;" "border: none;" "padding-left: 150px;" "padding-right: 150px;")
        self.aggiungi_item(list1, "")
        self.aggiungi_item(list1, "Massimo Mecarelli")
        self.aggiungi_item(list1, "")
        self.aggiungi_item(list1, "email - s1093260@studenti.univpm.it")

        self.v3_layout.addWidget(list1)

        self.tab3.layout.addLayout(self.v3_layout)
        self.tab3.setLayout(self.tab3.layout)

        # Final layout
        self.layout.addLayout(self.h_button_layout)
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    # Crea un bottone con i parametri passati
    def create_button(self, testo, text_color, background_color, nome, comando):
        bottone = QPushButton(testo)
        bottone.setStyleSheet("background-color: " + background_color + ";\n""font: 100 19pt \"American Typewriter\";\n"
                              "color: " + text_color + ";""border-radius: 15px;")
        bottone.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        bottone.setDefault(True)
        bottone.setObjectName(nome)
        bottone.clicked.connect(comando)
        return bottone

    # Crea delle label con immagini da inserire nei layout, come argomento deve essere passata la path dell'immagine come stringa
    def create_label_image(self, immagine):
        label = QLabel()
        label.setText("")
        label.setPixmap(QPixmap(immagine))
        label.setScaledContents(True)
        label.setObjectName("label")
        return label

    # Visualizza form registrazione
    def go_vista_registrazione(self):
        self.vista_registrazione = VistaRegistrazione()
        self.vista_registrazione.show()

    # Visualizza finestra login
    def go_vista_login(self):
        self.vista_login = VistaLogin()
        self.vista_login.show()

    # Visualizza la mappa
    def visualizza_info(self):
        dialog = QDialog()
        dialog.setWindowTitle("Dove siamo")

        v_layout = QVBoxLayout()
        label = QLabel()
        label.setPixmap(QPixmap("images/posizione.png"))

        v_layout.addWidget(label)

        dialog.setLayout(v_layout)
        dialog.exec()

    # Aggiunge alla lista in item con il nome passato
    def aggiungi_item(self, lista, nome):
        item = QListWidgetItem(nome)
        item.setTextAlignment(Qt.AlignCenter)
        font = QFont("American Typewriter", 16)
        font.setWeight(50)
        item.setFont(font)
        lista.addItem(item)

    def bacheca(self, lista):
        lista_film = ControlloreListaFilm().get_lista_film()
        for film in lista_film:
            item = QListWidgetItem(film.get_nome_film())
            item.setTextAlignment(Qt.AlignCenter)
            font = QFont("American Typewriter", 40)
            font.setWeight(100)
            item.setFont(font)
            lista.addItem(item)
            item = QListWidgetItem("ATTORI PROTAGONISTI:  " + film.get_attori())
            item.setTextAlignment(Qt.AlignCenter)
            font = QFont("Arial", 15)
            font.setWeight(40)
            font.setItalic(True)
            item.setFont(font)
            lista.addItem(item)
            item = QListWidgetItem("Durata:   " + film.get_durata() + "'")
            font = QFont("Papyrus", 19)
            font.setWeight(100)
            item.setFont(font)
            lista.addItem(item)
            item = QListWidgetItem(film.get_descrizione())
            font = QFont("American Typewriter", 15)
            font.setWeight(25)
            item.setFont(font)
            lista.addItem(item)

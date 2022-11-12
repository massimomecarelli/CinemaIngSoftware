from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QListView, QHBoxLayout
from PyQt5.QtGui import QFont, QStandardItemModel, QStandardItem


class VistaPrenotazione(QWidget):

    def __init__(self, controllore_prenotazione, parent=None):
        super(VistaPrenotazione, self).__init__(parent)
        self.controllore_prenotazione = controllore_prenotazione
        self.font_label = QFont("American Typewriter", 14, 40)

        self.v_layout = QVBoxLayout()

        # labels
        self.create_label("Username: ", self.controllore_prenotazione.get_username_prenotazione())
        self.create_label("Data: ", self.controllore_prenotazione.get_data_prenotazione().strftime('%d/%m/%Y'))
        self.create_label("Numero di biglietti: ", str(self.controllore_prenotazione.get_numero_biglietti()))
        self.create_label("Orario Spettacolo: ", self.controllore_prenotazione.get_numero_spettacolo())

        self.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.setLayout(self.v_layout)
        self.setWindowTitle("Dettagli Prenotazione")
        self.resize(450, 400)

    #Crea una coppia di label con le stringhe passate e le aggiunge al layout della finestra
    def create_label(self, testo, text_label):
        h_layout = QHBoxLayout()
    # crea prima label a sinistra con l'identificatore dei parametri
        label = QLabel(testo)
        label.setStyleSheet("color: rgb(255, 255, 255);\n""font: 300 18pt \"American Typewriter\";\n"
                            "background-color: rgb(200, 70, 70);""padding: 11px;""border-radius: 20;")
        h_layout.addWidget(label)
    # crea seconda label con i dettagli specifici della prenotazione
        label_di_testo = QLabel(text_label)
        label_di_testo.setFont(self.font_label)
        label_di_testo.setStyleSheet("padding-left: 12px")
        h_layout.addWidget(label_di_testo)

        self.v_layout.addLayout(h_layout)
        self.v_layout.addSpacing(20)

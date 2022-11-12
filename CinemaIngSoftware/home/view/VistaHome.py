from PyQt5.QtWidgets import QMainWindow, QDesktopWidget
from PyQt5.QtCore import Qt

from home.view.HomeWidget import HomeWidget


class VistaHome(QMainWindow):

    def __init__(self, parent=None):
        super(VistaHome, self).__init__(parent)
        self.setObjectName("HOME")
        self.setWindowTitle("CINEMA")
        self.setWindowState(Qt.WindowMaximized)
        self.move(50, 0)
        self.setStyleSheet("background-color: #000000;")

        #Crea il widget centrale della finestra e glielo assegna
        self.table_widget = HomeWidget()
        self.setCentralWidget(self.table_widget)

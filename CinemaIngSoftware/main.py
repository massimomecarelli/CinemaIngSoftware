import sys
from PyQt5.QtWidgets import QApplication
from home.view.VistaHome import VistaHome

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VistaHome()
    window.show()
    app.exec_()

# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from Nucleo.GUI.WindowAbout_ui import Ui_MainWindow
class WindowAbout (QMainWindow):

    def __init__(self, parent = None):

        
        super(WindowAbout, self).__init__(parent)
        self.uiAbout = Ui_MainWindow()
        self.uiAbout.setupUi(self)
        self.centerWindow()

        """
    Nombre: centerWindow
    Parametros: No recibe parametros
    Descripcion: Inicializa la ventana al centro de la pantalla.
    Retorno: Retorna True
    """
    def centerWindow(self):
        screen = self.frameGeometry()
        ubication = QtWidgets.QDesktopWidget().availableGeometry().center()
        screen.moveCenter(ubication)
        self.move(screen.topLeft())
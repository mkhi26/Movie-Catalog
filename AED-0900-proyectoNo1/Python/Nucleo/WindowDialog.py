# -*- coding: utf-8 -*-
"""
    Esta es la clase que gestiona la GUI del QDialog
"""
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from Nucleo.GUI.WindowDialog_ui import Ui_Dialog
class DialogConfirm(QDialog):

    def __init__(self, parent = None):

        
        super(DialogConfirm, self).__init__(parent)
        self.uiDialog = Ui_Dialog()
        self.uiDialog.setupUi(self)
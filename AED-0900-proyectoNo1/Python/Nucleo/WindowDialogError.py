# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from Nucleo.GUI.WindowDialogError_ui import Ui_Dialog
class DialogError(QDialog):

    def __init__(self, parent = None):

        
        super(DialogError, self).__init__(parent)
        self.uiDialogError = Ui_Dialog()
        self.uiDialogError.setupUi(self)
# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QEvent
from PyQt5.QtGui import QInputEvent, QMouseEvent
from Nucleo.GUI.WindowTreeTime_ui import Ui_MainWindow




class WindowTreeTime (QMainWindow):

    def __init__(self, parent = None):

        
        super(WindowTreeTime, self).__init__(parent)
        self.uiWindowTreeTime = Ui_MainWindow()
        self.uiWindowTreeTime.setupUi(self)
        self.centerWindowTree()

    def centerWindowTree(self):
        self.move(0,0)
        return True

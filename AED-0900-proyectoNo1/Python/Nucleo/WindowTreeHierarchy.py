# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QEvent
from PyQt5.QtGui import QInputEvent, QMouseEvent
from Nucleo.GUI.WindowTreeHierarchy_ui import Ui_MainWindow


class WindowTreeHierarchy (QMainWindow):

    def __init__(self, parent = None):

        
        super(WindowTreeHierarchy, self).__init__(parent)
        self.uiTreeHierarchy = Ui_MainWindow()
        self.uiTreeHierarchy.setupUi(self)
        self.centerWindowTree()
    def centerWindowTree(self):
        self.move(695,0)
        return True
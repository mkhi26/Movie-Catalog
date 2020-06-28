# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GuiTreeHierarchy.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(695, 410)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.txtViewTree = QtWidgets.QTextEdit(self.centralwidget)
        self.txtViewTree.setGeometry(QtCore.QRect(0, -10, 692, 400))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.txtViewTree.setFont(font)
        self.txtViewTree.setMouseTracking(True)
        self.txtViewTree.setTabletTracking(False)
        self.txtViewTree.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.txtViewTree.setAutoFillBackground(False)
        self.txtViewTree.setStyleSheet("background-color: rgb(218, 214, 205);\n"
"font: 25 10pt \"Ubuntu\";")
        self.txtViewTree.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.txtViewTree.setObjectName("txtViewTree")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Árbol Jerárquico de categorías"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

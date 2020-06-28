# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GuiTreeTime.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(695, 410)
        MainWindow.setStyleSheet("background-color: rgb(218, 214, 205);")
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Árbol binario de duración"))
        self.txtViewTree.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><img src=\":/cct/test.png\"/></p></body></html>"))
        self.txtViewTree.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:10pt; font-weight:24; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/cct/test.png\" /></p></body></html>"))
#import GraphicResources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GuiViewEdit.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ViewEdit_Window(object):
    def setupUi(self, ViewEdit_Window):
        ViewEdit_Window.setObjectName("ViewEdit_Window")
        ViewEdit_Window.resize(681, 415)
        ViewEdit_Window.setStyleSheet("background-color: rgb(218, 214, 205);")
        self.centralwidget = QtWidgets.QWidget(ViewEdit_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.txtTable = QtWidgets.QTextEdit(self.centralwidget)
        self.txtTable.setGeometry(QtCore.QRect(10, 20, 651, 261))
        self.txtTable.setMaximumSize(QtCore.QSize(651, 261))
        font = QtGui.QFont()
        font.setFamily("Abyssinica SIL")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.txtTable.setFont(font)
        self.txtTable.setMouseTracking(True)
        self.txtTable.setTabletTracking(False)
        self.txtTable.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.txtTable.setAutoFillBackground(False)
        self.txtTable.setStyleSheet("background-color: rgb(244, 255, 231);\n"
"font: 12pt \"Abyssinica SIL\";")
        self.txtTable.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.txtTable.setObjectName("txtTable")
        self.txtId = QtWidgets.QLineEdit(self.centralwidget)
        self.txtId.setGeometry(QtCore.QRect(220, 290, 151, 31))
        self.txtId.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtId.setObjectName("txtId")
        self.btnEdit = QtWidgets.QPushButton(self.centralwidget)
        self.btnEdit.setGeometry(QtCore.QRect(60, 340, 131, 41))
        self.btnEdit.setStyleSheet("QPushButton {\n"
"\n"
"    \n"
"    background-color: rgb(255, 170, 0);\n"
"    color: rgb(0, 0, 0);\n"
"    \n"
"    \n"
"    font: 57 italic 14pt \"URW Chancery L\";\n"
"    \n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    \n"
"    background-color: rgb(0, 85, 255);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    \n"
"    background-color: rgb(255, 255, 0);\n"
"    }")
        self.btnEdit.setObjectName("btnEdit")
        self.btnDelete = QtWidgets.QPushButton(self.centralwidget)
        self.btnDelete.setGeometry(QtCore.QRect(410, 340, 131, 41))
        self.btnDelete.setStyleSheet("QPushButton {\n"
"\n"
"    \n"
"    background-color: rgb(255, 170, 0);\n"
"    color: rgb(0, 0, 0);\n"
"    font: 57 italic 14pt \"URW Chancery L\";\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    \n"
"    background-color: rgb(0, 85, 255);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    \n"
"    background-color: rgb(255, 255, 0);\n"
"    }")
        self.btnDelete.setObjectName("btnDelete")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 340, 71, 41))
        self.label.setStyleSheet("image: url(:/cct/btnEditar.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(340, 340, 71, 41))
        self.label_2.setStyleSheet("image: url(:/cct/btnEliminar.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(160, 290, 61, 31))
        self.label_3.setStyleSheet("image: url(:/cct/id.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label.raise_()
        self.txtTable.raise_()
        self.txtId.raise_()
        self.btnEdit.raise_()
        self.btnDelete.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        ViewEdit_Window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ViewEdit_Window)
        self.statusbar.setObjectName("statusbar")
        ViewEdit_Window.setStatusBar(self.statusbar)

        self.retranslateUi(ViewEdit_Window)
        QtCore.QMetaObject.connectSlotsByName(ViewEdit_Window)

    def retranslateUi(self, ViewEdit_Window):
        _translate = QtCore.QCoreApplication.translate
        ViewEdit_Window.setWindowTitle(_translate("ViewEdit_Window", "Ver y editar películas"))
        self.txtTable.setToolTip(_translate("ViewEdit_Window", "<html><head/><body><p><br/></p></body></html>"))
        self.txtId.setText(_translate("ViewEdit_Window", "Id a editar o eliminar"))
        self.btnEdit.setText(_translate("ViewEdit_Window", "Editar"))
        self.btnDelete.setText(_translate("ViewEdit_Window", "Eliminar"))
#import GraphicResources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ViewEdit_Window = QtWidgets.QMainWindow()
    ui = Ui_ViewEdit_Window()
    ui.setupUi(ViewEdit_Window)
    ViewEdit_Window.show()
    sys.exit(app.exec_())

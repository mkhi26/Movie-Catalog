# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GuiAdd.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(636, 614)
        MainWindow.setStyleSheet("background-color: rgb(90, 90, 90);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.txtName = QtWidgets.QLineEdit(self.centralwidget)
        self.txtName.setGeometry(QtCore.QRect(140, 60, 301, 31))
        self.txtName.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtName.setObjectName("txtName")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 20, 231, 31))
        self.label.setStyleSheet("font: 14pt \"Padauk Book [SIL ]\";\n"
"    \n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 110, 231, 31))
        self.label_2.setStyleSheet("font: 14pt \"Padauk Book [SIL ]\";\n"
"    \n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.label_2.setObjectName("label_2")
        self.txtTime = QtWidgets.QLineEdit(self.centralwidget)
        self.txtTime.setGeometry(QtCore.QRect(140, 150, 301, 31))
        self.txtTime.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtTime.setObjectName("txtTime")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(140, 440, 231, 31))
        self.label_3.setStyleSheet("font: 14pt \"Padauk Book [SIL ]\";\n"
"    \n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.label_3.setObjectName("label_3")
        self.cbxCategory = QtWidgets.QComboBox(self.centralwidget)
        self.cbxCategory.setGeometry(QtCore.QRect(140, 470, 301, 23))
        self.cbxCategory.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.cbxCategory.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cbxCategory.setObjectName("cbxCategory")
        self.cbxCategory.addItem("")
        self.cbxCategory.addItem("")
        self.cbxCategory.addItem("")
        self.cbxCategory.addItem("")
        self.cbxCategory.addItem("")
        self.cbxCategory.addItem("")
        self.cbxCategory.addItem("")
        self.cbxCategory.addItem("")
        self.cbxCategory.addItem("")
        self.cbxCategory.addItem("")
        self.cbxCategory.addItem("")
        self.cbxCategory.addItem("")
        self.cbxCategory.addItem("")
        self.cbxCategory.addItem("")
        self.cbxCategory.addItem("")
        self.cbxCategory.addItem("")
        self.cbxCategory.addItem("")
        self.cbxCategory.addItem("")
        self.cbxCategory.addItem("")
        self.cbxCategory.addItem("")
        self.cbxCategory.addItem("")
        self.cbxCategory.addItem("")
        self.cbxCategory.addItem("")
        self.cbxCategory.addItem("")
        self.cbxCategory.addItem("")
        self.cbxCategory.addItem("")
        self.cbxCategory.addItem("")
        self.cbxCategory.addItem("")
        self.cbxCategory.addItem("")
        self.cbxCategory.addItem("")
        self.cbxCategory.addItem("")
        self.cbxCategory.addItem("")
        self.txtDescription = QtWidgets.QTextEdit(self.centralwidget)
        self.txtDescription.setGeometry(QtCore.QRect(140, 250, 301, 70))
        self.txtDescription.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtDescription.setObjectName("txtDescription")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(140, 210, 281, 31))
        self.label_4.setStyleSheet("font: 14pt \"Padauk Book [SIL ]\";\n"
"    \n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.label_4.setObjectName("label_4")
        self.btnCancelar = QtWidgets.QPushButton(self.centralwidget)
        self.btnCancelar.setGeometry(QtCore.QRect(130, 550, 131, 41))
        self.btnCancelar.setStyleSheet("QPushButton {\n"
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
        self.btnCancelar.setObjectName("btnCancelar")
        self.btnAgregar = QtWidgets.QPushButton(self.centralwidget)
        self.btnAgregar.setGeometry(QtCore.QRect(360, 550, 131, 41))
        self.btnAgregar.setStyleSheet("QPushButton {\n"
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
        self.btnAgregar.setObjectName("btnAgregar")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(300, 550, 59, 41))
        self.label_5.setStyleSheet("image: url(:/cct/agregar.png);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(70, 550, 59, 41))
        self.label_6.setStyleSheet("image: url(:/cct/cancelar.png);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(60, 50, 59, 41))
        self.label_7.setStyleSheet("image: url(:/cct/Pelicula.png);\n"
"")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(60, 140, 59, 41))
        self.label_8.setStyleSheet("image: url(:/cct/tiempo.png);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(50, 450, 81, 41))
        self.label_9.setStyleSheet("image: url(:/cct/palomitas.png);")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(40, 260, 81, 41))
        self.label_10.setStyleSheet("image: url(:/cct/tagdescription_102241.png);")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(140, 350, 231, 31))
        self.label_11.setStyleSheet("font: 14pt \"Padauk Book [SIL ]\";\n"
"    \n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(60, 370, 59, 41))
        self.label_12.setStyleSheet("image: url(:/cct/director.png);")
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.txtDirector = QtWidgets.QLineEdit(self.centralwidget)
        self.txtDirector.setGeometry(QtCore.QRect(140, 380, 301, 31))
        self.txtDirector.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtDirector.setObjectName("txtDirector")
        self.label_5.raise_()
        self.txtName.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.txtTime.raise_()
        self.label_3.raise_()
        self.cbxCategory.raise_()
        self.txtDescription.raise_()
        self.label_4.raise_()
        self.btnCancelar.raise_()
        self.btnAgregar.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.txtDirector.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Agregar películas"))
        self.txtName.setText(_translate("MainWindow", "Nombre"))
        self.label.setText(_translate("MainWindow", "Nombre de películas"))
        self.label_2.setText(_translate("MainWindow", "Duración"))
        self.txtTime.setText(_translate("MainWindow", "HH: MM: SS"))
        self.label_3.setText(_translate("MainWindow", "Categoría de la película"))
        self.cbxCategory.setItemText(0, _translate("MainWindow", "Acción"))
        self.cbxCategory.setItemText(1, _translate("MainWindow", "Artes marciales"))
        self.cbxCategory.setItemText(2, _translate("MainWindow", "Aventuras"))
        self.cbxCategory.setItemText(3, _translate("MainWindow", "Bélicas"))
        self.cbxCategory.setItemText(4, _translate("MainWindow", "Comedia"))
        self.cbxCategory.setItemText(5, _translate("MainWindow", "Comedias musicales"))
        self.cbxCategory.setItemText(6, _translate("MainWindow", "Ciencia ficción"))
        self.cbxCategory.setItemText(7, _translate("MainWindow", "Deportivas"))
        self.cbxCategory.setItemText(8, _translate("MainWindow", "Dibujos Animados"))
        self.cbxCategory.setItemText(9, _translate("MainWindow", "Documental"))
        self.cbxCategory.setItemText(10, _translate("MainWindow", "Dramáticas"))
        self.cbxCategory.setItemText(11, _translate("MainWindow", "Espada y hechicería"))
        self.cbxCategory.setItemText(12, _translate("MainWindow", "Espionaje"))
        self.cbxCategory.setItemText(13, _translate("MainWindow", "Fantásticas"))
        self.cbxCategory.setItemText(14, _translate("MainWindow", "Hechos reales"))
        self.cbxCategory.setItemText(15, _translate("MainWindow", "Horror"))
        self.cbxCategory.setItemText(16, _translate("MainWindow", "Infantiles"))
        self.cbxCategory.setItemText(17, _translate("MainWindow", "Misterio"))
        self.cbxCategory.setItemText(18, _translate("MainWindow", "Muertos vivientes"))
        self.cbxCategory.setItemText(19, _translate("MainWindow", "Musicales"))
        self.cbxCategory.setItemText(20, _translate("MainWindow", "Policíales"))
        self.cbxCategory.setItemText(21, _translate("MainWindow", "Propaganda"))
        self.cbxCategory.setItemText(22, _translate("MainWindow", "Psicológicas"))
        self.cbxCategory.setItemText(23, _translate("MainWindow", "Suspenso"))
        self.cbxCategory.setItemText(24, _translate("MainWindow", "Románticas"))
        self.cbxCategory.setItemText(25, _translate("MainWindow", "Sobre Animales"))
        self.cbxCategory.setItemText(26, _translate("MainWindow", "Sobre aviación"))
        self.cbxCategory.setItemText(27, _translate("MainWindow", "Sobre delincuencia"))
        self.cbxCategory.setItemText(28, _translate("MainWindow", "Sobre discapacitados"))
        self.cbxCategory.setItemText(29, _translate("MainWindow", "Sobre religión"))
        self.cbxCategory.setItemText(30, _translate("MainWindow", "Sobre política"))
        self.cbxCategory.setItemText(31, _translate("MainWindow", "Terror"))
        self.txtDescription.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Descripción</p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "Descripción de la películas"))
        self.btnCancelar.setText(_translate("MainWindow", "Cancelar"))
        self.btnAgregar.setText(_translate("MainWindow", "Agregar"))
        self.label_11.setText(_translate("MainWindow", "Director de la película"))
        self.txtDirector.setText(_translate("MainWindow", "Director"))
#import GraphicResources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

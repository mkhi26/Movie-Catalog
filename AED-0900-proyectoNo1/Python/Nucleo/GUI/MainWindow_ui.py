# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 450)
        MainWindow.setToolTip("")
        MainWindow.setStyleSheet("background-image: url(:/cct/mainSkin7.jpg);")
        MainWindow.setAnimated(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnOpenWindowAdd = QtWidgets.QPushButton(self.centralwidget)
        self.btnOpenWindowAdd.setGeometry(QtCore.QRect(120, 90, 201, 41))
        self.btnOpenWindowAdd.setStyleSheet("QPushButton {\n"
"    background-color: rgb(0, 170, 0);\n"
"    background-image: url(:/cct/Acerca de.png);\n"
"    color: rgb(0, 0, 0);\n"
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
"    \n"
"    background-color: rgb(255, 170, 0);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    \n"
"    background-color: rgb(255, 255, 0);\n"
"    }")
        self.btnOpenWindowAdd.setObjectName("btnOpenWindowAdd")
        self.btnOpenWindowEditList = QtWidgets.QPushButton(self.centralwidget)
        self.btnOpenWindowEditList.setGeometry(QtCore.QRect(120, 160, 201, 41))
        self.btnOpenWindowEditList.setStyleSheet("QPushButton {\n"
"    \n"
"    background-color: rgb(0, 170, 0);\n"
"    \n"
"    background-image: url(:/cct/Acerca de.png);\n"
"    color: rgb(0, 0, 0);\n"
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
"    background-color: rgb(255, 170, 0);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    \n"
"    background-color: rgb(255, 255, 0);\n"
"    }")
        self.btnOpenWindowEditList.setObjectName("btnOpenWindowEditList")
        self.btnOpenWindowViewTree = QtWidgets.QPushButton(self.centralwidget)
        self.btnOpenWindowViewTree.setGeometry(QtCore.QRect(120, 230, 201, 41))
        self.btnOpenWindowViewTree.setStyleSheet("QPushButton {\n"
"    \n"
"    \n"
"    \n"
"    background-color: rgb(0, 170, 0);\n"
"    \n"
"    background-image: url(:/cct/Acerca de.png);\n"
"    color: rgb(0, 0, 0);\n"
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
"    background-color: rgb(255, 170, 0);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    \n"
"    background-color: rgb(255, 255, 0);\n"
"    }")
        self.btnOpenWindowViewTree.setObjectName("btnOpenWindowViewTree")
        self.btnOpenWindowAbout = QtWidgets.QPushButton(self.centralwidget)
        self.btnOpenWindowAbout.setGeometry(QtCore.QRect(120, 300, 201, 41))
        self.btnOpenWindowAbout.setStyleSheet("QPushButton {\n"
"\n"
"    \n"
"    \n"
"    background-color: rgb(0, 170, 0);\n"
"    \n"
"    background-image: url(:/cct/Acerca de.png);\n"
"    color: rgb(0, 0, 0);\n"
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
"    background-color: rgb(255, 170, 0);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    \n"
"    background-color: rgb(255, 255, 0);\n"
"    }")
        self.btnOpenWindowAbout.setObjectName("btnOpenWindowAbout")
        self.lblCounter = QtWidgets.QLabel(self.centralwidget)
        self.lblCounter.setGeometry(QtCore.QRect(380, 170, 111, 41))
        self.lblCounter.setStyleSheet("background-image: url(:/cct/full glass.png);\n"
"selection-background-color: rgb(255, 0, 0);\n"
"color: rgb(0, 0, 0);\n"
"\n"
"font: 30pt \"FreeSerif\";")
        self.lblCounter.setObjectName("lblCounter")
        self.lblCounter_3 = QtWidgets.QLabel(self.centralwidget)
        self.lblCounter_3.setGeometry(QtCore.QRect(80, 100, 31, 21))
        self.lblCounter_3.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"background-image: url(:/cct/full glass.png);\n"
"image: url(:/cct/AgregarInventario.png);\n"
"color: rgb(255, 255, 255);\n"
"font: oblique 24pt \"Serif\";\n"
"border-color: rgb(255, 255, 255);")
        self.lblCounter_3.setText("")
        self.lblCounter_3.setObjectName("lblCounter_3")
        self.lblCounter_4 = QtWidgets.QLabel(self.centralwidget)
        self.lblCounter_4.setGeometry(QtCore.QRect(80, 170, 31, 21))
        self.lblCounter_4.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"background-image: url(:/cct/full glass.png);\n"
"image: url(:/cct/verLista.png);\n"
"color: rgb(255, 255, 255);\n"
"font: oblique 24pt \"Serif\";\n"
"border-color: rgb(255, 255, 255);")
        self.lblCounter_4.setText("")
        self.lblCounter_4.setObjectName("lblCounter_4")
        self.lblCounter_5 = QtWidgets.QLabel(self.centralwidget)
        self.lblCounter_5.setGeometry(QtCore.QRect(80, 240, 31, 21))
        self.lblCounter_5.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"background-image: url(:/cct/full glass.png);\n"
"image: url(:/cct/Active_Directory-80_icon-icons.com_57383.png);\n"
"color: rgb(255, 255, 255);\n"
"font: oblique 24pt \"Serif\";\n"
"border-color: rgb(255, 255, 255);")
        self.lblCounter_5.setText("")
        self.lblCounter_5.setObjectName("lblCounter_5")
        self.lblCounter_6 = QtWidgets.QLabel(self.centralwidget)
        self.lblCounter_6.setGeometry(QtCore.QRect(80, 310, 31, 21))
        self.lblCounter_6.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"background-image: url(:/cct/full glass.png);\n"
"image: url(:/cct/Acerca de.png);\n"
"color: rgb(255, 255, 255);\n"
"font: oblique 24pt \"Serif\";\n"
"border-color: rgb(255, 255, 255);")
        self.lblCounter_6.setText("")
        self.lblCounter_6.setObjectName("lblCounter_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ventana Principal"))
        self.btnOpenWindowAdd.setText(_translate("MainWindow", "Agregar"))
        self.btnOpenWindowEditList.setText(_translate("MainWindow", "Ver y editar listado"))
        self.btnOpenWindowViewTree.setText(_translate("MainWindow", "Visualización de Árbol"))
        self.btnOpenWindowAbout.setText(_translate("MainWindow", "Acerca de"))
        self.lblCounter.setToolTip(_translate("MainWindow", "<html><head/><body><p>1000</p></body></html>"))
        self.lblCounter.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\"><br/></span></p></body></html>"))
        self.lblCounter.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; color:#000000;\">0</span></p></body></html>"))
        self.lblCounter_3.setToolTip(_translate("MainWindow", "<html><head/><body><p>1000</p></body></html>"))
        self.lblCounter_3.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\"><br/></span></p></body></html>"))
        self.lblCounter_4.setToolTip(_translate("MainWindow", "<html><head/><body><p>1000</p></body></html>"))
        self.lblCounter_4.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\"><br/></span></p></body></html>"))
        self.lblCounter_5.setToolTip(_translate("MainWindow", "<html><head/><body><p>1000</p></body></html>"))
        self.lblCounter_5.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\"><br/></span></p></body></html>"))
        self.lblCounter_6.setToolTip(_translate("MainWindow", "<html><head/><body><p>1000</p></body></html>"))
        self.lblCounter_6.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\"><br/></span></p></body></html>"))
#import GraphicResources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

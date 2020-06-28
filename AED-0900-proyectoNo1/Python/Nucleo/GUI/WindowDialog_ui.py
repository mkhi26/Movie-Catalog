# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GuiDialogConfirm.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(369, 151)
        Dialog.setStyleSheet("background-color: rgb(85, 85, 127);")
        self.lblTxtCuestion = QtWidgets.QLabel(Dialog)
        self.lblTxtCuestion.setGeometry(QtCore.QRect(100, 50, 181, 31))
        self.lblTxtCuestion.setObjectName("lblTxtCuestion")
        self.btnConfirm = QtWidgets.QPushButton(Dialog)
        self.btnConfirm.setGeometry(QtCore.QRect(210, 110, 101, 23))
        self.btnConfirm.setStyleSheet("image: url(:/cct/confirm.png);\n"
"background-color: rgb(0, 85, 255);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/cct/confirm.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnConfirm.setIcon(icon)
        self.btnConfirm.setIconSize(QtCore.QSize(30, 20))
        self.btnConfirm.setObjectName("btnConfirm")
        self.btnCancel = QtWidgets.QPushButton(Dialog)
        self.btnCancel.setGeometry(QtCore.QRect(90, 110, 91, 23))
        self.btnCancel.setStyleSheet("background-color: rgb(0, 85, 255);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/cct/cancelar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCancel.setIcon(icon1)
        self.btnCancel.setObjectName("btnCancel")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 40, 59, 41))
        self.label_2.setStyleSheet("image: url(:/cct/cuestion.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.btnConfirm, self.btnCancel)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lblTxtCuestion.setWhatsThis(_translate("Dialog", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.lblTxtCuestion.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">¿Esta seguro?</span></p></body></html>"))
        self.btnConfirm.setText(_translate("Dialog", "Confirmar"))
        self.btnCancel.setText(_translate("Dialog", "Cancelar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QEvent
from PyQt5.QtGui import QInputEvent, QMouseEvent
from Nucleo.GUI.WindowViewEdit_ui import Ui_ViewEdit_Window
from Nucleo.WindowDialogError import DialogError
from Nucleo.WindowDialog import DialogConfirm



class WindowViewEdit (QMainWindow):

    def __init__(self, parent = None):

        
        super(WindowViewEdit, self).__init__(parent)
        self.uiViewEdit = Ui_ViewEdit_Window()
        self.uiViewEdit.setupUi(self)
        self.centerWindow()

        # Instancia de dialogos:
        self.uiEditDialog = DialogConfirm()
        self.uiEditErrorDialog = DialogError()
        self.uiRemoveDialog = DialogConfirm()

        # Eventos los botones de la pantalla Editar
        self.uiViewEdit.btnEdit.clicked.connect(self.openDialogEdit)
        self.uiViewEdit.btnDelete.clicked.connect(self.openDialogRemove)
        

        #Eventos de los dialogos de Error:
        self.uiEditErrorDialog.uiDialogError.btnConfirmar.clicked.connect(self.closeErrorDialog)

        #Eventos de los dialogos de confirmacion.
        self.uiEditDialog.uiDialog.btnCancel.clicked.connect(self.closeDialogEdit)
        self.uiRemoveDialog.uiDialog.btnCancel.clicked.connect(self.closeDialogRemove)

    # Funciones de la ventana ver y editar.

    """
    Nombre: getId
    Parametros: No recibe parametros.
    Descripcion: Obtiene el id del campo de texto.
    Retorno: retorna un Int si el id es valido, False en caso contrario.
    """
    def getId(self):
        validate = self.validateFieldsEdit()
        if(validate):
            idEditOrDelete = int(self.uiViewEdit.txtId.text())
            return idEditOrDelete
        else:
            self.showErrorDialogEdit()
            self.closeDialogRemove()
            return False


    """
    Nombre: validateFieldsEdit
    Parametros: No recibe parametros.
    Descripcion: Comprueba que el campo de texto que almacena el Id este lleno y ademas
                 comprueba que sea un numero entero.
    Retorno: Retorna True en caso de que el id ingresado sea valido.
    """
    def validateFieldsEdit(self):
        try:
            idEditOrDelete = int(self.uiViewEdit.txtId.text())
            return True
        except:
            return False

    """
    Nombre: showErrorDialogEdit
    Parametros: No recibe parametros.
    Descripcion: Muestra un dialogo de error en caso de que el id ingresado no sea valido
    Retorno: Retorna True
    """
    def showErrorDialogEdit(self):
        self.uiEditErrorDialog.uiDialogError.txtError.setText("No hay peliculas agregadas\n con ese ID")
        self.uiEditErrorDialog.show()
        return True

    """
    Nombre: CloseErrorDialogEdit
    Parametros: No recibe parametros.
    Descripcion: Cierra el dialogo de error.
    Retorno: Retorna True
    """
    def closeErrorDialog(self):
        self.uiEditErrorDialog.close()
        return True
    """
    Nombre: openDialogEdit
    Parametros: No recibe parametros.
    Descripcion: Abre un dialogo de confirmar edicion.
    Retorno: Retorna True
    """
    def openDialogEdit(self):
        self.uiEditDialog.show()
        return True
            
    """
    Nombre: closeDialogEdit
    Parametros: No recibe parametros.
    Descripcion: Cierra el dialogo de confirmar edicion.
    Retorno: Retorna True
    """
    def closeDialogEdit(self):
        self.uiEditDialog.close()
        return True

    """
    Nombre: openDialogRemove
    Parametros: No recibe parametros.
    Descripcion: Abre un dialogo
    Retorno: Retorna True

    """
    def openDialogRemove(self):
        self.uiRemoveDialog.show()
        return True

    """
    Nombre: closeDialogRemove
    Parametro: No recibe parametros.
    Descripcion: Cierra un dialogo de confirmacion.
    Retorno: Retorna True.
    """
    def closeDialogRemove(self):
        self.uiRemoveDialog.close()
        return True
        
    """
    Nombre: centerWindow
    Parametros: No recibe parametros
    Descripcion: Inicializa la ventana al centro de la pantalla.
    Retorno: Retorna True
    """
    def centerWindow(self):
        screen = self.frameGeometry()
        ubication = QtWidgets.QDesktopWidget().availableGeometry().center()
        screen.moveCenter(ubication)
        self.move(screen.topLeft())
    



    

    
# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from Nucleo.GUI.WindowAdd_ui import Ui_MainWindow
from Nucleo.WindowDialogError import DialogError
from Nucleo.WindowDialog import DialogConfirm
from Nucleo.TimeManager import *
from Nucleo.Catalog import *
from Nucleo.BST import *
from Nucleo.MemoryManager import *
from Nucleo.TableAscii import *
class WindowAdd(QMainWindow):
    def __init__(self, parent = None):
        super(WindowAdd, self).__init__(parent)
        self.uiAdd = Ui_MainWindow()
        self.uiAdd.setupUi(self)
        self.centerWindow()

        # Instancia de los dialogos
        self.uiDialogConfirmationAdd = DialogConfirm()
        self.uiDialogConfirmationCancel = DialogConfirm()
        self.uiDialogError = DialogError()
        
        # Eventos de los botones de la pantalla Agregar.
        self.uiAdd.btnAgregar.clicked.connect(self.openDialogConfirmationAdd)
        self.uiAdd.btnCancelar.clicked.connect(self.openDialogConfirmationCancel)

        # Eventos de los botones de los dialogBox
        self.uiDialogConfirmationAdd.uiDialog.btnConfirm.clicked.connect(self.eventAddOrEdit)
        self.uiDialogConfirmationAdd.uiDialog.btnCancel.clicked.connect(self.closeDialogConfirmationAdd)
        self.uiDialogConfirmationCancel.uiDialog.btnConfirm.clicked.connect(self.closeDialogConfirmationCancel)
        self.uiDialogConfirmationCancel.uiDialog.btnCancel.clicked.connect(self.closeDialogConfirmationCancel)
        self.uiDialogError.uiDialogError.btnConfirmar.clicked.connect(self.closeDialogError)
        

        # Variables
        self.idEdit= -1
        self.idRemove =-1
        self.add=True
        self.edit = False
        self.remove = False
        #Otras instancias
        self.table = TableAsscii()
        self.timeManager = TimeManager()
        self.memory = MemoryManager()
        self.catalog = Catalog()
        self.memory.getFromMemory()
        self.catalog =self.memory.getCatalogFromMemory()


    # Funciones para editar:

    """
    Nombre: activateEdition
    Paramereos: No recibe parametros
    Descripcion: activa la variable booleana edit para asegurar que se esta editando
                 en lugar de eliminar o agregar.
    Retorno: True
    """
    def activateEdition(self, idEdit):
        self.edit = True
        self.add = False
        self.remove = False
        self.idEdit = idEdit
        return True
    """
    Nombre: activateAdd
    Parametros: No recibe parametros.
    Descripcion: activa la variable booleana Add para asegurar que se esta agregando 
                 en lugar de editar o eliminar.
    Retorno: True
    """

    def activateAdd(self):
        self.add=True
        self.edit = False
        self.remove = False
        return True
    """
    Nombre: activateRemove
    Parametros: No recibe parametros.
    Descripcion: activa la variable booleana remove para asegurar que se esta eliminando 
                 en lugar de editar o eliminar.
    Retorno: True
    """
    def activateRemove(self, idRemove):
        self.remove =True
        self.edit =False
        self.add = False
        self.idRemove = idRemove
        return True
    """
    Nombre: setTextBox
    Parametros: No recibe parametros.
    Descripcion: Hace el set de los atributos del objeto que se esta editando hacia los textbox
                 de la pantalla de agregar.
    Retorno: Retorna True.

    """
    def setTextBox(self):
        movieEdit = self.catalog.getMovieFromList(self.idEdit)
        self.uiAdd.txtName.setText(movieEdit.nameMovie)
        self.uiAdd.txtTime.setText(movieEdit.timeMovie)
        self.uiAdd.txtDirector.setText(movieEdit.directorMovie)
        self.uiAdd.txtDescription.setText(movieEdit.descriptionMovie)
        return True


    # Funciones para agregar:

    """
    Nombre: getTextBox
    Parametros: No recibe parametro.
    Descripcion: Obtiene los datos de los textbox de la pantalla, luego crea el objeto Movie 
                y lo retorna.
    Retorno: Retorna un objeto Movie.
    """
    def getTextBoxForAdd(self):
        time = self.uiAdd.txtTime.text()
        validate= self.timeManager.verificateformate(time)
        if(not validate):
            self.openDialogError()
            return False
        idMovie = self.catalog.asignateId()
        nameMovie = self.uiAdd.txtName.text()
        descriptionMovie = str(self.uiAdd.txtDescription.toPlainText())
        directorMovie= self.uiAdd.txtDirector.text()
        category = self.uiAdd.cbxCategory.currentText()
        objMovie =Movie(nameMovie,time,descriptionMovie,directorMovie,category,idMovie)
        return objMovie

    #Funciones para editar.
    """
    Nombre: getTextBoxForEdit
    Parametros: No recibe parametro.
    Descripcion: Obtiene los datos de los textbox de la pantalla, luego crea el objeto Movie 
                y lo retorna.
    Retorno: Retorna un objeto Movie.
    """
    def getTextBoxForEdit(self):
        time = self.uiAdd.txtTime.text()
        validate= self.timeManager.verificateformate(time)
        if(not validate):
            self.openDialogError()
            return False
        idMovie = self.idEdit
        nameMovie = self.uiAdd.txtName.text()
        descriptionMovie = str(self.uiAdd.txtDescription.toPlainText())
        directorMovie= self.uiAdd.txtDirector.text()
        category = self.uiAdd.cbxCategory.currentText()
        objMovie =Movie(nameMovie,time,descriptionMovie,directorMovie,category,idMovie)
        return objMovie
    
    #Funciones de los DialogBox

    #1. Abrir y cerrar dialogos.
    """
    Nombre: openDialogError
    Parametros: No recibe parametros.
    Descripcion: Abre un dialogo que muestra un texto de error.
    Retorno: Retorna True
    """
    def openDialogError(self):
        self.uiDialogError.uiDialogError.txtError.setText("Error, el tiempo de duracion\nde la pelicula no es valido.")
        self.uiDialogError.show()
        return True

    """
    Nombre: closeDialogError
    Parametros: No recibe parametros.
    Descripcion: cierra el dialogo de error.
    Retorno: Retorna True.
    """
    def closeDialogError(self):
        self.uiDialogError.close()
        return True

    """
    Nombre: openDialogConfirmationAdd
    Parametros: No recibe parametrosconfirmación
    Descripcion: Abre un dialogo de confirmacion que muestra una pregunta para 
                 confirmar la accion de agregar.
    Retorno: Retorna True
    """
    def openDialogConfirmationAdd(self):
        validateFields = self.validateFields()
        if(validateFields):
            self.uiDialogConfirmationAdd.setWindowTitle("¿Agregar?")
            self.uiDialogConfirmationAdd.show()
            return True
        self.uiDialogError.uiDialogError.txtError.setText("Error, uno o mas campos están vacíos")
        self.uiDialogError.show()
        return False

    """
    Nombre: validateFields
    Parametros: No recibe parametros.
    Descripcion: Comprueba que los campos de los textBox esten llenos.
    Retorno: Retorna True en caso de que esten llenos,False en caso contrario.

    """
    def validateFields(self):
        name = self.uiAdd.txtName.text()
        time = self.uiAdd.txtTime.text()
        director = self.uiAdd.txtDirector.text()
        description = self.uiAdd.txtDescription.toPlainText()
        if(name =="" or time == "" or director =="" or description==""):
            return False
        return True

    """
    Nombre: closeDialogConfirmationAdd
    Parametros: No recibe parametros.
    Descripcion: Cierra el dialogo de confirmacion para agregar
    Retorno: Retorna True
    """
    def closeDialogConfirmationAdd(self):
        self.uiDialogConfirmationAdd.close()
        return True
    """
    Nombre: openDialogConfirmationCancel
    Parametros: No recibe parametrosconfirmación
    Descripción: Abre un dialogo de confirmación que muestra una pregunta para 
                 confirmar si quiere cancelar la acción.
    Retorno: Retorna True
    """
    def openDialogConfirmationCancel(self):
        self.uiDialogConfirmationCancel.setWindowTitle("¿Cancelar?")
        self.uiDialogConfirmationCancel.show()
        return True
    

    """
    Nombre: closeDialogConfirmationCancel
    Parametros: No recibe parametros.
    Descripcion: Cierra el dialogo de confirmacion de el boton cancelar.
    Retorno: Retorna True
    """
    def closeDialogConfirmationCancel(self):
        self.uiDialogConfirmationCancel.close()
        return True

    #2. Evento de los dialogos

    """
    Nombre: eventAdd
    Parametros: No recibe parametros.
    Descripcion: Al momento de hacer click en el boton aceptar del dialogo de confirmacion
                se agregara la pelicula al catalogo.
    Retorno: Retorna True
    """
    def eventAddOrEdit(self):
        if(self.add):
            objMovie = self.getTextBoxForAdd()
            self.catalog.addMovie(objMovie)
            self.memory.saveCatalog(self.catalog)
            self.closeDialogConfirmationAdd()
            self.cleanTextBox()
            self.activateAdd()
            self.idEdit =-1
            self.idRemove = -1
            return True
        elif(self.edit):
            movieEdit = self.getTextBoxForEdit()
            self.catalog.editMovie(self.idEdit,movieEdit)
            self.memory.saveCatalog(self.catalog)
            self.closeDialogConfirmationAdd()
            self.close()
            self.activateAdd()
            self.idEdit =-1
            self.idRemove = -1
            return True
        return False
    # Otras funciones

    """
    Nombre: cleanTextBox
    Parametros: No recibe parametros.
    Descripcion: Limpia los formularios de los textBox
    Retorno: Retorna True
    """
    def cleanTextBox(self):
        formate = self.uiAdd.txtTime.text()
        validate = self.timeManager.verificateformate(formate)
        if(validate):
            self.uiAdd.txtDescription.setPlainText("")
            self.uiAdd.txtDirector.setText("")
            self.uiAdd.txtName.setText("")
            self.uiAdd.txtTime.setText("HH:MM.SS")
            self.uiAdd.cbxCategory.setCurrentIndex(0)
        return True

    """
    Nombre: getIndexCbx
    Parametros: Recibe el String a buscar en el comboBox
    Descripcion: Genera la posicion de el comboBox.
    Retorno: Retorna la posicion del item en el comboBox
    """
    
    def getIndexCbx(self, category):
        array=[]
        array.append("Acción")
        array.append("Artes marciales")
        array.append("Aventuras") 
        array.append("Bélicas")
        array.append("Comedia")
        array.append("Comedias musicales")
        array.append("Ciencia ficción")
        array.append("Deportivas")
        array.append("Dibujos Animados")
        array.append("Documental")
        array.append("Dramáticas")
        array.append("Espada y hechicería")
        array.append("Espionaje")
        array.append("Fantásticas")
        array.append("Hechos reales")
        array.append("Horror")
        array.append("Infantiles")
        array.append("Misterio")
        array.append("Muertos vivientes")
        array.append("Musicales")
        array.append("Policíales")
        array.append("Propaganda")
        array.append("Psicológicas")
        array.append("Suspenso")
        array.append("Románticas")
        array.append("Sobre Animales")
        array.append("Sobre aviación")
        array.append("Sobre delincuencia")
        array.append("Sobre discapacitados")
        array.append("Sobre religión")
        array.append("Sobre política")
        for i in range(len(array)):
            if(array[i]== category):
                return i
        return 0

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
        return True


        

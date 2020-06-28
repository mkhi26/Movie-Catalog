#-*-coding:utf-8 -*-
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from Nucleo.GUI.MainWindow_ui import Ui_MainWindow
from Nucleo.GUI.GraphicResources_rc import *
from Nucleo.WindowAdd import WindowAdd
from Nucleo.WindowEdit import WindowViewEdit
from Nucleo.WindowAbout import WindowAbout
from Nucleo.WindowTreeTime import WindowTreeTime
from Nucleo.WindowTreeHierarchy import WindowTreeHierarchy

class main(QMainWindow):
    def __init__(self):
        super(main, self).__init__()

        # Se inicializa la ventana principal
        self.mainWindow = Ui_MainWindow()
        self.mainWindow.setupUi(self)
        self.centerWindow()

        # Instancias de las ventanas secundarias.
        self.uiAdd = WindowAdd()
        self.uiEdit = WindowViewEdit()
        self.uiAbout = WindowAbout()
        self.uiTreeTime= WindowTreeTime()
        self.uiTreeHierarchy = WindowTreeHierarchy()

        self.updateData()

        #  Variables Centinelas de la pantalla Ver y editar.
        self.edit = False
        self.idEditOrDelete = -1


        # Eventos de Botones de la pantalla principal.
        self.mainWindow.btnOpenWindowAdd.clicked.connect(self.openWindowAdd)
        self.mainWindow.btnOpenWindowEditList.clicked.connect(self.openWindowEdit)
        self.mainWindow.btnOpenWindowAbout.clicked.connect(self.openWindowAbout)
        self.mainWindow.btnOpenWindowViewTree.clicked.connect(self.viewTree)
        # Eventos de los botones de la pantalla agregar.
        self.uiAdd.uiDialogConfirmationCancel.uiDialog.btnConfirm.clicked.connect(self.closeWindowAdd)
        self.uiAdd.uiDialogConfirmationAdd.uiDialog.btnConfirm.clicked.connect(self.updateData)

        # Eventos de botones de la pantalla Editar
        self.uiEdit.uiEditDialog.uiDialog.btnConfirm.clicked.connect(self.eventEdit)
        self.uiEdit.uiRemoveDialog.uiDialog.btnConfirm.clicked.connect(self.eventRemove)




    #Funcion de la ventana Editar:
    def openDialogEdit(self):
        self.uiEdit.uiEditDialog.show()
        return True
    """
    Nombre: eventRemove
    Parametros: No recibe parametros
    Descripcion: Es el evento del boton del dialogo de eliminar.
    Retorno: Retorna True o False
    """
    def eventRemove(self):
        idRemove = self.uiEdit.getId()
        validate = self.uiEdit.validateFieldsEdit()
        searchId = self.uiAdd.catalog.search(idRemove)
        if(validate):
            if(not searchId):
                self.uiEdit.showErrorDialogEdit()
                self.uiEdit.closeDialogRemove()
                return False
            self.uiAdd.catalog.deleteMovie(idRemove)
            self.uiAdd.memory.saveCatalog(self.uiAdd.catalog)
            self.uiEdit.closeDialogRemove()
            self.updateData()
            return True
        return False

    """
    Nombre: eventEdit
    Parametros: No recibe parametros
    Descripcion: evento editar, se activa desde el dialogo de confirmacion de la ventana editar
                 hace las validaciones correspondientes de tal manera que el id a editar sea valido y si es valido
                 obtiene el objeto a editar y completa los campos de texto.
    Retorno: retorna True en caso que la operacion se realice correctamente, False en caso contrario.
    """
    def eventEdit(self):
        idEdit = self.uiEdit.getId()
        validate = self.uiEdit.validateFieldsEdit()
        searchId = self.uiAdd.catalog.search(idEdit)
        if(validate):
            if(not searchId):
                self.uiEdit.showErrorDialogEdit()
                self.uiEdit.closeDialogEdit()
                return False
            self.uiAdd.activateEdition(idEdit)
            self.uiAdd.setTextBox()
            self.uiAdd.show()
            self.uiEdit.closeDialogEdit()
            self.uiEdit.uiViewEdit.txtId.setText("")
            self.updateData()

            return True
        self.uiEdit.closeDialogEdit()
        return False
        
    #Funciones OpenWindow
    """
    Nombre: openWindowAdd
    Parametros: No recibe parametro.
    Descripción: Abre una ventana con el formulario de agregar Película.
    Retorno: Retorna True
    """
    def openWindowAdd(self):
        self.uiAdd.cleanTextBox()
        self.uiAdd.show()
        return True
    """
    Nombre: openWindowEdit
    Parametros: No recibe parametro.
    Descripción: Abre una ventana que muestra uns tabla con las películas agregadas
                 ademas muestra un formulario para editar o eliminar Películas.
    Retorno: Retorna True
    """
    def openWindowEdit(self):
        self.uiEdit.show()
        return True
    """
    Nombre: openWindowAbout
    Parametros: No recibe parametro.
    Descripción: Abre una ventana con los créditos del desarrollo del proyecto.
    Retorno: Retorna True
    """
    def openWindowAbout(self):
        self.uiAbout.show()
        return True

    #Funciones closeWindow

    """
    Nombre: closeWindowAdd
    Parametros: No recibe parametros.
    Descripcion: Cierra la ventana de editar.
    Retorno: Retorna True.
    """
    def closeWindowAdd(self):
        self.uiAdd.close()
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


    """
        Nombre: updateLabel
        Parametros: No recibe parametros.
        Descripcion: Permite actualizar el contador que se muestra en la pantalla de inicio.
        Retorno: Retorna True.
    """
    def updateLabel(self):
        size = str(self.uiAdd.catalog.listMovie.length())
        txtLbl= "    %s"%(size)
        self.mainWindow.lblCounter.setText(txtLbl)
        return True

    """
        Nombre: updateTable
        Parametros: No recibe parametros.
        Descripcion: Permite actualizar la tabla que se muestra en la ventana ver y editar.
        Retorno: Retorna True.
    """
    def updateTable(self):
        catalog = self.uiAdd.catalog
        conten = self.uiAdd.table.createTable(self.uiAdd.catalog)
        self.uiEdit.uiViewEdit.txtTable.setReadOnly(True)
        self.uiEdit.uiViewEdit.txtTable.setPlainText(conten)
        return True

    """
        Nombre: updateData
        Parametros: No recibe parametros.
        Descripcion: Permite actualizar la tabla y el contador que se muestra en la ventana ver y editar y en la pantalla
                    de inicio respectivamente.
        Retorno: Retorna True.
    """
    def updateData(self):
        self.updateLabel()
        self.updateTable()
        return True
    """
    Nombre: openWindowTreeTime
    Parametros: No recibe parametros.
    Descripcion: Abre una ventana que muestra un árbol binario con las peliculas agregadas
                 al inventario.
    Retorno: Retonrna un booleano.
    """
    def openWindowTreeTime(self):
        self.uiTreeTime.uiWindowTreeTime.txtViewTree.setReadOnly(True)
        validate = self.uiAdd.catalog.viewTree()
        if(validate):
            self.uiTreeTime.uiWindowTreeTime.txtViewTree.setHtml("<img src=\"Nucleo/tree.png\">")
        else:
            self.uiTreeTime.uiWindowTreeTime.txtViewTree.setHtml("")
        self.uiTreeTime.show()
        return True

    """
    Nombre: openWindowTreeHierarchy
    Parametros: No recibe parametros.
    Descripcion: Abre una ventana que muestra un árbol jerárquico.
                    1. El textbox se habilita en modo de solo lectura.
                    2. Se agrega la imagen que se quiere visualizar (Árbol jerarquico) a través 
                    del método setHTML que incrusta la imagen mediante código HTML
    Retorno: Retorna un booleano.
    """
    def openWindowTreeHierarchy(self):
        self.uiTreeHierarchy.uiTreeHierarchy.txtViewTree.setReadOnly(True)
        if(self.uiAdd.catalog.treeN.validate()):
            self.uiTreeHierarchy.uiTreeHierarchy.txtViewTree.setHtml("<img src=\"Nucleo/treeN.png\">")
        else:
            self.uiTreeHierarchy.uiTreeHierarchy.txtViewTree.setHtml("")
        self.uiTreeHierarchy.show()
        return True
        

    """
    Nombre: viewTree
    Parametros: No recibe parametros.
    Descripcion: Llama a la funcion viewTree del catalogo de peliculas para generar la imagenes de Árbol
                 luego llama a las funciones openWindowTreeTime y openWindowTreeHierarchy  para abrir las ventanas.
    Retorno: Retorna Un booleano.

    """
    def viewTree(self):
        self.uiAdd.catalog.viewTree()
        self.uiAdd.catalog.viewTreeN()
        self.openWindowTreeTime()
        self.openWindowTreeHierarchy()
        return True


        
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = main()
    main.show()
    sys.exit(app.exec_())
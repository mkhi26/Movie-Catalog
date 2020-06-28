from Nucleo.NodeBst import *
from Nucleo.LinkedList import *
from Nucleo.BST import *
from Nucleo.Movie import *
from Nucleo.TimeManager import *
import networkx as nx

"""
Nombre: BST
Descripcion: Es el TDA BST: Binary Search Tree, permite agregar elementos al arbol de manera ordenada para
             obtener una busqueda mas eficiente de estos elementos.
Atributos: self. root: Es la raiz del Arbol, por defecto esta en None pero al agregar
           elementos se convertira en un nodo que tiene mas hijos y estos hijos por defecto estaran en None.
            
            self.g : Es una instancia del Grafo de Network X, nos permite agregar los elementos al grafo para
            mostrarlos de manera grafica.
            
            self.timeManager:  Permite gestionar el tiempo.

"""
class BST:
    def __init__(self):
        self.root = None
        self.g = nx.Graph()
        #self.g = nx.dodecahedral_graph()
        self.timeManager = TimeManager()

    """
    Nombre: BSTAdd
    Parametros:   Value = valor que se quiere agregar al árbol.
    Descripcion: Llama a la funcion BSTAddInner.
    Retorna: Retorna un llamado a la funcion BSTAddInner
    """
    def BSTAdd(self, value):
        return self.BSTAddInner(value,self.root)

    """
    Nombre: BSTAddInner
    Parametros: 
                Value: Valor que se quiere agregar al arbol.
                Current: La raiz actual donde se quiere agregar.
    Descripcion: Esta funcion agrega elementos al árbol binario.

    Retorno: Retorna un booleano.
                True: Si se agrego correctamente.
                False: si no se pudo agregar.

    """
    def BSTAddInner(self,value, current):
        valueTime = self.timeManager.convertTimeToSeconds(value.timeMovie)
        if(not self.root):
            self.root = NodeBst(value)
            return True
        currentTime = self.timeManager.convertTimeToSeconds(current.value.timeMovie)
        if(currentTime > valueTime):
            if(not current.left):
                current.left = NodeBst(value)
                return True
            return self.BSTAddInner(value, current.left)
        elif(currentTime < valueTime):
            if(not current.right):
                current.right = NodeBst(value)
                return True
            return self.BSTAddInner(value, current.right)
        else:
            return False


    """
    Nombre: getValue
    Parametros:
                value: objeto Movie al que se quiere extraer su contenido para visualizar en el árbol.
    Descripcion: Obtiene el contenido que se desea visualizar en el árbol.
    Retrorna: Retorna un String si se encontro el valor deseado, False en caso contrario.
    """
    def getValue(self, value):
        if(isinstance(value, Movie)):
            if(len(value.nameMovie)>20):
                conten = "%s |\n%s"%(value.timeMovie, value.nameMovie)
            else:
                conten = "%s | %s"%(value.timeMovie, value.nameMovie)
 
            return conten
        return False
    """
    Nombre: BSTADToLinkedList
    Parametros: 
                ll: LinkedList con todos los elementos del catalogo.
    Descripcion: Agrega los elementos de una lista enlazada a un arbol.
    Retorno: Retorna True

    """
    def BSTAddFromLinkedList(self,ll = LinkedList()):
        if(isinstance(ll,LinkedList)):
            current = ll.first
            while(current):
                value = current.value
                self.BSTAdd(value)
                current = current.next
            return True
    """
    Nombre: BSTConvert
    Parametros: 
                ll: LinkedList con todos los elementos del catalogo.
    Descripcion: Convierte los elementos de una lista enlazada a un árbol.
    Retorno: Retorna Un TDA BST

    """
    def BSTConvert(self, ll = LinkedList()):
        current = ll.first
        if(not current):
            return False
        tree = BST()
        rootNode = self.getValue(current.value)
        tree.g.add_node(rootNode)
        while(current):
            value = current.value
            tree.BSTAdd(value)
            current = current.next
        return tree

    
    """
    Nombre: BSTSearch
    Parametros: 
                value: Valor que se desea encontrar.
    Descripcion: Llama a la funcion BSTSearchInner para que busque desde la raiz.
    Retorno: Retorna el llamado a la funcion BSTSearchInner
    """
    def BSTSearch(self, value):
        return self.BSTSearchInner(value, self.root)

    """
    Nombre: BSTSearchInner
    Parametros: 
                value: Valor que se desea encontrar.
                Current: La raiz actul donde se esta buscando.
    Descripcion: Realiza un recorrido  en profundidad de manera recursiva hasta encontrar el valor que se desea obtener.
    Retorno: Retorna un Booleano.

    """
    def BSTSearchInner(self, value, current):
        if(isinstance(current, NodeBst)):
            if(not self.root):
                return False
            if(current.value == value):
                return True
            if(current.value> value):
                if(not current.left):
                    return False
                return self.BSTSearch(value,current.left)
            if(current.value < value):
                if(not current.right):
                    return False
                return self.BSTSearch(value, current.right)
            return False
        return False

    """
    Nombre: AddToG
    parametros: 
                current: Nodo actual, por defecto comienza desde la raiz.
    Descripcion: Agrega Nodos y aristas al Grapho de networkX
    Retorno: No retorna Nada.

    """
    def AddToG(self, current):
        if not current:
            return False
        else:
            currentValue = self.getValue(current.value)
            self.g.add_node(currentValue)
            if(current.left):
                leftCurrentValue = self.getValue(current.left.value)
                self.g.add_edge(currentValue,leftCurrentValue)
            if(current.right):
                rightCurrentValue = self.getValue(current.right.value)
                self.g.add_edge(currentValue,rightCurrentValue)
            self.AddToG(current.left)
            self.AddToG(current.right)

    """
    Nombre: getGraph
    Parametros:  No recibe parametros.
    Descripcion: Obtiene el grapho de networkx
    Retorno: Retorna el grapho de networkX
    """
    def getGraph(self):
        return self.g

    """
    Nombre:getRoot
    Parametros: No recibe parametros.
    Retorno: Retorna la raiz.
    """
    def getRoot(self):
        return self.root

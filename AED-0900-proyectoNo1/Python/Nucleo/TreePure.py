from Nucleo.NodeN import *
from Nucleo.Movie import *
from Nucleo.LinkedList import *
import networkx as nx
#from networkx.drawing.nx_agraph import graphviz_layout
import matplotlib.pyplot as plt

"""
Nombre: TreePure
Atributos:
    self.root: Es la raiz, por defecto es un Nodo que contiene el nodo Padre
    self.g: es una instancia de la libreria networkx que permite graficar el arbol.
Descripcion: Este es el TDA TreePure que permite gestionar un arbol jerarquico de n Nodos.
"""
class TreePure:
    def __init__(self):
        self.root = NodeN("Categorias")
        self.g = nx.Graph()
        
    """
    Nombre: add
    Parametros: parent, value
                parent: Nombre del padre a donde se desea agregar el valor.
                value: valor que se desea agregar al árbol.
    Descripcion: 
            Si el objeto que se desea agregar es un Movie se extrae su valor y se agrega en el segundo nivel del árbol.
            De lo contrario se agregara como hijo de la raiz.
    Retorno: retorna un boleano.

    """
    def add(self,parent, value):
        if(isinstance(value, Movie)):
            category = value.categoryMovie
            value = value.nameMovie
        if(self.root.value== parent):
            self.root.children.push(NodeN(value))
            return True
        current = self.root.children.first
        while(current):
            if(current.value.value ==parent):
                current.value.children.push(NodeN(value))
                return True
            current = current.next
        return False


    """
    Nombre: generateGraph
    Parametros: No recibe parametros.
    Descripcion: Agrega nodos y aristas a la instancia de grafo de networkx.
    Retorno: Retorna un boleano.
    """

    def generateGraph(self):
        currentParent = self.root.children.first
        if(self.root.children.first.value.children.first):
            self.g.add_node(self.root.value)
        while(currentParent):
            grandchild = currentParent.value.children.first
            while(grandchild):
                parent = currentParent.value.value
                children = grandchild.value.value
                self.g.add_node(parent)
                self.g.add_edge(self.root.value, parent)
                self.g.add_node(children)
                self.g.add_edge(parent,children)
                grandchild = grandchild.next
            currentParent = currentParent.next
        return True


    """
    Nombre: validate
    Parametros: No recibe parametros.
    Descripcion: Comprueba si hay elementos como hijos de categorias.
    Retorno: Retorna True en caso de que las categorias tengan hijos, False en caso contrario

    """
    def validate(self):
        current = self.root.children.first
        if(current):
            currentParent = current.value.children.first
            if(current):
                return True
        return False


    

    """
    Nombre: getGraphN
    Parametros: No recibe parametros.
    Descripcion: 
    Retorno: retorna la instancia de grapho de networkx
    """
    def getGraphN(self):
        return self.g
        
        


            
    
        

    
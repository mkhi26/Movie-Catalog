#-*-coding:utf-8 -*-
from Nucleo.LinkedListTree import *

"""
Nombre: NodeN
Constructor:
            Parametros: 
                value: Valor del Nodo.
    self. value: valor que tendra el Nodo.
    self.children: Hijos que tendra el Arbol de n nodos, es una Lista Enlazada( LinkedList)
Descripcion: Es el Nodo que complementara al árbol De n Nodos.
"""
class NodeN:
    def __init__(self, value=None):
        self.value = value
        self.children = LinkedListTree()
        
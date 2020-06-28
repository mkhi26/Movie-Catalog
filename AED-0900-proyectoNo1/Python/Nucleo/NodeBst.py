#-*-coding:utf-8 -*-
"""
Nombre: NodeBst
Constructor:
            Parametros: 
                value: Valor del Nodo.
    self. value: valor que tendra el Nodo.
    self.left: Hijo izquierdo.
    self.right: Hijo derecho.
Descripcion: Es el Nodo que complementara al árbol binario.
"""
class NodeBst:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
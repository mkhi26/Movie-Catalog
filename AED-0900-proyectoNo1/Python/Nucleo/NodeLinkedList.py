#-*-coding:utf-8 -*-
"""
Nombre: Node
Constructor:
            Parametros: 
                value: Valor del Nodo.
    self. value: valor que tendra el Nodo.
    self.next: Es None por defecto.
Descripcion: Es el Nodo que complementara la lista enlazada (LinkedList)
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
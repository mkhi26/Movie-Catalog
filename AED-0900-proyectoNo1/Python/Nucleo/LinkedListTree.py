#-*-coding:utf-8 -*-
from Nucleo.NodeLinkedList import *
from Nucleo.NodeN import *
from Nucleo.Compare import *


class LinkedListTree:

    def __init__(self):
        self.first = None

    """
    Nombre: push
    Parametros: 
                value: Valor que se desea agregar.
                position: Posición en la que se desea agregar, si este atributo no es asignado entonces
                          se agregara el elemento en la ultima posición.
    Descripcion: Agrega elementos a la lista enlazada segun la posicion en la que se desea agregar.
    Reorno: Retorna True si el elemento se agrego correctamente, False en caso contrario.
    """
    def push(self, value):
        if not self.first:
            self.first = Node(value)
            return True

        current = self.first
        compare = Compare()

        if(compare.compare(value, current) < 0):
            self.first = Node(value)
            self.first.next = current
            return True

        elif(compare.compare(value, current) > 0):
            before = current
            current = before.next
            while(current):
                if(compare.compare(value, current) < 0):
                    before.next = Node(value)
                    before.next.next = current
                    return True
                elif(compare.compare(value, current) > 0):
                    before = current
                    current = before.next
                else:
                    pass
            before.next = Node(value)
            return True
        else:
            pass
                      
    """
    Nombre: search
    Parametros: 
                index: Posición del elemento que se desea buscar.
    Descripción: Busca un elemento según la posición que recibe como parametro.
    Retorno: Retorna un booleano.
                True: Si el elemento existe en la lista.
                False: Si el elemento no existe en la lista.
    """
    def search(self, index):
        if(not self.first):
            return False
        current = self.first
        count = 0
        while(current):
            if(count == index):
                return True
            current = current.next
            count+=1
        return False
    
    """
    Nombre: pop
    Parametros: 
                position: Es la posicion del elemento que se desea eliminar.
    Descripcion: Elimina un elemento de la lista segun la posicion.
    Retorno: Si el elemento existe segun su posicion, entonces retorna el elemento eliminado, 
             False en caso contrario.
    """

    def pop(self, index):
        if(not self.first):
            return False
        else:
            if(index == 0):
                current = self.first
                self.first = self.first.next
                return current.value
            else:
                prevLast = self.first
                last = self.first.next
                count = 1
                while(last):
                    if(count == index):
                        prevLast.next = last.next
                        return last.value
                    prevLast = last
                    last = prevLast.next
                    count+=1
                return False
    """
    Nombre: lenght
    Parametros: No recibe parametros.
    Descripcion: Cuenta la cantidad de elementos que hay en la lista.
    Retorno: Retorna el tamaño de la lista.
    """
    def length(self):
        if(not self.first):
            return 0
        count = 1
        current = self.first
        while(current.next):
            count +=1
            current = current.next
        return count

    def print(self):
        current = self.first
        txt= ""
        while(current):
            txt+= current.value.value
            txt+= "->"
            current = current.next
        txt+= "null"
        return txt
        
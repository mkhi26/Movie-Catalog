#-*-coding:utf-8 -*-
from Nucleo.NodeLinkedList import *

class LinkedList:
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
    def push(self, value, position = None):
        if(not position):
            position = self.length()+1
        if(not isinstance(position, int) or position <0):
            return False
        if(not self.first):
            self.first = Node(value)
            return True
        count = 0
        current = self.first
        if(count== position):
            queue = self.first
            self.first= Node(value)
            self.first.next = queue
            return True
        before = self.first
        current = self.first.next
        while(current):
            count +=1
            if(count == position):
                before.next = Node(value)
                before.next.next = current
                return True
            before = current
            current = current.next
        before.next= Node(value)
        return True

    """
    Nombre: getElementFromIndex
    Parametros: Recibe la posición del objeto a buscar.
    Descripción: Este metodo permite encontrar un elemento segun su posicion en la lista.
    Retorno: Retorna el elemento de la lista que fue encontrado, en caso de no encontrarlo retornara False.
    """
    def getElementFromIndex(self,index):
        if(isinstance(index,int)):
            if(not self.first):
                return False
            current = self.first
            count = 0
            while(current):
                if(index == count):
                    return current.value
                current = current.next
                count +=1
        return False


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
    Nombre: remplace
    Parametros: 
                Index: Este parametro es la posicion del objeto que se quiere remplazar.
                objAdd: Es el nuevo objeto que remplazara al viejo.
    Descripción: Este método remplaza un objeto existente dentro de la lista.
    Retorno: Retorna True en caso de que se realice con éxito la operación, False en caso contrario.
    """
    def replace(self, index, objAdd):
        if(isinstance(index, int)):
            if(not self.first):
                return False
            current = self.first
            count = 0
            while(current):
                if(count == index):
                    current.value = objAdd
                    return True
                current = current.next
                count +=1
            return False
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
        
    """
    Nombre: print
    Parametros: No recibe parametros.
    Descripcion:  Imprime los elementos en la lista.
    Retorno: Retorna un String.
    """
    def print(self):
        txt = ""
        current = self.first
        while(current):
            txt += "%s %s" %(current.value, "->")
            current= current.next
        txt += "null"
        return txt

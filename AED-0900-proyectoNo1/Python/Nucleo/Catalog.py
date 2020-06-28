#-*-coding:utf-8 -*-
from Nucleo.LinkedList import *
from Nucleo.Movie import *
from Nucleo.BST import *
from Nucleo.TreePure import *
from Nucleo.NodeN import *
from Nucleo.TreePure import *
import matplotlib.pyplot as plt
try:
    import networkx as nx
except:
    print("Networkx no esta instalado.")
"""
Nombre: Catalog
Atributos:
            self.listMovie: Es la lista enlazada que contiene las peliculas agregadas al catalogo.
            self.tree : Es el arbol binario que contiene las peliculas agregdas en el catalogo.
            self.treeN : Es el árbol de n nodos, contiene la jerarquia segun la categoria de la pelicula.
Descripcion: Es el TDA que gestiona las peliculas agregadas a la lista enlazada.

"""
class Catalog:
    def __init__(self):
        self.listMovie = LinkedList()
        self.tree = BST()
        self.treeN = TreePure()

    
    """
    Nombre addMovie
    Parametros: Recibe un objeto Movie.
    Descripcion: Agrega peliculas a la lista Enlazada.
    Retorno: Retorna True si el objeto a ingresar es un objeto Movie, False en caso contrario.
    
    """
    def addMovie(self,movie):
        if(isinstance(movie,Movie)):
            self.listMovie.push(movie)
            self.tree=BST()
            self.tree=self.tree.BSTConvert(self.listMovie)
            self.tree.AddToG(self.tree.root)
            self.viewTree()
            self.viewTreeN()
            return True
        return False

    """
    Nombre: addCatalogToTreeN
    Parametros: No recibe parametros.
    Descripcion: Agrega las categorias de peliculas y  los elementos de la lista de este catalogo
                 al árbol de n nodos.
    Retorno: Retorna un boleano.
    """
    def addCatalogToTreeN(self):
        self.setCategoryTree()
        current = self.listMovie.first
        while(current):
            parent = current.value.categoryMovie
            self.treeN.add(parent,current.value)
            current = current.next
        return True


    """
    Nombre: viewTreeN
    Parametros: No recibe parametros.
    Descripcion: Genera una imagen en formato png con la reprecentacion del árbol jerarquico.
    Retorno: Retorna un boleano.
    """
    def viewTreeN(self):
        self.addCatalogToTreeN()
        try:
            self.treeN.generateGraph()
            G = self.treeN.getGraphN()
            nx.nx_agraph.write_dot(G,"Nucleo/treeN.dot")
            A = nx.nx_agraph.to_agraph(G)
            A.layout('dot',args='-Nfontsize=14  -Nwidth=".5" -Nheight=".5" -Nmargin=0 -Gfontsize=36')
            A.draw('Nucleo/treeN.png')
        except ValueError:
            print("Error")
            
        return True
        
    """
    Nombre: setCategoryTree
    Parametros: No recibe parametros.
    Descripcion: Agrega las categorías de peliculas al árbol jerárquico
    Retorno: Retorna True.
    """
    def setCategoryTree(self):
        self.treeN = TreePure()
        self.treeN.add("Categorias","Acción")
        self.treeN.add("Categorias","Artes marciales")
        self.treeN.add("Categorias","Aventuras") 
        self.treeN.add("Categorias","Bélicas")
        self.treeN.add("Categorias","Comedia")
        self.treeN.add("Categorias","Comedias musicales")
        self.treeN.add("Categorias","Ciencia ficción")
        self.treeN.add("Categorias","Deportivas")
        self.treeN.add("Categorias","Dibujos Animados")
        self.treeN.add("Categorias","Documental")
        self.treeN.add("Categorias","Dramáticas")
        self.treeN.add("Categorias","Espada y hechicería")
        self.treeN.add("Categorias","Espionaje")
        self.treeN.add("Categorias","Fantásticas")
        self.treeN.add("Categorias","Hechos reales")
        self.treeN.add("Categorias","Horror")
        self.treeN.add("Categorias","Infantiles")
        self.treeN.add("Categorias","Misterio")
        self.treeN.add("Categorias","Muertos vivientes")
        self.treeN.add("Categorias","Musicales")
        self.treeN.add("Categorias","Policíales")
        self.treeN.add("Categorias","Propaganda")
        self.treeN.add("Categorias","Psicológicas")
        self.treeN.add("Categorias","Suspenso")
        self.treeN.add("Categorias","Románticas")
        self.treeN.add("Categorias","Sobre Animales")
        self.treeN.add("Categorias","Sobre aviación")
        self.treeN.add("Categorias","Sobre delincuencia")
        self.treeN.add("Categorias","Sobre discapacitados")
        self.treeN.add("Categorias","Sobre religión")
        self.treeN.add("Categorias","Sobre política")
        return True

    """
    Nombre: viewTree
    Parametros: No recibe parametros.
    Descripcion: Genera una imagen en formato png con la reprecentacion del árbol Binario.
    Retorno: Retorna un boleano.
    """
    def viewTree(self):
        try:
            if(self.tree):
                G = self.tree.getGraph()
                nx.nx_agraph.write_dot(G,"Nucleo/tree.dot")
                A = nx.nx_agraph.to_agraph(G)
                A.layout('dot', args='-Nfontsize=14 -Nwidth=".5" -Nheight=".5" -Nmargin=0.1 -Gfontsize=36')
                A.draw('Nucleo/tree.png')
                return True
            return False
        except:
            print("Es necesario instalar pygraphviz")

    """
    Nombre: editMovie
    Parametros: 
                idEdit: Id del objeto que se quiere editar
                Movie: Objeto Movie que se quiere agregar como nuevo objeto.
    Descripción: Remplaza un objeto de la lista enlazada según su ID
    Retorno: Retorna True en caso de que el objeto nuevo sea un objeto Movie, False en caso contrario.
    """

    def editMovie(self, idEdit, movie):
        index = self.getIndex(idEdit)
        if(isinstance(movie, Movie)):
            self.listMovie.replace(index,movie)
            self.tree= self.tree.BSTConvert(self.listMovie)
            self.tree.AddToG((self.tree.root))
            self.viewTree()
            self.viewTreeN()
            return True
        return False

    """
    Nombre: deleteMovie
    Parametros:
                idRemove: Id del objeto que se desea eliminar.
    Descripcion: Elimina un elemento de la lista enlazada.
    Retorno: Retorna True

    """
    def deleteMovie(self, idRemove):
        index = self.getIndex(idRemove)
        self.listMovie.pop(index)
        self.tree= self.tree.BSTConvert(self.listMovie)
        try:
            self.tree.AddToG((self.tree.root))
            self.viewTree()
            self.viewTreeN()
        except:
            return False
        return True

    """
    Nombre: asignateId
    Parametros: 
                start: Por defecto esta inicializado en 0, es el inicio desde donde se quiere
                       encontrar una disponibilidad de ID
    Descripcion: Asigna un Id a un nuevo objeto que se quiera agregar a la lista.
    Retorno: retorna un Entero con el id encontrado.
    """
    def asignateId(self,start = 0):
        size = self.listMovie.length()
        obj = self.getMovieFromList(start)
        if(not obj):
            return start
        return self.asignateId(start+1)

    """
    Nombre: getIndex
    Parametros: 
                idSearch: Id del elemento al que se quiere obtener su posición den la lista.
    Descripción: Permite encontrar la posicion de un elemento seleccionado segun su ID.
    Retorno: Retorna su posicion si fue encontrado, False en caso contrario.
    """
    def getIndex(self, idSearch):
        size = self.listMovie.length()
        count = 0
        while(count != size):
            objMovie = self.listMovie.getElementFromIndex(count)
            if(isinstance(objMovie,Movie)):
                if(objMovie.idMovie== idSearch):
                    return count
                count+=1
        return -1


    """
    Nombre: getMovieFromList
    Parametros: 
                idMovie: Identificador del objeto que se quiere buscar.
    Descripcion: Se obtendra una pelicula del catalogo segun su posicion.
    Retorno: Retorna el objeto encontrado.

    """
    def getMovieFromList(self, idMovie):
        index = self.getIndex(idMovie)
        objMovie = self.listMovie.getElementFromIndex(index)
        return objMovie

    """
    Nombre: printCatalog
    Parametros: No recibe parametros.
    Descripcion: Genera un string con todos los valores agregados en el catalogo.
    Retorno: Retorna un String.

    """

    def printCatalog(self):
        txt=""
        size= self.listMovie.length()
        if(size==0):
            return "null"
        for i in range(size):
            objMovie = self.listMovie.getElementFromIndex(i)
            txt+="%s->"%(objMovie.nameMovie)
        txt+="null"
        return txt
    """
    Nombre: search
    Parametros: Recibe un Id para verificar su existencia en la lista.
    Descripcion: verifica si hay un id con el parametro recibido dentro de la lista.
    Retorno: retorna un boleano.
    """
    def search(self, idCheck):
        index = self.getIndex(idCheck)
        check=self.listMovie.search(index)
        return check


    """
    Nombre: getSize
    Parametros: No recibe parametros.
    Descripcion: Obtiene el tamaño de la lista de peliculas.
    Retorno: retorna un entero con el tamaño de la lista.
    """
    def getSize(self):
        size = self.listMovie.length()
        return size


    """
    Nombre: getMovieFromIndex
    Parametros: 
                index: pocision  en memoria del objeto a retornar.
    Descripción: Busca un objeto pelicula segun su posicion en memoria.
    Retorno: Retorna el objeto encontrado.
    """
    def getMovieFromIndex(self, index):
        movie = self.listMovie.getElementFromIndex(index)
        return movie

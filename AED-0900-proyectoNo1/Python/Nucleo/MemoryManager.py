#-*-coding:utf-8 -*-
from Nucleo.Catalog import *
import json

"""
Nombre: MemoryManager
Atributos: 
            self.memoryCatalog: Es un catalogo con la lista de peliculas.
            self.data: Es un Diccionario
Descripción: Es el TDA Memory Manager, mediante el TDA se puede gestionar la memoria permanente.

"""
class MemoryManager:
    def __init__(self):
        self.memoryCatalog = Catalog()
        self.data = {}

    """
    Nombre: getMovieFromCatalog
    Parametros: 
                catalog: Recibe un catalogo con la lista de películas.
    Descripción: Recorre la lista de catalogo y se obtiene el objeto Movie
                 para agregar el objeto Movie al diccionario.
    Retorno: True o False
    """
    def getMovieFromCatalog(self, catalog):
        if(isinstance(catalog, Catalog)):
            self.data.clear()
            size = catalog.getSize()
            for i in range(size):
                movie = catalog.getMovieFromIndex(i)
                self.generateDictMemory(movie, i)
            return True
        return False

    """
    Nombre: generateDictMemory
    Parametros: 
                movie: Recibe un objeto Movie
                index: recibe la posicion del objeto en la lista.
    Descripción: Agrega  objetos movie al diccionario, la clave del diccionario sera
                 asignada segun su ID.
    Retorno: Retorna True
    """
    def generateDictMemory(self, movie, index):
        dictMovie = self.generateDictMovie(movie)
        self.data[index]= dictMovie
        return True

    """
    Nombre: generateDictMovie
    Parametros: 
                movie: objeto Movie
    Descripcion: Recibe un objeto movie, se extraen sus valores y se agregan al diccionario
    Retorno: retorna un diccionario que incluye los datos del obj Movie.
    """
    def generateDictMovie(self, movie):
        dictMovie ={}
        dictMovie["name"] = movie.nameMovie
        dictMovie["time"] = movie.timeMovie
        dictMovie["description"] = movie.descriptionMovie
        dictMovie["director"]= movie.directorMovie
        dictMovie["category"] =movie.categoryMovie
        dictMovie["id"] = movie.idMovie
        return dictMovie


    """
    Nombre: generateJson
    Parametros: No recibe parametros.
    Descripción: crea un archivo .JSON en el disco duro.
    Retorno: Retorna True.
    """
    def generateJson(self,d={}):
        f = open('Nucleo/Memoria/memory.json', 'w', encoding= 'utf8')
        json.dump(self.data, f, indent=4)
        return True
    """
    Nombre: saveCatalog
    Parametros: 
                catalog: catalogo con la lista de peliculas.
    Descripción: Guarda el catalogo de peliculas en un archivo .JSON
    Retorno: Retorna True
    """
    def saveCatalog(self, catalog):
        self.getMovieFromCatalog(catalog)
        self.generateJson(self.data)
        return True

    """
    Nombre: getDicFromFile
    Parametros: No recibe parametros.
    Descripción: obtiene un diccionario desde un archivo .JSON
                 y lo guarda en la variable local 'self.data'
    Retorno: True
    """
    def getDicFromFile(self):
        try:
            with open('Nucleo/Memoria/memory.json') as file:
                self.data = json.load(file)
                file.close()
        except:
            return False
        return True
    """
    Nombre: getFromMemory
    Parametros: No recibe parametros.
    Descripción: recorre un diccionario segun su clave para posteriormente
                 llamar a la función getMovieFromDictionary.
    Retorno: Retorna True.
    """
    def getFromMemory(self):
        self.getDicFromFile()
        for key in self.data.keys():
            dicMovie = self.data[key]
            self.getMovieFromDictionary(dicMovie)
        return True
            

    """
    Nombre: getMovieFromDictionary
    Parametros: 
                dicMovie= Recibe un diccionario que contiene los datos de un 
                objMovie.
    Descripción: Obtiene los datos del diccionario para crear un objeto Movie
                 y posteriormente agregarlo al catalogo.
    Retorno: True o False.
    """
    def getMovieFromDictionary(self, dicMovie={}):
        if(isinstance(dicMovie,dict)):
            name = dicMovie["name"]
            time = dicMovie["time"]
            description = dicMovie["description"]
            director = dicMovie["director"]
            category = dicMovie["category"]
            idMovie =int(dicMovie["id"])
            movie = Movie(name,time,description,director,category,idMovie)
            self.memoryCatalog.addMovie(movie)
            return True
        return False

    """
    Nombre: getCatalogFromMemory
    Parametros: No recibe parametros.
    Descripcion: Mediante esta funcion se puede obtener la memoria permanente.
    Retorno: Retorna la memoria permanente.
    """
    def getCatalogFromMemory(self):
        return self.memoryCatalog


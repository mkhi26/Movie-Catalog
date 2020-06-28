#-*-coding:utf-8 -*-
from Nucleo.Catalog import *
from Nucleo.Movie import *
from Nucleo.TimeManager import *
"""
Nombre: TableAssci
Atributos:
    self.idMax: tamanio mas grande de las cadena ID
    self.nameMax: tamanio mas grande de las cadena name
    self.timeMax: tamanio mas grande de las cadena time
    self.descriptionMax: tamanio mas grande de las cadena descripción
    self.directorMax : tamanio mas grande de las cadena descripción   
    self.categoryMax: tamanio mas grande de las cadena de categorias.
    self.lenString: tamano total de la suma de todos los string que irán en una fila.

"""
class TableAsscii:
    def __init__(self):
        self.idMax=0
        self.nameMax=0
        self.timeMax=0
        self.descriptionMax=28
        self.directorMax=0
        self.categoryMax=0
        self.lenString = 0

    """
    Nombre: getMovie
    Parametro: 
                catalog: Catalogo que contiene todas las películas agregadas a la lista.
    Descripción: Recorre la lista para obtener el objeto Movie y posteriormente llama a la función getConten.
    Retorno: True o False.
    """
    def getMovie(self, catalog= Catalog()):
        if(isinstance(catalog,Catalog)):
            size = catalog.getSize()
            for i in range(size):
                movie = catalog.getMovieFromIndex(i)
                self.getContent(movie)
            return True
        return False


    """
    Nombre: getContent
    Parametros: 
                movie: Objeto Movie al que se desea extraer sus valores.
    Descripcion: Obtiene el contenido de un objeto Movie.
    Retorno: Retorna el contenido del objeto.
    """
    def getConten(self, movie=Movie()):
        name = movie.nameMovie
        idMovie = str(movie.idMovie)
        time = movie.timeMovie
        description = movie.descriptionMovie
        director = movie.directorMovie
        category = movie.categoryMovie
        return [idMovie,name , time, description, director, category]

    """
    Nombre: getDataString
    Parametros:
                catalog: Catalogo de peliculas
    Descripcion: Esta funcion obtiene los datos de todos los objetos de la lista del catalogo y los
                almacena en un vector(list).
    Retorno: Retorna un vector (List)

    """
    def getDataString(self, catalog = Catalog()):
        timeManager = TimeManager()
        size = catalog.getSize()
        vector= []
        for i in range(size):
            movie = catalog.getMovieFromIndex(i)
            idMovie,name , formate, description, director, category = self.getConten(movie)
            time = timeManager.convertTimeToSeconds(formate)
            if(len(description)>29):
                description= description[0:29]
                description+="..."
            if(len(name)>37):
                name = name[0:37]
                name+="..."
            time = "%s%s"%(time," seg.")
            spaceId, spaceName, spaceTime, spaceDescription, spaceDirector, spaceCategory = self.getSpaces(movie)
            data="%s%s\t|  %s%s\t|  %s%s|%s%s\t|  %s%s\t|  %s%s\t  " %(idMovie," "*spaceId,name," "*spaceName,time," "*spaceTime,description," "*spaceDescription, category," "*spaceCategory,director," "*spaceDirector)
            vector.append(data)
            if(i ==0):                                     
                self.lenString = len(data) +60

        return vector


    """
    Nombre: createTable
    Parametros: 
            catalog: Catalogo de peliculas.
    Descripcion: Crea una tabla ASCII con los elementos del catalogo.
    Retorno: Retorna un string con la tabla.
    """
    def createTable(self, catalog = Catalog()):
        size = catalog.getSize()
        if(size == 0):
            self.lenString = 200
            
            return self.getheader()
        self.getStringMax(catalog)
        
        listData = self.getDataString(catalog)
        header = self.getheader()
        row = "-"*self.lenString
        conten=""
        listConten =[]
        listConten.append(header)
        for i in range(len(listData)):
            conten+=listData[i]+"\n"
            conten+=row+"\n"
            listConten.append(conten)
        table = header + conten
        return  table


    """
    Nombre: getSpaces
    Parametros: 
        movie: objeto Movie.
    Descripcion: Obtiene los tamaños de las cadenas de todos los atributos del objeto
                 y los resta con los tamaños maximos para obtener el total de espacios
                 con los que se imprimira en la tabla.
    Retorno: Retorna una lista con todos los espacios de este objeto.
    """
    def getSpaces(self, movie):
        if(isinstance(movie, Movie)):
            timeManager = TimeManager()
            idMovie,name , time, description, director, category = self.getConten(movie)
            time= str(timeManager.convertTimeToSeconds(time))
            spaceId = self.idMax - len(idMovie)
            spaceName = 32 - len(name)
            spaceTime = self.timeMax - len(time)
            spaceDescription = 32- len(description)
            spaceDirector = self.directorMax - len(director)
            spaceCategory = 20 - len(category)
            return spaceId, spaceName+4, spaceTime+4, spaceDescription, spaceDirector+4, spaceCategory+4


    """
    Nombre: getStringMax
    Parametros: 
                catalog: objeto Catalogo con la lista de las películas agregadas.
    Descripción: Obtiene las cadenas de texto mas grande dentro de los atributos del objeto Movie
    Retorno: Retorna enteros con los valores máximos de las cadenas de texto del objeto Movie.
    """  
    def getStringMax(self, catalog= Catalog()):
        size = catalog.getSize()
        idMax = 0
        nameMax= 0
        timeMax= 0
        descriptionMax= 0
        directorMax= 0
        categoryMax= 0
        self.cleanMax()
        for i in range(size):
            timeManager = TimeManager()
            movie = catalog.getMovieFromIndex(i)
            idMovie,name,time, description, director, category = self.getConten(movie)
            time =str(timeManager.convertTimeToSeconds(time))
            if(len(name)>self.nameMax):
                self.nameMax = len(name)
            if(len(idMovie)> self.idMax):
                self.idMax= 4
            if(len(time)> self.timeMax):
                self.timeMax = len(time)
            if(len(description)> self.descriptionMax):
                self.descriptionMax = 32
            if(len(director)> self.directorMax):
                self.directorMax = len(director)
            if(len(category)> self.categoryMax):
                self.categoryMax = len(category)
        return True

    """
    Nombre: cleanMax
    Parametro: No recibe parametros
    Descripcion: Iguala a  los maximos en el construtor.
    Retorno: Retorna True
    """
    def cleanMax(self):
        self.idMax =0
        self.nameMax =0
        self.categoryMax = 0
        self.directorMax = 0
        self.timeMax =0
        self.descriptionMax =0
        return True


    """
    Nombre: getheader
    Parametros: No recibe parametros.
    Descripcion: Genera el encabezado de la tabla con los espacios correspondientes en la separacion de cada 
                 columna de la tabla.
    Retorno: Retorna un String con los elementos de encabezado.
    """
    def getheader(self):
    
        movie = Movie("|Nombre", "| Duración","| Descripción","| Director","| Categoria",110)
        spaceId, spaceName, spaceTime, spaceDescription, spaceDirector, spaceCategory = self.getSpaces(movie)
        spaceTime=6
        conten="%s%s\t%s%s\t%s%s%s%s%s%s%s%s\t" %("ID"," "*spaceId,"|Nombre"," "*spaceName,"|Duración"," "*spaceTime,"|Descripción"," "*(31-len("Descripción")), "\t|Categoría"," "*spaceCategory,"\t|Director"," "*spaceDirector)
        spaces = " "*int(self.lenString/4)
        title = "Inventario de Películas"
        row = "-"*self.lenString
        header = "%s%s%s%s%s"%(row,"\n",spaces,title,spaces)
        txt= "%s%s%s%s%s%s%s%s"%(header,"\n",row,"\n",conten,"\n",row,"\n")
        return txt



        

        
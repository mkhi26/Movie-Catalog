#-*-coding:utf-8 -*-
""" 
    TDA Movie
    Nombre: Movie
    Atributos: 
        name: Nombre de la pelicula.
        time: tiempo de duracion de la pelicula en formato 'HH:MM:SS'.
        description: Objeto pelicula.
    Descripcion: Este es el TDA Movie.

"""
class Movie:
    def __init__(self, name="", time="", description="",director="",category="",idMovie=0):
        self.nameMovie = name
        self.timeMovie = time
        self.descriptionMovie = description
        self.directorMovie = director
        self.categoryMovie = category
        self.idMovie = idMovie
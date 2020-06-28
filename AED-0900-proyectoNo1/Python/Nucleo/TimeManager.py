#-*-coding:utf-8 -*-
class TimeManager:
    def __init__(self):
        pass

    """
        Nombre: hoursToSecounds
        Parametros: Recibe el tiempo en Horas
        Descripcion: Convierte las horas a segundos.
        Retorno: Retorna el tiempo en segundos.

    """
    def hoursToSecounds(self, hours):
        m = int(hours * 60)
        s = self.minutesToSeconds(m)
        return s

    """
        Nombre: minutesToSeconds
        Parametros: Recibe como parametro el tiempo en minutos.
        Descripcion: Convierte los minutos a segundos.
        Retorno: Retorna el tiempo en segundos.
    """
    def minutesToSeconds(self, minutes):
        s = int(minutes * 60)
        return s
    """
        Nombre: verificateformate
        Parametros: Recibe un formateo de tiempo en un tipo de dato String.
        Descripcion: Esta funcion permite verificar si el formateo de tiempo recibido es valido.
        Retorno: Retorna True en caso de que el formateo sea valido, retornara False en caso contrario.
    """
    def verificateformate(self, formate):
        """
        Realiza un split del formateo que recibe como atributo para poder
                     separar las horas, minutos y segundos en un vector, de tal manera que el vector 
                     tendra un tamaño de 3 elementos, donde:
                        vector[0]: contiene las horas en un tipo de dato String.
                        vector[1]: contiene los minutos en un tipo de dato String.
                        vector[2]: contiene los segundos en un tipo de dato String.
        """
        vector = formate.split(":")
        if(len(vector)==3):
            try:
                vector[0]= int(vector[0])
                vector[1]= int(vector[1])
                vector[2]= int(vector[2])
                if(vector[1]>=60 or vector[2]>=60):
                    return False
                return True
            except:
                return False
        return False

    """
        Nombre: strigToInt
        Parametros: Recibe una lista como parametro.
        Descripción: Esta función hace un casteo de los elementos que están en String a Integer.
        Retorno: Retorna una lista, si el formateo de tiempo es valido, de lo contrario retornará False.
    """
    def strigToInt(self, formate):
        validate = self.verificateformate(formate)
        if(validate):
            vector = formate.split(":")
            for i in range(len(vector)):
                vector[i]= int(vector[i])
            return vector
        return False

    """
        Nombre: convertTimeToSeconds
        Parametros: Recibe un formateo de tiempo en un tipo de dato String.
        Descripcion: Esta funcion verifica que el formateo recibido como parametro sea valido, luego
                     si el formateo es valido entonces se convertira las horas, minutos a segundos y retornara
                     el tiempo sumado en segundos.

        Retorno: Retorna el tiempo total en segundos.

    """
    def convertTimeToSeconds(self, formate):
        validate = self.verificateformate(formate)
        if(validate):
            vector = self.strigToInt(formate)
            hoursToSecouns = self.hoursToSecounds(vector[0])
            minutesToSecounds= self.minutesToSeconds(vector[1])
            secounds = vector[2]
            time = int(hoursToSecouns + minutesToSecounds + secounds)
            return time
        return False

        


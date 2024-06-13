from Conjunto import conjunto

import csv

class manejador:
    __A = None
    __B = None
    __C = None
    def __init__(self, a = [1, 2, 3, 4, 5], b = [1, 6, 7], c = [2, 3, 4, 1, 5]): #prueba
        self.__A = conjunto(a)
        self.__B = conjunto(b)
        self.__C = conjunto(c)
    def punto1(self): #unión de conjuntos
        return self.__A + self.__B
    def punto2(self): #diferencia de conjuntos
        return self.__A - self.__B
    def punto3(self, band): #comparación de conjuntos
        resultado = None
        if(band == True):
            resultado = self.__A == self.__B
        else:
            resultado = self.__A == self.__C
        return resultado
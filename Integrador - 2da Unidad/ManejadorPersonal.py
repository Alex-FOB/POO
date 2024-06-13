import numpy as np

from Personal import personal

class manejadorP:
    __arreglo = None
    __dim = 0
    __i = 0
    def __init__(self):
        self.__dim = 0
        self.__i = 0
        self.__arreglo = np.empty(self.__dim, dtype = personal)
    def modDim(self, dim):
        self.__dim = dim
        self.__arreglo.resize(self.__dim)
    def addPersonal(self, personal):
        self.__arreglo[self.__i] = personal
        self.__i += 1
    def comparar(self, legajo):
        leg = str(legajo)
        band = False
        i = 0
        while not band and i < len(self.__arreglo):
            if(self.__arreglo[i].getLegajo() == leg):
                band = True
            i += 1
        return band
    def calcular(self, novedades):
        for personal in self.__arreglo:
            add = novedades.getAdd(personal.getLegajo())
            sub = novedades.getSub(personal.getLegajo())
            sueldo = personal.getSueldo() + add - sub
            personal.setCobrar(sueldo)
    def buscar(self, legajo):
        pos = -1
        band = False
        i = 0
        while not band and i < len(self.__arreglo):
            if(self.__arreglo[i].getLegajo() == legajo):
                pos = i
                band = True
            i += 1
        return pos
    def ordenar(self): #algoritmo Burbuja Mejorado NOTA:es el método de burbuja porque el mejorado lo ordena a medias
        cota = len(self.__arreglo) - 1
        k = 1
        while(k != -1):
            k = -1
            for i in range(cota):
                if(self.__arreglo[i] > self.__arreglo[i+1]):
                    aux = self.__arreglo[i]
                    self.__arreglo[i] = self.__arreglo[i+1]
                    self.__arreglo[i+1] = aux
                    k = i
            cota = k
    def minSueldo(self):
        min = 1000000000
        for personal in self.__arreglo:
            if(personal < min):
                min = personal.getCobrar()
        return min
    def getSueldo(self, pos):
        return self.__arreglo[pos].getCobrar()
    def mostrar(self, novedades):
        text = ''
        self.ordenar()
        for personal in self.__arreglo:
            text += '{}\n'.format(personal)
            text += 'Codigo      Concepto                 Importe\n'
            text += '{}\n'.format(novedades.getNovedades(personal.getLegajo()))
            text += 'Total a cobrar: ${}\n'.format(personal.getCobrar())
        return text
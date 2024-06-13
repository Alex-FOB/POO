class novedad:
    __legajo = None
    __imp = None
    __concepto = None
    __cod = None
    def __init__(self, legajo, imp, concepto, cod):
        self.__legajo = str(legajo)
        self.__imp = float(imp)
        self.__concepto = str(concepto)
        self.__cod = str(cod)
    def __str__(self):
        return '{:10} {:25} ${}'.format(self.__cod, self.__concepto, self.__imp)
    def getLegajo(self):
        return self.__legajo
    def getImp(self):
        return self.__imp
    def getCod(self):
        return self.__cod
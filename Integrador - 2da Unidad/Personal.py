class personal:
    __legajo = None
    __dni = None
    __ape = None #apellido
    __nom = None #nombre
    __sueldo = None #sueldo básico
    __cobrar = None #AÑADIDO
    def __init__(self, legajo, dni, ape, nom, sueldo):
        self.__legajo = str(legajo)
        self.__dni = str(dni)
        self.__ape = str(ape)
        self.__nom = str(nom)
        self.__sueldo = float(sueldo)
    def __str__(self):
        return 'Apellido: {:20} Nombre:{}\nDNI: {}\nSueldo Basico: ${}'.format(self.__ape, self.__nom, self.__dni, self.__sueldo)
    def __gt__(self, other):
        return self.__ape > other.getApe()
    def __lt__(self, other):
        return self.__cobrar < other
    def setCobrar(self, sueldo):
        self.__cobrar = sueldo
    def getLegajo(self):
        return self.__legajo
    def getSueldo(self):
        return self.__sueldo
    def getCobrar(self):
        return self.__cobrar
    def getApe(self):
        return self.__ape
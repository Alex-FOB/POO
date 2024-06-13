from Manejador import manejador

class interfaz:
    __funcion = None
    __op = None
    __manejador = None
    def __init__(self):
        self.__op = {1: self.punto1, 2: self.punto2, 3: self.punto3, 4: self.salir}
        self.__manejador = manejador()
    def opcion(self, op):
        self.__funcion = self.__op.get(op)
        if self.__funcion:
            self.__funcion()
        else:
            print('ERROR: opcion invalida')
    def punto1(self): #unión de conjuntos
        print('A + B = {}'.format(self.__manejador.punto1()))
        input()
    def punto2(self): #diferencia de conjuntos
        print('A - B = {}'.format(self.__manejador.punto2()))
        input()
    def punto3(self): #comparación de conjuntos
        print('A == B = {}\nA == C = {}'.format(self.__manejador.punto3(True), self.__manejador.punto3(False)))
        input()
    def salir(self):
        print('FINALIZANDO...')
        input()
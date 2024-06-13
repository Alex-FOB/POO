class menu:
    __op = None
    __personal = None
    __novedades = None
    def __init__(self, personal, novedades):
        self.__op = {1: self.punto1, 2: self.punto2, 3: self.punto3, 4: self.salir}
        self.__personal = personal
        self.__novedades = novedades
        #-----------------------------------------------------------
        self.__personal.calcular(self.__novedades)
    def opcion(self, op):
        funcion = self.__op.get(op)
        if funcion:
            funcion()
        else:
            print('ERROR: opcion invalida')
            input()
    def punto1(self):
        legajo = str(input('Ingrese numero de legajo: '))
        pos = self.__personal.buscar(legajo)
        if(pos != -1):
            print('Sueldo a liquidar: ${}'.format(self.__personal.getSueldo(pos)))
        else:
            print('ERROR: personal no encontrado')
        input()
    def punto2(self):
        print(self.__personal.mostrar(self.__novedades))
        input()
    def punto3(self):
        print('Sueldo minimo a cobrar: ${}'.format(self.__personal.minSueldo()))
        input()
    def error(self):
        print('ERROR: valor invalido')
        input()
    def salir(self):
        print('FINALIZANDO...')
        input()
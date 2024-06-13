class manejadorN:
    __lista = None
    def __init__(self):
        self.__lista = []
    def addNovedad(self, novedad):
        self.__lista.append(novedad)
    def getAdd(self, legajo):
        acum = 0
        for novedad in self.__lista:
            if(novedad.getLegajo() == legajo and novedad.getCod().lower() == 'a'):
                acum += novedad.getImp()
        return acum
    def getSub(self, legajo):
        acum = 0
        for novedad in self.__lista:
            if(novedad.getLegajo() == legajo and novedad.getCod().lower() == 'd'):
                acum += novedad.getImp()
        return acum
    def getNovedades(self, legajo):
        text = ''
        for novedad in self.__lista:
            if(novedad.getLegajo() == legajo):
                text += '{}\n'.format(novedad)
        return text
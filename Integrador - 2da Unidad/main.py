import csv

from Menu import menu

from Personal import personal

from Novedad import novedad

from ManejadorPersonal import manejadorP

from ManejadorNovedades import manejadorN

def readPersonal():
    manejador = manejadorP()
    band = False
    i = 0
    with open('personal.csv') as archi:
        reader = csv.reader(archi, delimiter = ';')
        for fila in reader:
            if(band == False):
                band = True
            else:
                unPersonal = personal(fila[0], fila[1], fila[2], fila[3], fila[4])
                i += 1
                manejador.modDim(i)
                manejador.addPersonal(unPersonal)
    archi.close()
    return manejador
def readNovedades(mPersonal):
    manejador = manejadorN()
    band = False
    with open('novedades.csv') as archi:
        reader = csv.reader(archi, delimiter = ';')
        for fila in reader:
            if(band == False):
                band = True
            else:
                if(mPersonal.comparar(fila[0])): #compara la novedad con los personales
                    unaNovedad = novedad(fila[0], fila[1], fila[2], fila[3])
                    manejador.addNovedad(unaNovedad)
    archi.close()
    return manejador
if __name__ == '__main__':
    mPersonal = readPersonal()
    mNovedades = readNovedades(mPersonal)
    interfaz = menu(mPersonal, mNovedades)
    band = False
    while not band:
        print('1.- Sueldo a liquidar del personal\n2.- Listar personal\n3.- Sueldo del personal mas bajo\n4.- Salir')
        try:
            op = int(input('Opcion: '))
            interfaz.opcion(op)
            band = op == 4
        except ValueError:
            interfaz.error()
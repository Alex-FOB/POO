from Menu import interfaz

from Conjunto import conjunto

def test():
    A = [1, 2, 3, 4, 5]
    unConjunto = conjunto(A)
    print(unConjunto)
if __name__ == '__main__':
    if(str(input('¿Desea testear? ')).lower() == 'si'):
        test()
    else:
        menu = interfaz()
        band = False
        while not band:
            print('1.- A + B\n2.- A - B\n3.- A == ?\n4.- Salir')
            op = int(input('Opcion: '))
            menu.opcion(op)
            band = op == 4
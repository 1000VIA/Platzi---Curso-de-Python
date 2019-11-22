# -*- coding: utf-8 -*-
def is_genero(genero, edad):
    if edad >= 18 and genero == 'M':
        return 'M'
    if edad >= 18 and genero == 'F':
        return 'F'
    if edad < 18 and genero == 'M':
        return 'Niño'
    if edad < 18 and genero == 'F':
        return 'Niña'


def run():
    genero = str(input('¿Cuál es su género?: '))
    edad = int(input('¿Ingrese su edad: '))
    result = is_genero(genero, edad)

    if result == 'M':
        print('Hola, señor')
    elif result == 'Niño':
        print('Hola niño')
    if result == 'F':
        print('Hola, señora')
    elif result == 'Niña':
        print('Hola, niña')


if __name__ == "__main__":
    run()

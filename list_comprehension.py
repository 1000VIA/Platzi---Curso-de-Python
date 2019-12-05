pares = []


def run():
    print(' ')
    print('Ejemplo -> Dictionary comprehension')
    for num in range(1, 31):
        if num % 2 == 0:
            pares.append(num)
    print('Los numeros pares son: {}'.format(pares))

    print(' ')
    print('Ejemplo -> list comprehension')
    even = [num for num in range(1, 31) if num % 2 == 0]
    print('Los numeros pares son: {}'.format(pares))

    print(' ')
    print('Ejemplo Cuadrados -> list comprehension:')
    cuadrados = {}
    for num in range(1, 11):
        cuadrados[num] = num ** 2
    print('Los numeros pares son: {}'.format(cuadrados))

    print(' ')
    print('Ejemplo Cuadrados -> Dictionary comprehension:')
    # se declara la llave antes de los dos puntos y el valor despues de los dos puntos.
    squares = {num: num ** 2 for num in range(1, 11)}
    print('Los numeros pares son: {}'.format(squares))


if __name__ == "__main__":
    run()

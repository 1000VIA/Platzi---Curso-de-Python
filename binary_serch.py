# numbers: lista de números
# number_to_find: número a encontrar
# low: indice más bajo
# high: indice más alto


def run():
    numbers = [1, 2, 3, 4, 5, 6, 9, 10, 11, 25, 27, 28, 34, 36, 49, 51]

    number_to_find = int(input('Ingresa un número: '))

    result = binary_search(numbers, number_to_find, 0, len(numbers) - 1)

    if result is True:
        print('El nímero sí está en la lista. ')
    else:
        print('El número no está en la lista')


def binary_search(numbers, number_to_find, low, high):

    if low > high:
        return False

    # Cuando se hace una división hay que poner doble //
    mid = (low + high) // 2

    if numbers[mid] == number_to_find:
        return True
    elif numbers[mid] > number_to_find:
        return binary_search(numbers, number_to_find, low, mid - 1)
    else:
        return binary_search(numbers, number_to_find, mid + 1, high)


if __name__ == "__main__":
    run()

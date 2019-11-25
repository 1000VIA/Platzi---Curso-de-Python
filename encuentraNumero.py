import random


def run():
    number_found = False
    random_number = random.randint(0, 20)

    while not number_found:
        number = int(input('Escribe un número: '))

        if number == random_number:
            print('wooo, encontraste el numero! ')
            number_found = True
        elif number > random_number:
            print('El número debe ser de menor valor')
        else:
            print('El número debe ser mayor')


if __name__ == '__main__':
    run()

# import lamp
from lamp import Lamp


def run():
    lamp = Lamp(is_turned_on=False)

    while True:
        command = str(input('''
        ¿Que deseas hacer?

        [p]render
        [a]pagar
        [s]alir
        '''))

        if command == 'p':
            lamp.turn_on()
        elif command == 'a':
            lamp.turn_off()
        else:
            break


if __name__ == '__main__':
    run()

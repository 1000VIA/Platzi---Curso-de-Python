class Contac: #Contenedor de variables

    def __init__(self, name, phone, email):
        self._name = name
        self._phone = phone
        self._email = email


class ContactBook:

    def __init__(self):
        self._contacts = []

    def add(self, name, phone, email):
        print('name: {}, phone: {}, email: {}'.format(name, phone, email))

def run():

    contact_book = ContactBook()

    while True:
        command = str(input('''
            ¿Qué deseas hacer?

            [a]ñadir contacto
            [ac]tualizar contacto
            [b]uscar contacto
            [e]liminar contacto
            [l]istar contactos
            [s]alir
        '''))

        if command == 'a':
            name = str(input('Escribe el nombre del contacto: '))
            phone = str(input('Escribe el teléfono del contacto: '))
            email = str(input('Escribe el email del contacto: '))

            contact_book.add(name, phone, email)

        elif command == 'ac':
            print('actualizar contacto')

        elif command == 'b':
            print('buscar contacto')

        elif command == 'e':
            print('eliminar contacto')

        elif command == 'l':
            print('listar contactos')

        elif command == 's':
            break
        else:
            print('Comando no encontrado.')


if __name__ == '__main__':
    print('B I E N V E N I D O  A  L A  A G E N D A')
    run()
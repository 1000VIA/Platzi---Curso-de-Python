class Contact: #Contenedor de variables

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email


class ContactBook:

    def __init__(self):
        self._contacts = []

    def add(self, name, phone, email):
        contact = Contact(name, phone, email)
        self._contacts.append(contact)#Guardar contacto dentro de nuestra lista de contactos
        #print('name: {}, phone: {}, email: {}'.format(name, phone, email))

    def show_all(self):
        for contact in self._contacts:
            self._print_contact(contact)

    def delete(self, name):
        for idx, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                del self._contacts[idx]
                break
    def search(self, name):
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                self._print_contact(contact)
                break
        else:
            self._not_found()
    
    def update(self, name, phone, email):
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                contact.phone = phone
                contact.email = email
                break
        else:
            self._not_found()

    
    def find(self, name):
        for idx, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                return idx
        else:
            return-1

    def update(self, idx, name, phone, email):
        newContact = Contact(name, phone, email)
        self._contacts[idx] = newContact
        print('Contacto actualizado')
        print('*---*---*---*---*---*---*---*---*')

    def _print_contact(self, contact): #los metodos de instancia siempre empiesan con self
        print('*---*---*---*---*---*---*---*---*')
        print('Nombre: {}'.format(contact.name))
        print('Teléfono: {}'.format(contact.phone))
        print('Email: {}'.format(contact.email))
        print('*---*---*---*---*---*---*---*---*')

    def _not_found(self):
        print('*********')
        print('¡No encontrado!')
        print('*********')


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
            name = str(input('Escribe el nombre del contacto a actualizar: '))
            idx = contact_book.find(name)
            if idx>=0:
                name = str(input('Escribe el nuevo nombre del contacto: '))
                phone = str(input('Escribe el telefono del contacto: '))
                email = str(input('Escribe el email del contacto: '))
                contact_book.update(idx, name, phone, email)
            else:
                print('No encontrado')

        elif command == 'b':
            name = str(input('Escribe el nombre del contacto a buscar: '))

            contact_book.search(name)

        elif command == 'e':
            name = str(input('Escribe el nombre del contacto para eliminar: '))

            contact_book.delete(name)

        elif command == 'l':

            contact_book.show_all()


        elif command == 's':
            break
        else:
            print('Comando no encontrado.')


if __name__ == '__main__':
    print('')
    print('B I E N V E N I D O  A  L A  A G E N D A')
    run()
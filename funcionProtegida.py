def proctected(func):

    def wrapper(password):

        if password == 'milvia2019':
            return func()
        else:
            print('La contraseña es incorrecta')

    return wrapper


@proctected  # Decora nuestra función
def proctected_func():
    print('Tú contraseña es correcta.')


if __name__ == '__main__':
    password = str(input('Ingresar tu contraseña: '))

    proctected_func(password)

def say_hello(age):
    if age > 18:
        print('Usted es mayor de edad.')
    else:
        print('Usted es menor de edad.')


def run():
    age = int(input('Por favor ingrese su edad: '))
    res = say_hello(age)


if __name__ == "__main__":
    run()

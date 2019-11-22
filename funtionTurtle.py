import turtle


def main():
    window = turtle.Screen()
    milvia = turtle.Turtle()

    make_square(milvia)

    turtle.mainloop()


def make_square(milvia):
    length = int(input('Tamaño del cuadrado: '))

    for i in range(4):
        make_line_and_turn(milvia, 100)


def make_line_and_turn(milvia, length):
    milvia.forward(length)
    milvia.left(90)


if __name__ == '__main__':
    main()

import turtle

def main():
    window = turtle.Screen()
    milvia = turtle.Turtle()

    make_square(milvia)

    turtle.mainloop() #evitar que la ventana se cierre

def make_square(milvia):
    length = int(input('Tamaño de cuadrado:' ))

    for i in range(4):
        make_line_and_turn(milvia, length)#Generar lineas y vueltas

def make_line_and_turn(milvia, length):
    milvia.forward(length)
    milvia.left(90)

if __name__=='__main__': #la forma en que se le dice a python que queremos empezar.
    main()
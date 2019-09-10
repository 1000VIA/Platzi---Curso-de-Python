#intalar sudo pacman -S tk
import turtle

window = turtle.Screen() # Decirle a turtle que queremos generar una ventana
milvia = turtle.Turtle() # Genero una tortuga que se va a llamar 'Milvia'
milvia.forward(100) #Que se mueva una distancia de 100 de manera derecha.
milvia.left(90) #Que de una vuelta de 90º
milvia.forward(100)
milvia.left(90)
milvia.forward(100)
milvia.left(90)
milvia.forward(100)
milvia.left(90)

turtle.mainloop(); #mainloop -> es para que turtle no cierre la ventana

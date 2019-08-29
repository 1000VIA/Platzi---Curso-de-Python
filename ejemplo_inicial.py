#intalar sudo pacman -S tk   
import turtle

window = turtle.Screen() # Decirle a turtle que queremos generar una ventana
milvia = turtle.Turtle() # Genero una tortuga que se va a llamar 'Milvia'
milvia.forward(50) #Que se mueva una distancia de 50 de manera derecha.
milvia.left(90) #Que de una vuelta de 90º
milvia.forward(50)
milvia.left(90)
milvia.forward(50)
milvia.left(90)
milvia.forward(50)
milvia.left(90)

turtle.mainloop(); #mainloop -> es para que turtle no cierre la ventana

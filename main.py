from racket import Racket
from turtle import Screen, Turtle
import threading
from ball import Ball

l_side = -380
r_side = 370

ball = Ball()

screen = Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor("black")
screen.tracer(0)

racketl = Racket(l_side)
racketr = Racket(r_side)

screen.onkeypress(racketr.moveUp, 'Up')
screen.onkeypress(racketr.moveDown, 'Down')

screen.onkeypress(racketl.moveUp, 'w')
screen.onkeypress(racketl.moveDown, 's')

gameIsOn = True

screen.listen()
getPosition = 0

while gameIsOn:
    screen.update()
    getPosition = racketr.ycor()    
    print(getPosition)


screen.exitonclick()
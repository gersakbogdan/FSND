import random
import turtle

def tree(branchLenght, t):
    t.pensize(branchLenght / 10)

    if branchLenght < random.randint(1,2) * 20:
        t.color("green")
    else:
        t.color("brown")

    if branchLenght > 5:
        t.forward(branchLenght)
        t.left(25)
        tree(branchLenght - random.randint(10, 20),t)
        t.right(50)
        tree(branchLenght - random.randint(10, 20),t)
        t.left(25)
        color = t.pencolor()
        t.penup()
        t.backward(branchLenght)
        t.pendown()


window = turtle.Screen()
window.bgcolor("black")

myTurtle = turtle.Turtle()
myTurtle.color("brown", "blue")
myTurtle.left(90)
myTurtle.speed(0)
myTurtle.penup()
myTurtle.setpos(0, -250)
myTurtle.pendown()

tree(120, myTurtle)

window.exitonclick()

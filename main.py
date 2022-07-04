import turtle as turtle_module
from turtle import Screen
from random import choice

color_list = [(139, 164, 184), (27, 114, 171), (202, 141, 167), (237, 213, 67), (219, 157, 89), (22, 136, 66)]

tim = turtle_module.Turtle()

turtle_module.colormode(255)


def a_side():
    for _ in range(10):
        tim.dot(20, choice(color_list))
        tim.penup()
        tim.forward(50)


def return_base():
    tim.speed(10)
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(500)

tim.hideturtle() 
tim.setheading(225)
tim.penup()
tim.forward(300)
tim.setheading(0)

for _ in range(10):
    a_side()
    return_base()
    tim.left(180)

my_screen = Screen()
my_screen.exitonclick()

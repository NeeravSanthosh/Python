from turtle import *
import turtle
screen = turtle.Screen()
screen.screensize(400,400)
screen.title("HEXAGON")
screen.bgcolor("black")
t = turtle.Turtle()
t.color("whitesmoke")
t.width(5)
t.begin_fill()
s = 3
a = 360/s
for i in range(s):
    t.forward(100)
    t.left(a)
t.left(90)
t.penup()
t.forward(65)
t.right(90)
t.pendown()
for i in range(s):
    t.forward(100)
    t.right(a)
turtle.done()
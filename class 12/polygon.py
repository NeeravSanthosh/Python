from turtle import *
import turtle
screen = turtle.Screen()
screen.screensize(400,400)
screen.title("HEXAGON")
screen.bgcolor("black")
t = turtle.Turtle()
t.color("green")
t.shape("turtle")
t.width(4)
t.fillcolor("yellow")
t.begin_fill()
s = 6
a = 360/s
for i in range(s):
    t.forward(100)
    t.left(a)
t.end_fill()
turtle.done()
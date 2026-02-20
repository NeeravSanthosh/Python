import turtle
screen = turtle.Screen()
screen.screensize(600,600)
screen.title("Spiral square")
t = turtle.Turtle()
screen.bgcolor("Black")
t.color("yellow")
s = 20
while True:
    t.forward(s)
    t.right(90)
    s=s+5
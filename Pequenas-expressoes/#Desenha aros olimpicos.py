#Desenha aros olimpicos
import turtle

s = turtle.Screen()
t = turtle.Turtle()
def jump(t,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

def AroOlimpico(t,x,y):
    t.pensize(3)
    t.setheading(0)
    jump(t,x,y)
    t.circle(100)

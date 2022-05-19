#Desenha aros olimpicos
from re import A
import turtle

s = turtle.Screen()
t = turtle.Turtle()

#te = int(input("Defina T: "))
#xis = int(input("Defina X: "))
#ip = int(input("Defina Y: "))

def jump(t,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

def AroOlimpico(x,y):
    t.pensize(5)
    t.setheading(0)
    jump(t,x,y)
    t.pencolor("blue")
    t.circle(50)
    jump(t,x+45,y-45)
    t.pencolor("yellow")
    t.circle(50)
    jump(t,x+90,y)
    t.pencolor("black")
    t.circle(50)
    jump(t,x+135,y-45)
    t.pencolor("green")
    t.circle(50)
    jump(t,x+180,y)
    t.pencolor("red")
    t.circle(50)

AroOlimpico(-150,0)
AroOlimpico(-100,-210)
AroOlimpico(-50,+210)
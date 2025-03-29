from math import radians
from secrets import token_bytes

from shared_turtle import global_turtle as turtle

def chosen_challenge_one():
    radius = 40
    turtle.begin_fill()
    turtle.color("yellow")
    turtle.left(90)
    turtle.circle(radius, 180)
    turtle.left(60)
    turtle.forward(radius/2)
    turtle.left(260)
    turtle.forward(radius/2)
    turtle.left(60)
    turtle.circle(radius,180)
    turtle.end_fill()

def chosen_challenge_two():
    radius = 40

    for _ in range(3):
        turtle.circle(radius, 240)
        turtle.right(120)
def chosen_challenge_three(n):
    for _ in range(n):
        turtle.circle(26)
        turtle.right(45)

def chosen_challenge_four():
    radius = 70
    for _ in range(3):
        turtle.circle(radius, 240)
        turtle.right(120)
        turtle.forward(4)

    turtle.penup()
    turtle.fd(radius * 1.7 - radius)
    turtle.pendown()

    for _ in range(3):
        turtle.circle(radius * 1.7  , 240)
        turtle.right(120)


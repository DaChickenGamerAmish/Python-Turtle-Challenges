"""Python Turtle Module Challenges"""

from shared_turtle import global_turtle as turtle

# Challenge 1: Draw A Square
# Use the turtle to draw a square
# Use the side_length variable to make varying sizes

def challenge_one(side_length):
    turtle.forward(side_length)
    turtle.left(90)
    turtle.forward(side_length)
    turtle.left(90)
    turtle.forward(side_length)
    turtle.left(90)
    turtle.forward(side_length)
    pass

# Challenge 2: Draw a Triangle
# Make an equilateral triangle

def challenge_two(side_length):
    turtle.forward(side_length)
    turtle.left(90)
    turtle.forward(25)
    turtle.left(120)
    turtle.forward(50)
    pass

# Challenge 3: Draw a Red Circle
# Use the turtle to draw a red c

def challenge_three(radius):
    turtle.begin_fill()
    turtle.color("Red")
    turtle.circle(radius)
    turtle.end_fill()

    pass

# Challenge 4: Draw a Star
# Draw a 5-pointed star with a given size

def challenge_four(number_of_sides, side_lengths):
    for i in range(5):
        turtle.left(10)
        turtle.forward(10)
    pass

# Challenge 5: Draw a Polygon
# Draw a polygon with a given number of sides and side length

def challenge_five(sides, side_length):
    pass

# Challenge 6: Draw a Spiral
# Draw a colorful spiral with increasing line lengths

def challenge_six():
    pass

# Challenge 7: Draw a Flower
# Draw a flower with a given number of petals and radius

def challenge_seven(number_of_petals, radius):
    pass

# Challenge 8: Fractal Tree
# Draw a fractal tree with recursive branches

def challenge_eight():
    pass

# Challenge 9: Spirograph
# Draw a spirograph with a given radius and steps

def challenge_nine(radius, steps):
    pass

# Challenge 10: Design a House
# Combine basic shapes to create a house design

def challenge_ten():
    pass

# Challenge 11: Draw a Landscape
# Create a basic landscape with a sun, grass, and a tree

def challenge_eleven():
    pass

# Challenge 12: Turtle Race
# Simulate a race with multiple turtles

def challenge_twelve():
    pass
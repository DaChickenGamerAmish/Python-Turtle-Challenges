"""Python Turtle Examples"""

from shared_turtle import global_turtle as turtle

def example_forward():
    """Move the turtle forward by a specified distance."""
    turtle.forward(100)  # Moves the turtle forward by 100 units

def example_backward():
    """Move the turtle backward by a specified distance."""
    turtle.backward(100)  # Moves the turtle backward by 100 units

def example_left():
    """Turn the turtle left by a specified angle."""
    turtle.left(90)  # Turns the turtle left by 90 degrees

def example_right():
    """Turn the turtle right by a specified angle."""
    turtle.right(90)  # Turns the turtle right by 90 degrees

def example_penup():
    """Lift the pen up so no drawing occurs."""
    turtle.penup()
    turtle.forward(50)  # Moves forward without drawing

def example_pendown():
    """Put the pen down to start drawing."""
    turtle.pendown()
    turtle.forward(50)  # Moves forward while drawing

def example_circle():
    """Draw a circle with a specified radius."""
    turtle.circle(50)  # Draws a circle with a radius of 50 units

def example_color():
    """Change the turtle's pen color."""
    turtle.color("blue")  # Sets the pen color to blue
    turtle.forward(100)  # Draws a blue line

def example_reset():
    """Reset the turtle's position and clear the screen."""
    turtle.reset()  # Clears the screen and resets the turtle's position

def example_speed():
    """Set the turtle's speed."""
    turtle.speed("fastest")  # Sets the turtle's speed to the fastest setting
    turtle.circle(100)  # Draws a circle quickly
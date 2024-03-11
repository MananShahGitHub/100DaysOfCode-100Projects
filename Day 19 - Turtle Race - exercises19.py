from turtle import Turtle, Screen

# Create turtle and screen objects
turtle = Turtle()
screen = Screen()


# Function to move the turtle forwards
def move_forwards():
    turtle.forward(10)


# Function to move the turtle backwards
def move_backwards():
    turtle.backward(10)


# Function to turn the turtle counter-clockwise
def turn_left():
    turtle.left(10)  # Turns the turtle left by 10 degrees


# Function to turn the turtle clockwise
def turn_right():
    turtle.right(10)  # Turns the turtle right by 10 degrees


# Function to clear the drawing
def clear_drawing():
    turtle.clear()  # Clears the turtle's drawings
    turtle.penup()  # Lifts the pen up so it doesn't draw while going to the starting position
    turtle.home()  # Moves the turtle to the starting position
    turtle.pendown()  # Puts the pen down to start drawing again


# Set up the screen to listen to keyboard events
screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear_drawing, "c")

# Click on the screen to exit (closes the window)
screen.exitonclick()

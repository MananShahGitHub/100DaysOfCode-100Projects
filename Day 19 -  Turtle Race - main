screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.speed("fastest")
    new_turtle.penup()
    new_turtle.color(colors[index])
    new_turtle.goto(x=-230, y=y_positions[index])
    all_turtles.append(new_turtle)

if bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:

        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()

# Originally did not use a for loop to create the 6 different turtle objects
# M = Turtle(shape="turtle")
# M.penup()
# M.color("red")
# M.goto(x=-230, y=-150)
#
# N = Turtle(shape="turtle")
# N.penup()
# N.color("orange")
# N.goto(x=-230, y=-100)
#
# O = Turtle(shape="turtle")
# O.penup()
# O.color("yellow")
# O.goto(x=-230, y=-50)
#
# P = Turtle(shape="turtle")
# P.penup()
# P.color("green")
# P.goto(x=-230, y=0)
#
# Q = Turtle(shape="turtle")
# Q.penup()
# Q.color("blue")
# Q.goto(x=-230, y=50)
#
# R = Turtle(shape="turtle")
# R.penup()
# R.color("purple")
# R.goto(x=-230, y=100)

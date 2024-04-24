# import colorgram
# from turtle import Turtle, Screen, colormode

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

# The above was used to extract the RGB values of the HIRST painting in the variable below
import random
from turtle import Turtle, Screen, colormode


color_list = [(250, 247, 244), (248, 245, 246), (213, 154, 96), (52, 107, 132), (179, 77, 31), (202, 142, 31),
              (115, 155, 171), (124, 79, 99), (122, 175, 156), (229, 236, 239), (226, 198, 131), (242, 247, 244),
              (192, 87, 108), (11, 50, 64), (55, 38, 19), (45, 168, 126), (47, 127, 123), (200, 121, 143),
              (168, 21, 29), (228, 92, 77), (244, 162, 160), (38, 32, 35), (2, 25, 24), (78, 147, 171), (170, 23, 18),
              (19, 79, 90), (101, 126, 158), (235, 166, 171), (177, 204, 185), (49, 62, 84)]

colormode(255)

screen = Screen()

screen.setup(350, 350)

M = Turtle()
M.speed("fastest")

M.penup()
M.hideturtle()
M.setposition(-130, -130)
M.setheading(0)

rows = 10
cols = 10

for r in range(rows):
    for c in range(cols):
        M.dot(20, random.choice(color_list))
        M.forward(30)
    M.setheading(90)
    M.forward(30)
    M.setheading(180)
    M.forward(cols * 30)
    M.setheading(0)

screen = Screen()
screen.exitonclick()

# # Extract color from the picture
# import colorgram

# rgb_colors = []
# colors = colorgram.extract("image.jpg", 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_colors = (r, g, b)
#     rgb_colors.append(new_colors)
    
# print(rgb_colors)

import turtle as t
import random

kanny = t.Turtle()
kanny.hideturtle()
kanny.speed("fastest")
t.colormode(255)
color_list = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]


def row_dot(column_count):
    for _ in range(column_count):
        kanny.pendown()
        kanny.dot(20, random.choice(color_list))
        kanny.penup()
        kanny.forward(50)

def hirst_painting(x_cor, y_cor, row, column):
    for _ in range(row):
        kanny.penup()
        kanny.goto(x_cor, y_cor)
        row_dot(column)
        y_cor += 50
        kanny.goto(x_cor, y_cor)

hirst_painting(-200, -200, 10, 10)

screen = t.Screen()
screen.exitonclick()
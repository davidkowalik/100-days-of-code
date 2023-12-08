import random
from turtle import Turtle, Screen, colormode
from random import randint
# import colorgram


def color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b

# def draw_circles(gap_size):
#     for _ in range(int(360 / gap_size)):
#         tim.pencolor(color())
#         tim.left(gap_size)
#         tim.circle(200)

# rgb_colors = []
# colors = colorgram.extract('.\\image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)


def print_row(dots_number, dot_size, space, colors):
    for _ in range(dots_number):
        tim.dot(dot_size, random.choice(colors))
        tim.forward(space)


tim = Turtle()
tim.penup()
tim.hideturtle()
colormode(255)
color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20),
              (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70),
              (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74),
              (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153),
              (176, 192, 208), (168, 99, 102)]
tim.speed("fastest")

dot_nr = 10
dot_space = 50
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
x = tim.position()[0]
y = tim.position()[1]

for _ in range(dot_nr):
    y += dot_space
    print_row(dot_nr, 20, dot_space, color_list)
    tim.setx(x)
    tim.sety(y)
tim.hideturtle()






screen = Screen()
screen.exitonclick()

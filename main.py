import turtle
import random

# import colorgram
#
# colors = colorgram.extract('image.jpg', 30)
# rgb_colors = []
# for color in colors:
#     rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))
# print(rgb_colors)
color_list = [(239, 236, 238), (238, 237, 236), (237, 237, 241), (26, 108, 164), (193, 38, 81), (237, 161, 50),
              (234, 215, 86), (227, 237, 229), (223, 137, 176), (143, 108, 57), (103, 197, 219), (21, 57, 132),
              (205, 166, 30), (213, 74, 91), (238, 89, 49), (142, 208, 227), (119, 191, 139), (5, 185, 177),
              (106, 108, 198), (137, 29, 72), (4, 162, 86), (98, 51, 36), (24, 155, 210), (229, 168, 185),
              (173, 185, 221), (29, 90, 95), (233, 173, 162), (156, 212, 190), (87, 46, 33), (37, 45, 83)]

tim = turtle.Turtle()
turtle.colormode(255)
tim.speed("fast")
tim.hideturtle()
tim.pensize(10)


for index1 in range(0, 10):
    tim.teleport(-100, (index1 * 40) - 100)
    for index2 in range(10):
        tim.dot(20, random.choice(color_list))
        tim.up()
        tim.forward(40)
        tim.down()


screen = turtle.Screen()
screen.exitonclick()

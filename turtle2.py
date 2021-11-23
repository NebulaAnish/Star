# import turtle
# a = turtle.Turtle()

# # a.forward(100)
# # a.left(45)
# # a.forward(100)
# for i in range(4):
#     a.forward(100)
#     a.left(90)
# turtle.done()

import turtle
turtle.speed(10)
a = turtle.Turtle()

a.color("blue", "cyan")
a.begin_fill()

for i in range(80):
    a.forward(200)
    a.left(155)
a.end_fill()
turtle.done()

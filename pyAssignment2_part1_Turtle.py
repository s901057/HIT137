from turtle import *
import colorsys

bgcolor('black')
tracer(99)
width(78)
speed(0)

h = 0
n = 70

for i in range(730):
    c = colorsys.hsv_to_rgb(h, 1, .8)
    h += 1 / n

    pencolor(c)
    pensize(5)

    lt(i)
    circle(66)
    fd(-66)
    fd(90)

exitonclick()

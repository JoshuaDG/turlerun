# Joshua D Gonzalez CS 200

import turtle
import random


#red_name = raw_input("what is red's turtle name: ")
#green_name = raw_input("what is green's turtle name: ")
red_name = "red"
green_name = "green"
red = turtle.Turtle()
green= turtle.Turtle()
TL = 750
TH= 600
bouds = turtle.Turtle()
bouds.width(4)
bouds.color(0,0,0)
bouds.penup()
bouds.goto(-400,250)
bouds.pendown()
bouds.forward(TL)
bouds.right(90)
bouds.forward(TH)
bouds.right(90)
bouds.forward(TL)
bouds.right(90)
bouds.forward(TH)

bouds.hideturtle()

red.color(1.0,0,0)
green.color(0,1.0,0)

red.shape("turtle")
green.shape("turtle")

red.penup()
red.goto(-400,125)
red.pendown()
green.penup()
green.goto(-400,-125)
green.pendown()

x = -400
gx = -400
start_x = -400
y = 125
gy = -125
dist = x - start_x
dist_green = x - start_x
step = 0

while dist < TL and dist_green < TL:
    change_x = random.randint(1,10)
    greenchange_x = random.randint(1,10)
    change_y = random.randint(-10,10)
    greenchange_y = random.randint(-10,10)
    x = x + change_x
    y = y + change_y
    gx = gx + greenchange_x
    gy = gy + greenchange_y
    red.goto(x,y)
    green.goto(gx,gy)
    dist = dist + change_x
    dist_green = dist_green + greenchange_x
    step = step + 1
red_d = dist
green_d = dist_green

if red_d >= TL:
    print (" winner is %s and his distance is %.f " % (red_name,step))
else: 
    print (" winner is %s and his/her distance is %.f "  % (green_name,step))

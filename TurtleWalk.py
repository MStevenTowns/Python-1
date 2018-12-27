#M. Steven Towns
#Assignment 5
#1/20/2014

import turtle, random

anne=turtle.Turtle()
anne.speed(0)
anne.up()
anne.setpos(-325,-275)
anne.down()
anne.forward(650)
anne.left(90)
anne.forward(275*2)
anne.left(90)
anne.forward(650)
anne.left(90)
anne.forward(275*2)
anne.up()
anne.setpos(5000,5000)
fred=turtle.Turtle()
fred.shape("turtle")
fred.speed(0)
fred.resizemode("auto")
fred.color("black","green")
fred.pensize()
print "This is the Turtle Hulk, he gets bigger when he hits the top and right,\nbut he gets smaller when he hits the bottom or left."
while True:
    fred.forward(5)
    fred.right(random.randint(-15,15))
    #Right
    if (fred.xcor()>325):
        fred.right(90)
        fred.pensize(fred.pensize()+1)
        fred.pencolor(random.random(),random.random(),random.random())
        if (fred.pensize()>20):
            fred.pensize(20)
            print "Roar!!"
        if (fred.xcor()>350):
            fred.up()
            fred.setpos(0,0)
            fred.down()
    #Top
    if (fred.ycor()>275):
        fred.right(90)
        fred.pensize(fred.pensize()+1)
        fred.pencolor(random.random(),random.random(),random.random())
        if (fred.pensize()>20):
            fred.pensize(20)
            print "Roar!!"
        if (fred.ycor()>300):
            fred.up()
            fred.setpos(0,0)
            fred.down()
    #Left
    if (fred.xcor()<-325):
        fred.right(90)
        fred.pensize(fred.pensize()-1)
        fred.pencolor(random.random(),random.random(),random.random())
        if (fred.pensize()<1):
            fred.pensize(1)
            print "Ouch!"
        if (fred.xcor()<-350):
            fred.up()
            fred.setpos(0,0)
            fred.down()
    #Bottom
    if (fred.ycor()<-275):
        fred.right(90)
        fred.pensize(fred.pensize()-1)
        fred.pencolor(random.random(),random.random(),random.random())
        if (fred.pensize()<1):
            fred.pensize(1)
            print "Ouch!"
        if (fred.ycor()<-300):
            fred.up()
            fred.setpos(0,0)
            fred.down()

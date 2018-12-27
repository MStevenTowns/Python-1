#M. Steven Towns
#Assignment 9
#2/4/14

import turtle
bob=turtle.Turtle()

x=-1
while x<0 or x>13:
    x=raw_input('Give me a number between 0 and 13: ')
    x=int(x)
    if x>13 or x<0:
        print "That Doesn't Work!!!"
fractal="SRSRS"
seed="SLSRSLS" #never Changes
bob.up()
bob.goto(-200,115.47005383792515290182975610039)
bob.down()
l=400.0
screen=bob.getscreen()
for i in range(x):
    fractal=fractal.replace("S", seed)
    l=l/3.0
length=len(fractal)
screen.tracer(10000)
print ("This is going to take "+str(length)+" comands")
for letter in fractal:
    if letter=="S":
        bob.forward(l)
    elif letter=="L":
        bob.left(60)
    elif letter=="R":
        bob.right(120)
screen.update()
turtle.done()

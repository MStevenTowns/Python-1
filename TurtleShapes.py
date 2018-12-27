# M. Steven Towns
#Assignment 4.1
#1/14/2014

import turtle

print "This is bob, he is a turtle"
print "Bob likes to draw shapes"

bob=turtle.Turtle()
bob.shape("turtle")
#This tells bob to draw a square
for i in range(4):   
    bob.forward(100)
    bob.left(90)

#This puts bob in a new position    
bob.up()            
bob.setpos(0,-100)
bob.down()
#This tells bob to a triangle
for i in range(3):  
    bob.forward(100)
    bob.left(120)

#This puts bob in a new position
bob.up()            
bob.setpos(-150,0)
bob.down()
#This tells bob to draw a pentagon
for i in range(5):  
    bob.forward(100)
    bob.left(72)


    #in new file resizemode = noresize search fit in documentation

turtle.done() #this keeps the turtle window from not responding


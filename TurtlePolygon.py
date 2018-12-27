# M. Steven Towns
#Assignment 4.2
#1/14/2014

#learn.code.org
import turtle

print "This is bob, he is a turtle"
print "Bob likes to draw shapes"
bob=turtle.Turtle()
bob.shape("turtle")
again=True
while again:
    sides=raw_input('How many sides on your polygon? ')
    sides=int(sides)
    x=float(sides)
#I put weird stuff in my code
    if sides<3:
        print "Are you stupid or something?!? A polygon has 3 or more sides!"
    #hard code square
   # elif sides==4:
     #   bob.up()
      #  bob.setpos(
            #FIX THIS
       # bob.down()
    elif sides>=3:
        print "Really man! what you need a polygon for anyway?"
        bob.up()
        bob.setpos(-250,0)
        bob.down()
        bob.right(90)
        angle=((360.0/x)) 
        length=(float(1570.0/x)) #circumfrence/sides
        bob.forward(length/2.0)
        for i in range(sides):
            bob.left(angle)
            bob.forward(length) 
    go=True
    while go==True:
        test=raw_input('Draw another? (yes/no) ')
        if (test.lower()=="yes"):
            again=True
            go=False
            print "Yay!!"
            print "Mommy, I have a friend that isn't dead!"
            bob.reset()
    #Some REALLY weird stuff
        if (test.lower()=="no"):
            again=False
            print "b...but, why?? *cries*"
            print "I don't like it when my friends leave, accidents happen to them..."
            go=False
            turtle.done() #this keeps the turtle window from not responding
        else:
            print "What you say to me!?! What?!? I DARE you to say it!"
            go=True

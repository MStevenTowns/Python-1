##M. Steven Towns
##Assignment 10
##2/6/14

import turtle
bob=turtle.Turtle()
go=True
while go:
    name=raw_input('What is the name of the input file? (Enter for default): ')
    if (name==""):
        name="Input"
    if not name.endswith(".txt"):
        name+=".txt"
    f=file(name)
    num1=0
    num2=0
    run=0
    for line in f:
        where=line.find(" ")
        num1=line[:where]
        num1=float(num1)
        num2=line[where+1:]
        num2=float(num2)
        if (run==0):
            bob.up()
        bob.goto(num1,num2)
        bob.down()
        run+=1
    again=True
    while again:
        prompt=(raw_input("Do you want to play again?: ")).lower()
        if prompt=="no":
            go=False
            print "Goodbye!"
            turtle.done()
            again=False
        elif prompt=="yes":
            print "Yay! let's play!."
            again=False
            bob.reset()
        else:
            again=True
            print "Try that again, I couldn't understand that."

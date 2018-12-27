#Prob1
x=raw_input("Give me a number to multiply by 5: ")
x=float(x)
ans=x*5
print ("The number you have typed is "+str(x)+" and "+str(x)+"*5 is "+str(ans))

#Prob2
x=raw_input("> ")
x=float(x)
print x

#Prob3
raw_input returns a string

#Prob4
x=raw_input("Give me a number: ")
y=raw_input("Give me another number: ")
x=float(x)
y=float(y)
if (x>y):
    print (str(x)+"is greater than "+str(y)+".")
else:
    print (str(y)+" is greater than "+str(x)+".")

#Prob5
goto requires 2 arguments an x-cord and a y-cord

#Prob6
= stores the value on the right into the variable on the left
== compares the value on the right with the value on the left to see if they are equal -returns True/False

#Prob7
x=raw_input("Give me a word. I will print that word once for each letter it has. ")
y=len(x)
for i in range (y):
    print x

#Prob8
x=int(raw_input("Give me a side length: "))
import turtle
bob=turtle.Turtle()
for i in range (6):
    bob.right(360.0/6)
    bob.forward(x)
turtle.done()

#Prob9
name_of_turtle.heading()

#Prob10
meet the conditions set by while loop
use a break

#Prob11
import random
num=random.randint(4,11)
print num

#Prob12
x=int(raw_input("I am now going to double the number you give me until it is bigger than 1000. "))
while (x<1000):
    x*=2
    print x

#Prob13
When you need to do something forever
if you want to repeatedly use a program, such as a calculator for multiple problems

#Prob14
x=raw_input("Give me a word and I will rip the first and last letters off. ")
x=x[1:-1]
print x

#Prob15
the python equal sign forces the value on the righ to be stored in the left, in algebra it simply tells you that they are equal

#Prob16
no, python requires that there be an if statement before elif

#Prob17
f=file("somefile.txt")
output=""
for line in f:
    output+=line[0]
print output

#Prob18
x=raw_input("Give me a word and I will ignore it and print out squirrel. ")
print "squirrel"

#Prob 19
colon (:)

#Prob20
use return 

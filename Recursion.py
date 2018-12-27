#!/bin/bin/python2
def pow(a,b):
    if b==0: return 1
    return (a*(pow(a,(b-1))))
def factorial(n):
    if n==0: return 1
    return (n*(factorial(n-1)))
def printTriangle(n,c):
    if n==0: return
    print c*n
    return (printTriangle(n-1,c))

print "This will take a number and raise it to the specified power"
num1=int(raw_input("Give me a number: "))
num2=int(raw_input("Give me an exponent: "))
print pow(num1,num2)

print"\nThis will print a triangle with a specified number of characters"
num1=int(raw_input("Give me a number: "))
c=raw_input("Give me a character: ")
printTriangle(num1,c)

print "\nThis will take a number and give the factorial of it"
num1=int(raw_input("Give me a number: "))
print factorial(num1)

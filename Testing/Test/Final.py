print """*** problem 1 ***
Ask the user for a list of animals separated by commas and then turn it into a list.  Print out this list.
----------------------------------------"""
m=raw_input("list input> ")
m=m.split(",")
print m

print """\n*** problem 2 ***
Ask the user for another animal and put it at the beginning of the list.
----------------------------------------"""
x=raw_input("animal> ")
x=[x]
x+=m
print x

print """\n*** problem 3 ***
Loop through the list and sum up the number of letters in all the words.
----------------------------------------"""
num=0
for elem in x:
    num+=len(elem)
print num


print """\n*** problem 4 ***
Create a class for a BankAccount. The __init__ function should accept an initial deposit.  Add a __str__ function.
Let the user create a BankAccount and print it out.
----------------------------------------"""
import locale
locale.setlocale( locale.LC_ALL, '' )
class BankAccount:
    def __init__(self,v):
        self.value=v
    def __str__(self):
        return "The bank account has "+str(locale.currency(self.value))+" in it."
    def deposit(self,v):
        self.value+=v
    def withdraw(self,v):
        self.value-=v

x=float(raw_input("initial deposit> "))
b=BankAccount(x)
print b

print """\n*** problem 5 ***
Add two methods to the BankAccount to deposit and withdraw money.  Allow the user to deposit and then withdraw money and then print the BankAccount.
----------------------------------------"""
x=float(raw_input("deposit> "))
b.deposit(x)
x=float(raw_input("withdraw> "))
b.withdraw(x)
print b

print """\n*** problem 6 ***
Let the user specify a text file that contains a number on each line.  Create an array of these numbers and print them out.
----------------------------------------"""
f=file(raw_input("filename> "))
m=[]
for line in f:
    m+=[int(line)]
print m

print """\n*** problem 7 ***
Loop through the array in the last problem.  Append any multiples of 7 to a new array and print it.
----------------------------------------"""
x=[]
for elem in m:
    if elem%7==0:
        x+=[elem]
print x

print """\n*** problem 8 ***
Let the user type in a word and remove all the vowels and reprint it.
----------------------------------------"""
x=raw_input("input> ")
x=x.replace("a","")
x=x.replace("e","")
x=x.replace("i","")
x=x.replace("o","")
x=x.replace("u","")
x=x.replace("A","")
x=x.replace("E","")
x=x.replace("I","")
x=x.replace("O","")
x=x.replace("U","")
print x

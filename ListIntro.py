print "Problem 2"
myList=[]
myList+=[76]
myList.append(92.3)
myList+=["hello"]
myList+=[True]
myList.append(76)
print str(myList)+("\n")

print "Problem 4"
def average(aList):
    total=0
    for j in myList:
      total+=j
    avg=total/100
    return avg
import random
myList=[]
for i in range (100):
    x=random.randint(0,1000)
    myList+=[x]
print "the average for this list is "+str(average(myList))+".\n"

print "Problem 6"
def sum_of_squares(xs):
    total=0
    for i in xs:
        total+=i**2
    return total
xs=[2, 3, 4]
print xs
print "The sum of squares is "+str(sum_of_squares(xs))+".\n"

print "Problem 8"
myList=[0,1,2,3,4,5,6,7,8,9]
total=0
for i in myList:
    if i%2==0:
        total+=i
print myList
print "The total of the even numbers is "+str(total)+".\n"

print "Problem 10"
myList=['hello', 'hi', '12345','52','56234']
total=0
for i in myList:
    if len(i)==5:
        total+=1
print myList
print str(total)+"words in the list have 5 characters.\n"

print "Problem 12"
myList=["sam",'helo','hi','1235','52','6234']
print myList
print "The number of words before and including 'sam' was "+str(myList.index('sam')+1)+".\n"

print "Problem 14"
def replace(s, old, new):
    return s.replace(old, new)
s = 'I love spom! Spom is my favorite food. Spom, spom, spom, yum!'
print s
print replace(s, 'om', 'am')

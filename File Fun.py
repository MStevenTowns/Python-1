##M. Steven Towns
##Assignment 13 File Fun
##4/1/14

myList=[]
name=(raw_input('What is the name of unsorted input file? (Enter for default): ')).strip()
if (name==""):
    name="InputSort"
if not name.endswith(".txt"):
    name+=".txt"
f=file(name)
for line in f:
    myList+=[line.strip()]
myList.sort()
for elem in myList:
    print elem

name=(raw_input('\nWhat is the name of the numeric input file? (Enter for default): ')).strip()
if (name==""):
    name="InputNum"
if not name.endswith(".txt"):
    name+=".txt"
f=file(name)
myList=[]
for line in f:
    line=float(line.strip())
    myList+=[line]
myList.sort()
print "Min:",myList[0]
print "Max:",myList[-1]
print "Average:",sum(myList)/len(myList)

name=(raw_input('\nWhat is the name of the encoded input file? (Enter for default): ')).strip()
if (name==""):
    name="InputCode"
if not name.endswith(".txt"):
    name+=".txt"
f=file(name)
sentence=""
for line in f:
    hold=line.split()
    word=hold[0]
    num=int(hold[1])
    sentence+=word[num]
print "The secret word is:",sentence

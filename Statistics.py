##M. Steven Towns
##4/29/204
##Assignment 14

import math

def minimum(aList):
    guess=aList[0]
    for num in aList:
        if num<guess:
            guess=num
    return guess
def maximum(aList):
    guess=aList[0]
    for num in aList:
        if num>guess:
            guess=num
    return guess
def sumNum(aList):
    total=0
    for num in aList:
        total+=num
    return total
def avg(aList):
    return sumNum(aList)/len(aList)
def median(aList):
    x=len(aList)
    y=x/2
    if x%2==1:
        return aList[y]
    else:
        return (aList[y-1]+aList[y])/2
def notThere(elem, aList):
    out=True
    for thing in aList:
        if elem==thing:
            out=False
    return out
def mode(aList):
    high=0
    nums=[]
    out=""
    for elem in aList:
        if high<aList.count(elem):
            high=aList.count(elem)
    for x in aList:
        if (aList.count(x)==high and nums.count(x)<1):
            nums+=[x]
    for a in range(len(nums)):
        out+=str(nums[a])+" "
    return out

def standDev(aList):
    xBar=avg(aList)
    sumThis=0
    for i in aList:
        sumThis+=((i-xBar)**2)
    return math.sqrt(sumThis/(len(aList)-1))


nameFileIn=raw_input('What is the name of the input file? (Enter for default): ')
if (nameFileIn==""):
    nameFileIn="Input"
if not nameFileIn.endswith(".txt"):
    nameFileIn+=".txt"
nameFileOut=raw_input('What is the name of the output file? (Enter for default): ')
if (nameFileOut==""):
    nameFileOut="Output"
if not nameFileOut.endswith(".txt"):
    nameFileOut+=".txt"

inFile=file(nameFileIn,"r") 
outFile=file(nameFileOut,"w")

m=[]
for line in inFile:
    m+=[float(line)]
sendout=""
sendout+=("Count: "+str(len(m))+"\nSum: "+str(sumNum(m))+"\nMode(s): "+str(mode(m))+"\nAverage: "+str(avg(m))+"\nMinimum: "+str(minimum(m))+"\nMaximum: "+str(maximum(m))+"\nMedian: "+str(median(m))+"\nStandard Deviation: "+str(standDev(m)))
outFile.write(sendout)
print "\n"+sendout
outFile.close()
inFile.close()

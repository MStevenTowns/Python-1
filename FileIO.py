##M. Steven Towns
##Assignment 11
##3/14/14

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

inFile=file(nameFileIn) 
outFile=file(nameFileOut,"w")

for line in inFile:
    hold=line.strip().split(" ")
    name=hold[0]
    wage=hold[1]
    wage=float(wage[1:])
    hours=hold[2]
    hours=float(hours[:-5])
    sendOut=name+" $"+str(wage*hours)
    outFile.write(sendOut+"\n")
print "The wages have been calculated"
outFile.close()
inFile.close()
    

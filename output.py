##inFile=file("input.txt") #use w if writing
##outFile=file("output.txt","w")
##
##for line in inFile:
##    formattedName=line.strip().title()+"\n"
##    outFile.write(formattedName)
##    
##outFile.close()
        
##a=int(x[0:2])
##a= int(x.split(" ")) #splits list based on the char

inFile=file("input.txt") #use w if writing
outFile=file("output.txt","w")

for line in inFile:
    numList=line.strip().split(" ")
    product=1
    for num in numList:
        product*=int(num)
    outFile.write(str(product)+"\n")
outFile.close()
inFile.close()
print "Done"


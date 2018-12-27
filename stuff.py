#3/31/14 notes
f=file("input.txt")
m=f.readlines()
#print m
n=[]
for elem in m:
    n.append(elem.strip().title())
for elem in n:
    pass
    #print elem, n.count(elem)
outList=[]
for elem in n:
    if elem not in outList:
        outList.append(elem)
#print outList
outList.sort()
#print outList
for name in outList:
    print name,n.count(name)

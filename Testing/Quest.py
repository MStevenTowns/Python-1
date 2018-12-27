def combine(m,n):
    return m+n
def bedazzle(m):
    return ["*"]+m+["*"]
def topThree(m):
    m.sort()
    return m[-3:]
def countMultipliesOf5(m):
    count=0
    for i in m:
        if i%5==0:
            count+=1
    return count
def random5():
    m=[]
    for i in range(5):
        m+=[random.randint(-1000,1000)]
    return m

import random

a=[1,2,3]
b=[4,5,6]
print combine(a,b)
print bedazzle(a)
print topThree(a+b)
print countMultipliesOf5(a+b)
print random5()

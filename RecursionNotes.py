def printN(s,n):
    if n<=0: return
    print s
    printN(s,n-1)
    
def  printStrip(s):
    if len(s)<=0:
        print s
        return
    print s
    printStrip(s[:-1])
    print s
    
def multiply(a,b):
    if b==0: return 0
    if b>0:
        return a+multiply(a,b-1)
    else:
        return -a+multiply(a,b+1)

def pow(a,b):
    if b==0: return 1
    print str(a)+"**"+str(b)+"="+str(a)+"*("+str(a)+"**"+str(b)+")"
    return (a*(pow(a,(b-1))))
def factorial(n):
    if n==0: return "0!=1"
    print str(n)+"!="+str(n)+"*"+str(n-1)+"!"
    factorial(n-1)
def printTriangle(n):
    if n==0: return
    print "*"*n
    return (printTriangle(n-1))

    
    
printN("Hello",7)
printStrip("Hello")
print multiply(7,-75)
num1=int(raw_input("Give me a number: "))
num2=int(raw_input("Give me an exponent: "))
pow(num1,num2)
print
num1=int(raw_input("Give me a number: "))
printTriangle(num1)
print
num1=int(raw_input("Give me a number: "))
factorial(num1)

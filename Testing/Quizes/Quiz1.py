##M. Steven Towns
##Quiz 1
##2/10/14



#Problem 1
x=raw_input('How many times do you want me to print hello?: ')
x=int(x)
for i in range (x):
    if (i%3==0):
        print "hello..."
    elif (i%3==1):
        print "Hello."
    elif (i%3==2):
        print "HELLO!!!!!"


#Problem 2
y=raw_input('Type something: ')
#print between star
y=y[y.find("*")+1:]
y=y[:y.find("*")]
print y


#Problem 3
z=float(raw_input('Give me a number: '))
while z>=1:
    z=z/2
    print z



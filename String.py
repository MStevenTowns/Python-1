# M. Steven Towns
#Assignment 6
#1/22/2014

sent=raw_input('Give me a sentence: ')
sent=(sent.strip())
print sent.lower()
upperC=sent
upperC=(upperC.replace(".","!"))
print upperC.upper()
this=raw_input('Tell me something to find in your sentence: ')
this=this.strip()
if ((sent.lower()).find(this.lower()))>=0:
    print ("I found it!")
else:
    print ("That isn't in your sentence")
old=raw_input('What part of your sentence do you want to get rid of? ')
old=old.strip()
if (sent.find(old)>=0):
    word=raw_input('What do you want to replace it with? ')
    print (sent.replace(old,word))
else:
    print ("That isn't part of your sentence.")

name=raw_input('What is your full name? ')
name=(name.strip())
print ("Your initials are ")+((((name[0]) + (name[name.find(" ")+1])) + (name[name.find(" ", name.find(" ")+1)+1])).upper())+(".")




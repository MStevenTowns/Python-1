#M. Steven Towns
#Assignment 7
#1/28/2014

verb="a"
while not verb.endswith("ing") or len(verb)<=3:
        verb=(raw_input("Give me a verb ending in -ing: ")).strip()
        if not verb.endswith("ing"):
            print "WRONG, I told you to give me a verb ending in -ing!"
        if len(verb)<=3 and verb.endswith("ing"):
            print "Dont just type 'ing'"

name=raw_input('What is your name?: ')
name=(name.strip()).title()
place1=((raw_input('Place: ')).strip()).lower()
superhero=(raw_input('Superhero: '))
superhero=(superhero.strip()).title()
friend=(((raw_input('Another Name: ')).strip()).capitalize())
thing=((raw_input('Thing: ')).strip()).lower()
act1=((raw_input('Action: ')).strip()).lower()
food=((raw_input('Food: ')).strip()).lower()
act2=((raw_input('Another Action: ')).strip()).lower()
emotion=((raw_input('Emotion: ')).strip()).lower()
place2=((raw_input('Another Place: ')).strip()).lower()
print ("Your name is, "+name+", You are in "+place1+"! You are "+verb+" with "+friend+" from "+place2+". Suddenly you see a "+thing+" and "+friend+" decides that you need to "+act1+". Suddenly a "+food+" truck apears and everyone is "+emotion+".")

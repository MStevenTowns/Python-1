# M. Steven Towns
#Assignment 3
#1/14/2014

import random

playingGames=True
while playingGames:
    goal=random.randint(1,100)
    isRunning=True
    count=0
    while isRunning:
        x=raw_input("Give me a number between 1 and 100: ")
        x=int(x)
        count=count+1
        if x==goal:
            print("Congratulations! You have won, NOTHING!")
            print "It took you this many guesses to win?!?!?"
            print count
            isRunning=False
        elif x<goal:
            print "Too Low"
        elif x>goal:
            print "Too High"
    again=True
    while again:
        Prompt=raw_input("do you want to play again? (yes/no) ")
        if Prompt=="no":
            playingGames=False
            print "Goodbye!"
            again=False
        elif Prompt=="yes":
            print "Lets Play!"
            again=False
        else:
            again=True
            print "Try that again, I couldn't understand that."
    

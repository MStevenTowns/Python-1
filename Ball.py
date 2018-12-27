class BasketBall:
    def __init__(self,psi=100):
        self.psi=psi #up to 100
        self.hasHole=False
    def __str__(self):
        psi=self.psi
        output= "I am a ball "
        if self.hasHole:
            output+="with a hole"
        else:
            output+=("without a hole, and a PSI of "+str(self.psi)+".")
        return output 
        
    def bounce(self):
        if self.psi<=25:
            return "Thump"
        else:
            return "Bounce"
        
    def inflate(self,deltapsi=5):
        if not self.hasHole:
            out= "Woosh"
            self.psi+=deltapsi
            if self.psi>150: out+="\n"+self.pop()
            elif self.psi<0: self.psi=0
        else:
            out="tsssss"
        return out
    
    def pop(self):
        self.psi=0
        self.hasHole=True
        return "BAM!!"
    def patch(self):
        out=""
        if self.hasHole:
            self.hasHole=False
            out="The ball was patched."
        else: out="The ball doesn't have a hole."
        return out
    
import subprocess,os,platform,sys
bob=BasketBall()
while(True):
    print "\n1: Inflate\n2: Deflate\n3: Pop\n4: Bounce\n5: Patch\n6: Print\n7: Quit"
    choice=int(raw_input("What do you want to do?: "))
    if choice==1:
        x=int(raw_input("how much do you want to inflate it by? "))
        print bob.inflate(x)
    if choice==2:
        x=int(raw_input("how much do you want to deflate it by? "))
        print bob.inflate(-x)
    if choice==3:
        print bob.pop()
    if choice==4:
        print bob.bounce()
    if choice==5:
        print bob.patch()
    if choice==6:
        print bob
    if choice==7:
        sys.exit()
    else:
        print "That is an invalid input"

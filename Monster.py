#Dragon


#What makes a dragon a dragon
##breathType
##size
##hasWings
##numHeads

#What info do we want when building


class Dragon:
    def __init__(self,color="Red",breathType="Fire",size=50,numHeads=1,hasWings=True):
        self.breathType=breathType
        self.color=color
        self.size=size
        self.numHeads=numHeads
        self.hasWings=hasWings
    def __str__(self):
        output="I am a",self.breathType+"breathing dragon with",str(numheads),"heads and "
        if self.hasWings:
            output+=
        
    def jumpOffCliff(self):
        if self.hasWings==True:
            print "Flap Flap"
        else: print "FUCK!!!"

##"Red","Ice",50,1,True
bob=Dragon()
bob.jumpOffCliff()

class Room:
    def __init__(self,name,desc):
        self.north=None
        self.east=None
        self.west=None
        self.south=None
        self.desc=desc
        self.hasStuff=False
        self.name=name
    def __str__(self):
        return self.name+"\n"+self.desc
    def __repr__(self):
        return str(self)
    def visit(self,hasKey):
            print "\nYou are in the "+self.name+"."
            print self.desc
            prompt=(raw_input("\nWhat do you want to do: ")).strip()
            prompt+="failsafe"
            prompt=prompt[0].lower()
            if prompt=="w":
                if self.west!=None:
                    self.west.visit(hasKey)
                    return 
                else:
                    print "there is no door there"
                    self.visit(hasKey)
                    return 
            elif prompt=="e":
                if self.east!=None:
                    self.east.visit(hasKey)
                    return
                else:
                    print "there is no door there"
                    self.visit(hasKey)
                    return 
            elif prompt=="n":
                if self.north!=None:
                    (self.north).visit(hasKey)
                    return 
                else:
                    print "there is no door there"
                    self.visit(hasKey)
                    return 
            elif prompt=="s":
                if self.south!=None:
                    self.south.visit(hasKey)
                    return 
                else:
                    print "there is no door there"
                    self.visit(hasKey)
                    return
            elif prompt=="i":
                if self==kitchen and hasKey:
                    print "You found the exit, you win!"
                    import sys
                    sys.exit(0)
                    return
                elif self.hasStuff:
                    self.interact()
                    self.visit(hasKey)
                    return
                else:
                    print "There is nothing in the room to interact with"
                    self.visit(hasKey)
                    return
                    
            else:
                print "learn to follow directions"
                self.visit(hasKey)
                return 
        
    def interact(self):
        print "You found the key!!!"
        hasKey=True
        self.hasStuff=False
        self.visit(hasKey)
        return 

    
diningRoom=Room("Dining Room","You see a dining room with chairs and tables knocked over")
morgue=Room("Morgue","You step on a skull.")
dungeon=Room("Dungeon","You see a dragon.")
entrance=Room("building","The door closes behind you.")
red=Room("Red Room","You see a blood stain on the wall.")
pool=Room("Pool", "You see a dirty, half-filled pool.")
cellar=Room("Cellar", "You see rats.")
kitchen=Room("Kitchen", "You see knives everywhere.")
lab=Room("Lab", "You see deadly chemicals.")
library=Room("Library", "You see a bunch of empty shelves.")
leave=Room("Exit hall", "winner")

entrance.south=lab
entrance.west=cellar
entrance.east=pool
entrance.north=diningRoom

cellar.south=morgue
cellar.west=kitchen
cellar.east=dungeon
cellar.north=library

pool.west=red
pool.south=morgue
pool.east=library
pool.north=red

red.west=diningRoom
red.north=kitchen
red.east=diningRoom
red.south=pool

diningRoom.west=library
diningRoom.north=lab
diningRoom.east=red
diningRoom.south=diningRoom

library.west=pool
library.north=morgue
library.east=diningRoom
library.south=cellar
library.hasStuff=True

morgue.west=pool
morgue.north=dungeon
morgue.east=lab
morgue.south=library

lab.west=morgue
lab.north=red
lab.east=kitchen
lab.south=diningRoom

kitchen.west=lab
kitchen.north=cellar
kitchen.east=diningRoom
kitchen.south=red

dungeon.west=cellar
dungeon.north=lab
dungeon.south=kitchen
dungeon.east=red



##GAME
hasKey=False
print "You must find the key and then the secret exit"
print "Your controls are: \nI: Interact\nN: Go North\nS: Go South\nE: Go East\nW: go West\n\nYou walk into an old building"
self=entrance.visit(hasKey)



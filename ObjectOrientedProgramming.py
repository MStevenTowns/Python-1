#OOP
import math
#class is a skeleton/blueprint for an object
class Point:
    #Constuctor function (2underscores init 2underscores)
    def __init__(self,x,y):#values are stored into self
        self.x=x
        self.y=y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def distanceFromOrigin(self):
        d=math.sqrt((self.x**2)+(self.y**2))
        return d
    def distanceFromPoint(self,p):
        x1=self.x
        x2=p.x
        y1=self.y
        y2=p.y
        d=math.sqrt((x1-x2)**2+(y1-y2)**2)
        return d

p=Point(3,4)
p2=Point(7,4)
print p.getX()
print p.getY()
print p.distanceFromOrigin()
print p.distanceFromPoint(p2)

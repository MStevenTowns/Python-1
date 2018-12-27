class Point:
    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __str__(self):
        return "("+str(self.x)+", "+str(self.y)+")"

    def halfway(self, target):
         mx = (self.x + target.x)/2
         my = (self.y + target.y)/2
         return Point(mx, my)
##Problem 2
    def reflect_x(self):
         return Point(self.x,-self.y)

##Problem 4
    def get_line_to(self,a):
        rise=float(self.getY()-a.getY())
        run=float(self.getX()-a.getX())
        slope=rise/run
        b=self.getY()-(slope*self.getX())
        return Point(slope,b)

p = Point(3,4)
q = Point(5,12)
print p.reflect_x()
print p.get_line_to(q)

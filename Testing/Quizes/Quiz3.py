import math
class Circle:
    def __init__(self, radius):
        self.radius=radius
    def __str__(self):
        output= "I am a circle with radius of "+str(self.radius)+"."
        return output
    def area(self):
        return math.pi*(self.radius**2)
c=Circle(5)
print c
print c.area()

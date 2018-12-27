class Rectangle:
    def __init__(self,l,w):
        self.l=l
        self.w=w
    def __str__(self):
        return "I am a rectangle with sides of length "+str(self.l)+" and "+str(self.w)+"."
    def perimeter(self):
        return (self.l+self.w)*2
        

r=Rectangle(5,7)
print r.perimeter()
print r

"""
24
I am a rectangle with sides of length 5 and 7
"""

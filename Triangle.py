import math
   
class Triangle:
    def __init__(self,p1,p2,p3):
        self.p1=p1
        self.p2=p2
        self.p3=p3
    def __str__(self):
        out= "\nYour triangle's information:"
        out+="\nThe perimeter is: "+str('{0:.3g}'.format(t.perimeter()))
        out+="\nThe area is: "+str('{0:.3g}'.format(t.area()))
        sides=""
        for elem in t.lengths():
            sides+=str('{0:.3g}'.format(elem))+" "
        out+="\nThe side lengths are: "+sides
        angles=""
        for elem in t.angles():
            angles+=str('{0:.3g}'.format(elem))+" "
        out+="\nThe Angles are: "+angles
        if t.isEquilateral(): out+= "\nIt is an equilateral triangle"
        if t.isIsosceles(): out+="\nIt is an isosceles triangle"
        if t.isRight(): out+= "\nIt is a right triangle"
        return out


    def length1(self):
        return math.sqrt(self.length1_squared())
    
    def length2(self):
        return math.sqrt(self.length2_squared())

    def length3(self):
        return math.sqrt(self.length3_squared())
    
    def length1_squared(self):
        x1,y1=self.p1
        x2,y2=self.p2
        x=((x2-x1)**2)
        y=((y2-y1)**2)
        return x+y

    def length2_squared(self):
        x1,y1=self.p2
        x2,y2=self.p3
        x=((x2-x1)**2)
        y=((y2-y1)**2)
        return x+y

    def length3_squared(self):
        x1,y1=self.p1
        x2,y2=self.p3
        x=((x2-x1)**2)
        y=((y2-y1)**2)
        return x+y

    def angle1(self):#Biggest
        a,b,c=self.lengths_squared()
        top=a+b-c
        bottom=2*math.sqrt(a)*math.sqrt(b)
        out=math.degrees(math.acos(math.radians(top/bottom)))
        return out
    
    def angle2(self):
        a,b,c=self.lengths_squared()
        top=self.angle1()
        top=math.radians(top)
        top=math.sin(top)
        top=math.sqrt(b)*top
        out=top/math.sqrt(c)
        out=math.asin(out)
        out=math.degrees(out)
        return out
    
    def angle3(self):
        out=180-self.angle1()-self.angle2()
        return out

    
    def lengths(self):##
        a=[self.length1(),self.length2(),self.length3()]
        a.sort()
        return a
    def angles(self):
        a=[self.angle1(),self.angle2(),self.angle3()]
        return a
    def lengths_squared(self):
        a=[self.length1_squared(),self.length2_squared(),self.length3_squared()]
        a.sort()
        return a

    def perimeter(self):
        l1,l2,l3=self.lengths()
        return l1+l2+l3

    def area(self):
        per=self.perimeter()/2
        a=self.length1()
        b=self.length2()
        c=self.length3()
        x=math.sqrt(per*(per-a)*(per-b)*(per-c))
        return x
    def isEquilateral(self):
        out=False
        if self.length1_squared()==self.length2_squared():
            if self.length1_squared()==self.length3_squared():
                out=True
        return out
    def isIsosceles(self):
        out=False
        if self.length1_squared()==self.length2_squared():
            out=True
        elif self.length1_squared()==self.length3_squared():
            out=True
        elif self.length2_squared()==self.length3_squared():
            out=True
        return out
    def isRight(self):
        out=False
        a,b,c=self.lengths_squared()
        if c==a+b: out= True
        return out
go=True
while (go):
    a=raw_input("Point 1: Give me 2 numbers seperate by a space: ")
    a=a.split()
    x=int(a[0]),int(a[1])
    a=raw_input("Point 2: Give me 2 numbers seperate by a space: ")
    a=a.split()
    y=int(a[0]),int(a[1])
    a=raw_input("Point 3: Give me 2 numbers seperate by a space: ")
    a=a.split()
    z=int(a[0]),int(a[1])
    run=True
    if x[0]==y[0]==z[0]:run==False
    elif x[1]==y[1]==z[1]:run==False
    if run:
        t=Triangle(x,y,z)
        print t
    else: "That is an invalid input"
    choice=(raw_input("\nWould you like another triangle?: ")).strip().lower()
    if choice[0]=="n":
        print "Goodbye"
        go=False
            


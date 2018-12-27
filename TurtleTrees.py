
"""
M. Steven Towns
Assignment 20
Recursive Trees
"""

def drawTree(t,depth,length,rightAngle,leftAngle,dropL,dropR):
    if depth==0:
        t.color("dark green")
        return
    t.width(depth+1)
    t.forward(length)
    t2=t.clone()
    t.left(leftAngle)
    t2.right(rightAngle)
    drawTree(t, depth-1, length*dropL,rightAngle,leftAngle,dropL,dropR)
    drawTree(t2, depth-1, length*dropR,rightAngle,leftAngle,dropL,dropR)
def drawRandomTree(t,depth,length,rightAngle,leftAngle,dropL,dropR):
    if depth==0:
        t.color("dark green")
        t.write("haha")
        return
    t.width(depth+1)
    t.forward(length)
    t2=t.clone()
    t.left(leftAngle)
    t2.right(rightAngle)
    drawRandomTree(t, depth-1, length*dropL,random.randint(0,60),random.randint(0,60),dropL,dropR)
    drawRandomTree(t2, depth-1, length*dropR,random.randint(0,60),random.randint(0,60),dropL,dropR)    



import turtle, random,sys
go=True
while (go):
    choice=int(raw_input("1: Draw Your tree\n2: Draw a random tree\n3: Draw my Tree\n4: Quit\nWhat do you want to do?: "))
    turtle.clearscreen()
    bob=turtle.Turtle()
    bob.shape("turtle")
    screen=bob.getscreen()
    screen.tracer(1000)
    bob.speed(0)
    bob.left(90)
    bob.up()
    bob.back(200)
    bob.down()
    if choice==1:
        rightAngle=raw_input("Give me the right angle: ")
        if rightAngle=="": rightAngle=30
        rightAngle=int(rightAngle)
        leftAngle=raw_input("Give me the left angle: ")
        if leftAngle=="": leftAngle=60
        leftAngle=int(leftAngle)
        length=raw_input("Give me the initial length: ")
        if length=="": length=100
        length=int(length)
        drop=raw_input("Give me the left percent drop in lenght: ")
        if drop=="": drop=60.0
        dropL=float(drop)/100
        drop=raw_input("Give me the right percent drop in lenght: ")
        if drop=="": drop=80.0
        dropR=float(drop)/100
        depth=raw_input("give me the number of calls: ")
        if depth=="": depth=7
        depth=int(depth)
        drawTree(bob,depth,length,rightAngle,leftAngle,dropL,dropR)
    elif choice==2:
        rightAngle=random.randint(30,60)
        leftAngle=random.randint(30,60)
        length=random.randint(50,200)
        depth=random.randint(5,10)
        dropL=random.randint(50,100)*1.0/100
        dropR=random.randint(50,100)*1.0/100
        drawRandomTree(bob,depth,length,rightAngle,leftAngle,dropL,dropR)
    elif choice==3:
        rightAngle=30
        leftAngle=60
        length=100
        dropL=.6
        dropR=.8
        depth=10
        drawTree(bob,depth,length,rightAngle,leftAngle,dropL,dropR)
    else:
        sys.exit()
    screen.update()
    print
turtle.done()

import turtle

def drawSpiral(t, depth,length):
    if depth==0: return
    t.forward(length)
    t.left(90)
    drawSpiral(t,depth-1,length+5)

def drawTree(t,depth):
    if depth==0:
        t.pencolor("green")
        return
    t.width(depth)
    t.forward(10*depth)
    t2=t.clone()
    t.left(45)
    t2.right(45)
    drawTree(t,depth-1)
    drawTree(t2,depth-1)

def drawFancyTree(t,depth,length):
    if depth==0: return
    t.forward(length)
    t2=t.clone()
    t.left(60)
    t2.right(30)
    drawFancyTree(t,depth-1,length*.8)
    drawFancyTree(t2,depth-1,length*.8)

bob=turtle.Turtle()
bob.shape("turtle")
screen=bob.getscreen()
screen.tracer(1000)
bob.speed(0)
bob.left(90)
bob.back(1000)
bob.forward(1000)
bob.pencolor(.4,.4,.4)




##drawFancyTree(bob,10,100)
screen.update()
turtle.done()

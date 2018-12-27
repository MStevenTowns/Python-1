def hanoi(n, startPeg=1, endPeg=3):
    if n:
        hanoi(n-1, startPeg, 6-startPeg-endPeg)
        print("Move disk %d from peg %d to peg %d" %(n, startPeg, endPeg))
        hanoi(n-1,6-startPeg-endPeg, endPeg)
hanoi(n=4)

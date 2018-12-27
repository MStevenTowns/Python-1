#1)
f=file("nums.txt")

#2)
number=0
for line in f:
    number+=int(line)
print number

#3)
f.close()

#4)
s="ann bob carl derrk"
s=s.split(" ")
for i in s:
    print i

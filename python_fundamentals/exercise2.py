a = 3 #a=3 b=None c=None
c = 0 #a=3 b=None c=0
b = a #a=3 b=3 c=0
c = a + b #a=3 b=3 c=6
b = 2 #a=3 b=2 c=6
a = b #a=2 b=2 c=6
b = c #a=2 b=6 c=6
c = a #a=2 b=6 c=2
a = b + (c + a) #a=10 b=6 c=2
print("a= "+str(a)+", b= "+str(b)+", c= "+str(c))
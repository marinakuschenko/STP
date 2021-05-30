import math
a=float(input("a="))
b=float(input("b="))
c=float(input("c="))

if a!=0 and b!=0 and c!=0:
    D=b*b-4*a*c
    if D>0:
        x1=(-b+math.sqrt(D))/2*a
        x2=(-b-math.sqrt(D))/2*a
        print(x1,x2)
    if D==0:
        x1=-b/2*a
        print(x1)
    if D<0:
        print("Корней нет")
        
if b!=0 and c==0:
   #a*math.pow(x)+b*x==0
   x1=0
   x2=b
   print(x1,x2)
if a!=0 and b==0 and c!=0:
    if c<0:
        x1=math.sqrt(c/a)
        x2=-math.sqrt(c/a)
        print(x1,x2)
    if c>0:
        print("Корней нет")
if  b==0 and c==0:
    print(x1=0)

if a==0 and b!=0 and c!=0:
    x=-c/b
    print(x)

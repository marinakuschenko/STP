import math
num=input("1-через длины сторон 2-Через координаты вершин ")
if num=="1":
    a=float(input("a="))
    b=float(input("b="))
    c=float(input("c="))
    p=(a+b+c)/2
    S=math.sqrt(p*(p-a)*(p-b)*(p-c))
    print(S)

if num=="2":
    
    x1, y1=input("A B ").split()
    x2, y2=input("B C ").split()
    x3, y3=input("C A ").split()
    x1=int(x1)
    x2=int(x2)
    x3=int(x3)
    y1=int(y1)
    y2=int(y2)
    y3=int(y3)
   
    arr=[x1-x3,y1-y3,x2-x3,y2-y3]

    res=arr[0]*arr[3]-arr[2]*arr[1]
    S=1/2*math.fabs(res)
    print(S)

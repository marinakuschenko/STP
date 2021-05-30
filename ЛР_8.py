a,x,b=input("").split()
a=float(a)
b=float(b)
if x=="+":
    print(a+b)
elif x=="-":
    print(a-b)
elif x=="*":
    print(a*b)
elif x=="/":
    print(a/b)
else:
    print ("ERROR. Выберите одну из операций + - * /")

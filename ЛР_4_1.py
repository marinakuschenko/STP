try:
    a=int(input("a="))
    b=int(input("b="))
except:
    print("Введите число")
c=a
a=b
b=c
print(a,b)

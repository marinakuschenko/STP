try:
    a=int(input("a="))
    b=int(input("b="))
except:
    print("Введите число")

a,b=b,a
print(a,b)

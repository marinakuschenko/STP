n = int ( input ("Введите число: "))

for a in range (2, n):
    if (n % a) == 0:
        print ("Составное")
        break
    elif (n // a) == 1:
        print ("Простое")
        break 

        

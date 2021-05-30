from itertools import permutations
from itertools import product

n=int(input("Количество символов "))
s=list(input("Введите символы "))

if n == len(s) or n < len(s):
    comb = list(permutations(s, n))
    for i in list(comb):
        for j in i:
            print(j, end="")
        print(" ", end="")
else:
    comb = list(product(s, repeat=n))
    del comb[0]
    del comb[len(comb) - 1]
    for i in list(comb):
        for j in i:
            print(j, end="")
        print(" ", end="")

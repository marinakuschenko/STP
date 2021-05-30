import string
import random
count=int(input("Количество билетов:"))
arr=["bc3355661","ac2155661", "bc3355661", "ac2156661","fh8546952","bc3355668"]

del arr[count:]
print(arr)

for word in arr:
    if len(word)==9:
        num=word[4:9]
        if(word[0]=="a") and ("55661" in num):
            print(word)
        else:
            print("-1")

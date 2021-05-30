import math
print("Введите время в формате DD:MM:")
h1, m1 = map(int, input().split(":"))
h2, m2 = map(int, input().split(":"))
h1=int(h1)
h2=int(h2)
m1=int(m1)
m2=int(m2)
    
if (h1 and h2)>=0 and (h1 and h2)<=23 and (m1 and m2)>=0 and (m1 and m2)<=60:
    res=((h2-h1)*3600+(m2-m1)*60)/60
    if res>15:
        print("Встреча не состоится")
    else: print("Встреча состоится")

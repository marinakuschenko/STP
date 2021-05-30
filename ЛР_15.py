import random


#for i in range(1,100):
def goal():
    num=random.randint(1,100)
    print(num)
    
    count=1
    while count<=5:
        print("Попытка ",count)
        inp=int(input("Введите предполагаемое число: "))
        count+=1
        if inp==num:
            print("Вы попали в цель!")
            return
        elif inp<num:
            print("Загаданное число больше")
        elif inp>num:
            print("Загаданное число меньше")
           
    print("Вы проиграли. Было загадано:",num)
goal()

print("Хотите начать сначала? (1 - ДА )")
new=int(input())
if new==1:
    goal();
    

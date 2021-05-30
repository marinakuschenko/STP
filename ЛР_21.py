def imt(weight: float, height: float) -> float:
    return weight / pow(height, 2)


def imtPrint(imt: float) -> float:
    if imt < 18.5:
        print("Underweight")
    elif imt < 25.0:
        print("Normal")
    elif imt < 30.0:
        print("Overweight")
    else:
        print("Obesity")


print("Введите вес и рост")

weight, height = map(int, input().split())
height /= 100
i = imt(weight, height)
imtPrint(i)

for k in range(1, 10):
    if k == 1:
        print(str(k) + " год")
    elif k in [2, 3, 4]:
        print(str(k) + " года")
    elif k in [5, 6, 7, 8, 9]:
        print(str(k) + " лет")
    else:
        print("Непонятное значение")

print("################")

for k in range(1, 10):
    if k == 1:
        print(str(k) + " год")
    elif k == 2 or k == 3 or k == 4:
        print(str(k) + " года")
    elif k == 5 or k == 6 or k == 7 or k == 8 or k == 9:
        print(str(k) + " лет")
    else:
        print("Непонятное значение")

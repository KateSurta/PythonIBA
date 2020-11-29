import random
n = int(input("Введите размер списка "))
listIntA = []
listIntB = []
for listValue in range(n):
    listValue = random.randint(0, 99)
    listIntA.append(listValue)
print("Исходный лист: " + str(listIntA))

for i in range(n):
    value = listIntA[i]
    if value % 2 == 0:
        listIntB.append(value)

print("Четные значения: " + str(listIntB))




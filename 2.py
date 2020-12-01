firstSide = 7
secondSide = 4
countOfSuare = 1


def cutofsquare(a, b):
    print("Исходный размер прямоугольника: " + str(a) + "*" + str(b))
    maxside = max(a, b)
    minside = min(a, b)
    print("Размер квадрата: " + str(minside) + "*" + str(minside))
    if a == b:
        return 1
    else:
        a = maxside - minside
        b = minside
        return 1 + cutofsquare(a, b)


print("Кол-во квадратов: " + str(cutofsquare(firstSide, secondSide)))



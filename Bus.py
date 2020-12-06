from datetime import datetime


def printBusList(listbus):
    for bus in listbus:
        print(bus.toPrint())


class Bus:
    __FIO = ""
    __busNumber = 0
    __numberOfWay = 0
    __carBrand = ""
    __yearOfOperation = 0
    __mileage = 0
    __listOfBuses = []

    # конструктор
    def __init__(self, fio, number, waynumber, brand, yearofoperation, mil):
        self.__FIO = fio
        self.__busNumber = number
        self.__numberOfWay = waynumber
        self.__carBrand = brand
        self.__yearOfOperation = yearofoperation
        self.__mileage = mil

    # получение полей класса
    def get_FIO(self):
        return self.__FIO

    def get_busNumber(self):
        return self.__busNumber

    def get_numberOfWay(self):
        return self.__numberOfWay

    def get_carBrand(self):
        return self.__carBrand

    def get_yearOfOperation(self):
        return self.__yearOfOperation

    def get_mileage(self):
        return self.__mileage

    # смена полей класса
    def set_FIO(self, person):
        self.__FIO = person

    def set_busNumber(self, number):
        self.__busNumber = number

    def set_numberOfWay(self, waynumber):
        self.__numberOfWay = waynumber

    def set_carBrand(self, brand):
        self.__carBrand = brand

    def set_yearOfOperation(self, yearofoperation):
        self.__yearOfOperation = yearofoperation

    def set_mileage(self, mil):
        self.__mileage = mil

    def ageOfBus(self):
        currentYear = datetime.now().year
        year = currentYear - self.get_yearOfOperation()
        return year

    def toPrint(self):
        return self.get_FIO() + "," + str(self.get_busNumber()) + "," + str(self.get_numberOfWay()) + \
               "," + self.get_carBrand() + "," + str(self.get_yearOfOperation()) + "," + str(self.get_mileage())


# присвоение и вывод полученных полей класса
Bus1 = Bus("Kate D", 2835, 375, "МАЗ 203", 1987, 450000)
Bus2 = Bus("Kate S", 2837, 37, "МАЗ 208", 1988, 350000)
Bus3 = Bus("Kate M", 2537, 20, "МАЗ 210", 1998, 150000)
Bus4 = Bus("Kate G", 2877, 40, "МАЗ 230", 1992, 100000)
print("--------------------------------")
print("Фио водителей автобусов: " + "\n" + str(Bus1.get_FIO()) + "\n" + str(Bus2.get_FIO()) + "\n" + str(
    Bus3.get_FIO()) + "\n"
      + str(Bus4.get_FIO()))
print("Номера автобусов: " + "\n" + str(Bus1.get_busNumber()) + "\n" + str(Bus2.get_busNumber()) + "\n" +
      str(Bus3.get_busNumber()) + "\n" + str(Bus4.get_busNumber()))
print("Номера маршрутов: " + "\n" + str(Bus1.get_numberOfWay()) + "\n" + str(Bus2.get_numberOfWay()) + "\n" +
      str(Bus3.get_numberOfWay()) + "\n" + str(Bus4.get_numberOfWay()))
print("Марки автобусов " + "\n" + str(Bus1.get_carBrand()) + "\n" + str(Bus2.get_carBrand()) + "\n" +
      str(Bus3.get_carBrand()) + "\n" + str(Bus4.get_carBrand()))
print("Год начала эксплуатации автобусов " + "\n" + str(Bus1.get_yearOfOperation()) + "\n" + str(
    Bus2.get_yearOfOperation()) + "\n" +
      str(Bus3.get_yearOfOperation()) + "\n" + str(Bus4.get_yearOfOperation()))
print("Пробег автобусов " + "\n" + str(Bus1.get_mileage()) + "\n" + str(Bus2.get_mileage()) + "\n" +
      str(Bus3.get_mileage()) + "\n" + str(Bus4.get_mileage()))
print("---------------------------------")

# set новые данные
Bus1.set_FIO("Make S")
Bus2.set_busNumber(2567)
Bus3.set_numberOfWay(47)
Bus2.set_carBrand("МАЗ 221")
Bus4.set_yearOfOperation(1994)
Bus1.set_mileage(475000)
print("-------------Новые данные-------------------")
print("Фио водителей автобусов: " + "\n" + str(Bus1.get_FIO()) + "\n" + str(Bus2.get_FIO()) + "\n" + str(
    Bus3.get_FIO()) + "\n"
      + str(Bus4.get_FIO()))
print("Номера автобусов: " + "\n" + str(Bus1.get_busNumber()) + "\n" + str(Bus2.get_busNumber()) + "\n" +
      str(Bus3.get_busNumber()) + "\n" + str(Bus4.get_busNumber()))
print("Номера маршрутов: " + "\n" + str(Bus1.get_numberOfWay()) + "\n" + str(Bus2.get_numberOfWay()) + "\n" +
      str(Bus3.get_numberOfWay()) + "\n" + str(Bus4.get_numberOfWay()))
print("Марки автобусов " + "\n" + str(Bus1.get_carBrand()) + "\n" + str(Bus2.get_carBrand()) + "\n" +
      str(Bus3.get_carBrand()) + "\n" + str(Bus4.get_carBrand()))
print("Год начала эксплуатации автобусов " + "\n" + str(Bus1.get_yearOfOperation()) + "\n" + str(
    Bus2.get_yearOfOperation()) + "\n" +
      str(Bus3.get_yearOfOperation()) + "\n" + str(Bus4.get_yearOfOperation()))
print("Пробег автобусов " + "\n" + str(Bus1.get_mileage()) + "\n" + str(Bus2.get_mileage()) + "\n" +
      str(Bus3.get_mileage()) + "\n" + str(Bus4.get_mileage()))

# Создание листа автобусов
listOfBuses = [
    Bus1, Bus2, Bus3, Bus4]

print("Лист автобусов ")

printBusList(listOfBuses)

print("---------------------------------")

# Получение возраста автобусов
print("---------------------------------")
ageBus1 = Bus1.ageOfBus()
ageBus2 = Bus2.ageOfBus()
ageBus3 = Bus3.ageOfBus()
ageBus4 = Bus4.ageOfBus()
print("Возраст 1-го автобуса: " + str(ageBus1))
print("Возраст 2-го автобуса: " + str(ageBus2))
print("Возраст 3-го автобуса: " + str(ageBus3))
print("Возраст 4-го автобуса: " + str(ageBus4))
print("---------------------------------")


# список автобусов для заданного номера маршрута
def getBusByWay(listbus, way):
    newListOfBussesByWay = []
    for buses in listbus:
        num = buses.get_numberOfWay()
        if way == num:
            newListOfBussesByWay.append(buses)
    return newListOfBussesByWay


# список автобусов, которые эксплуатируются больше заданного срока
def getBusByTime(listbus, time):
    newListOfBussesByTime = []
    for busses in listbus:
        timebus = busses.ageOfBus()
        if timebus > time:
            newListOfBussesByTime.append(busses)
    return newListOfBussesByTime


print("Лист втобусов следующих по маршруту 40: ")
printBusList(getBusByWay(listOfBuses, 40))
print("---------------------------------")

print("Лист втобусов которые в ходу больше 30 лет: ")
printBusList(getBusByTime(listOfBuses, 30))
print("---------------------------------")

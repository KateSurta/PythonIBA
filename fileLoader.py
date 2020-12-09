import io
import re

file1 = "F1.txt"
file2 = "F2.txt"

try:
    load_file = io.open(file1, "r")
    print("File 1: " + "\n")
    fileContent = load_file.readlines()
    for i in range(len(fileContent)):
        line = fileContent[i].rstrip('\n')
        result = re.findall('[0-9]', line)
        if not result:
            copy_to_file = io.open(file2, "a")
            copy_to_file.writelines(line + "\n")
            copy_to_file.close()
        else:
            print(str(line) + " это же число!")
except FileNotFoundError:
    print("File not found")

try:
    copy_file = io.open(file2, "r")
    print("File 2: " + "\n")
    fileContent = copy_file.readlines()
    count = 0
    for i in range(len(fileContent)):
        line = fileContent[i].rstrip('\n')
        result = re.findall('A', line)
        if not result:
            print(str(line) + " - не подходит")
        else:
            count += 1
        newCount = count

    print("Кол-во имён на букву А: " + str(count))
except FileNotFoundError:
    print("File not found")

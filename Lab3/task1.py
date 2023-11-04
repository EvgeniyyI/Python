F1 = open("F1.txt", "w+", encoding='utf-8')

line = input("Введите строку:")
while line != "":
    F1.write(line + "\n")
    line = input("Введите строку:")

F1.seek(0)
value = F1.readlines()
F1.close()

try:
    string1 = int(input("Введите номер первой строки:"))
    string2 = int(input("Введите номер второй строки:"))
except ValueError as v:
    print("Ошибка:", v)
except NameError as n:
    print("Ошибка:", n)

F2 = open("F2.txt", "w", encoding='utf-8')

if string1 == string2 + 1:
    print("Между строк нет элементов!")
    exit()
if string2 <= string1:
    print("Второе значение должно быть больше первого!")
    exit()
if string1 > 0:
    string1 -= 1

try:
    for line in range(string1 + 1, string2 - 1):
        if value[line][0] == "A":
            F2.write(value[line])
    print("Строки успешно скопированы в файл!")
except IndexError as i:
    print("Ошибка:", i)
except Exception as e:
    print("Ошибка:", e)
finally:
    F2.close()
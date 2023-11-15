import random


def find_nod(x, y):
    nod = 0
    if x > y:
        temp = y
    else:
        temp = x
    try:
        for i in range(1, temp + 1):
            if x % i == 0 and y % i == 0:
                nod = i
    except Exception:
        print("Ошибка!")
    else:
        return nod


def second_task(value):
    if isinstance(value, dict):
        try:
            d = sorted(value.items(), key=lambda d: d[1])
        except Exception:
            print("Ошибка!")
        else:
            print("Три ключа с самыми маленькими значениями:", d[0:3], "\n\n")

    elif isinstance(value, list):
        while 0 in value:
            value.remove(0)
        print("Список без нулей: ", value)
        first_index = second_index = -1
        result = 1
        for i in range(len(value)):
            if value[i] > 0:
                first_index = i
                break
        if first_index == -1:
            print("Нет положительных элементов.\n\n")
        else:
            for i in range(first_index + 1, len(value)):
                if value[i] > 0:
                    second_index = i
                    break
            if second_index == -1:
                print("Только один положительный элемент.\n\n")
            elif first_index == second_index + 1:
                print("Элементы стоят рядом.\n\n")
            else:
                for i in range(first_index, second_index):
                    result *= value[i]
                print("Произведение между первым и вторым положительными элементами: ", result, "\n\n")

    elif isinstance(value, int):
        print("Число:", value)
        count = 0
        value = abs(value)
        while value > 0:
            value //= 10
            count += 1
        print("Количество разрядов:", count, "\n\n")

    elif isinstance(value, str):
        print("Строка:", value)
        for i in value:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        print(d, "\n\n")


def menu_second_task():
    while True:
        print('''   1.Словарь. 
   2.Список.
   3.Число.
   4.Строка.
   5.Выход.''')
        choice2 = make_choice()
        if choice2 == 5:
            return
        elif choice2 == 1:
            dictionary = {1: 10, 2: 5, 3: 6, 4: 7, 5: 8}
            print("\n\nСловарь:", dictionary)
            second_task((dictionary))
        elif choice2 == 2:
            lst = [0, 1, -1, -2, -3, -1, 3, 0, 4, 5, 6, 0, 0, 10]
            print("\n\nСписок:", lst)
            second_task(lst)
        elif choice2 == 3:
            number = -1234
            second_task(number)
        elif choice2 == 4:
            string = "qweasdwwe"
            second_task(string)


def third_task(arr):
    min_value = arr[0][0]
    max_value = arr[0][0]

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if min_value > arr[i][j]:
                min_value = arr[i][j]
                index_min = (i, j)
            if max_value < arr[i][j]:
                max_value = arr[i][j]
                max_i = i
                max_j = j

    print("Минимальный элемент =", min_value, "\nИндекс:", index_min)
    print("Максимальный элемент =", max_value, "\nИндекс:", max_i, ",", max_j)


def index_error():
    elements = [random.randint(10, 50) for i in range(10)]
    print("Список: ", elements)
    try:
        el = int(input("Введите индекс элемента: "))
        print("Элемент по индексу", el, "равен", elements[el])
    except ValueError:
        print("Некорректный ввод данных!")
    except IndexError:
        print("Нет такого индекса!")
    finally:
        print("Функция завершена.")


def make_choice():
    while True:
        try:
            choice = int(input("Ваш выбор:"))
        except ValueError:
            print("Некорректный ввод! Повторите действие.")
        else:
            if choice < 1 or choice > 5:
                print("Введите чило от 1 до 5.")
            else:
                return choice


while True:
    print("=======================Задания=======================")
    print('''             1.Наибольший общий делитель.
             2.Задание 2.
             3.Найти мин. и макс. элементы матрицы.
             4.Программа try/except/finally.
             5.Выход.''')
    print("======================================================")
    choice = make_choice()

    if choice == 5:
        break

    elif choice == 1:
        x = int(input("Введите первое число: "))
        y = int(input("Введите второе число: "))
        nod = find_nod(x, y)
        print("Наибольший общий делитель =", nod)

    elif choice == 2:
        menu_second_task()

    elif choice == 3:
        array = [[random.randint(0, 10) for i in range(5)] for j in range(5)]
        print("Матрица:")
        for row in array:
            print(row)
        try:
            third_task(array)
        except Exception as e:
            print("Ошибка!", e)

    elif choice == 4:
        index_error()
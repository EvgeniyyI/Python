import random

my_list = [random.randint(0, 10) for i in range(10)]
print("Список: ", my_list)

counter = 0
for i in my_list:
    if my_list.count(i) == 1:
        counter += 1
        if counter == 1:
            print("Элементы, которые встерчаются только один раз: ")
        print(i)

if counter == 0:
    print("Нет элементов, которые встречаются только один раз.")

if my_list.count(0) < 2:
    print("В списке нет двух нулей.")
else:
    zero_index = 0
    for i in range(my_list.index(0) + 1, len(my_list)):
        if my_list[i] == 0:
            zero_index = i

    if zero_index - my_list.index(0) == 1:
        print("Между нулями нет элементов.")
    else:
        sum = 0
        for i in range(my_list.index(0), zero_index):
             sum += my_list[i]
        print("Сумма элементов, расположенных между первым и последним нулями равна: ", sum)
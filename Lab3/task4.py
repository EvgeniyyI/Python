import json

try:
    with open("Фирмы", "r", encoding='utf-8') as file_of_firms:
        firms = file_of_firms.readlines()

except Exception as e:
    print("Ошибка:", e)

print("Содержимое файла:\n", *firms)

dictionary = {}
loss_dictionary = {}
profit = {}
list_of_firms = []

for i in firms:
    firm = i.split()
    if (int(firm[2]) - int(firm[3])) < 0:
        loss_dictionary[firm[0]] = int(firm[2]) - int(firm[3])
    else:
        dictionary[firm[0]] = int(firm[2]) - int(firm[3])

profit["average_profit"] = sum(dictionary.values()) / len(dictionary)

print("\nСловарь с прибылью фирм: ", dictionary)
print("Средняя прибыль фирм: ", profit)
print("Словарь с убытком фирм: ", loss_dictionary)

list_of_firms.append(dictionary)
list_of_firms.append(profit)
list_of_firms.append(loss_dictionary)
print("\nИтоговый список: ", list_of_firms)

try:
    with open("f.json", "w") as write_f:
        json.dump(list_of_firms, write_f, indent=4)
except Exception as e:
    print("Ошибка!", e)
else:
    print("Данные успешно записаны в файл!")

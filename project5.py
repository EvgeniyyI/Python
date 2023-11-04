import random

my_list = (random.randint(0, 10) for i in range(10))

my_tuple=tuple(my_list)

print("Кортеж", my_tuple,"\nКоличество нулевых элементов: ", my_tuple.count(0))
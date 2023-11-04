import random

S = ''
counter = 0
while counter < 10:
    i = random.randint(0, 9)
    S += str(i)
    counter += 1

print("Строка:", S)

dictionary = {}

for i in S:
    i = int(i)

    if i in dictionary:
        dictionary[i] += 1
    else:
        dictionary[i] = 1
list=dict(sorted(dictionary.items(), key=lambda d:d[1]))

print(list)
import random

rand_number = random.randint(0, 10)

i = 0
while True:

    i += 1
    number = int(input('Введите число: '))
    if number > rand_number:
        print('Ваше число больше загаданного')
    elif number < rand_number:
        print('Ваше число меньше загаданного')
    else:
       print('\nВы угадали число ', rand_number, ' с ', i, ' попытки!!!')
       break
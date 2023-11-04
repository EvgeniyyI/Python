evens = odds = 0

while True:
    S = input('Введите строку:')
    if ',' in S or '.' in S or'!' in S or'?' in S:
        print('Введите строку без знаков препинания!')
    else: break;


list = S.split()
for i in list:
    if len(i) % 2 == 0:
        evens += 1
    else:
        odds += 1

if evens == 0:
    print('В строке нет чётных слов.')
else:
    print('Количество чётных слов = ', evens)

if odds == 0:
    print('В строке нет нечётных слов.')
else:
    print('Количество нечётных слов = ', odds)
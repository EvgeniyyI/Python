dictionary = {'Торт': [['Бисквит', 'Крем', 'Фрукты'], 10, 1000],
              'Пирожное': [['Глазурь', 'Крем', 'Тесто'], 3, 500],
              'Мороженое': [['Сливки', 'Сахар', 'Глазурь'], 2, 500],
              'Кофе': [['Кофейные зёрна', 'Вода', 'Сливки'], 5, 750],
              'Коктейл': [['Молоко', 'Мороженое'], 4, 750]}
bill_price = {}
bill_quantity = {}
Price = 0
while True:
    print("====================Кондитерская====================")
    print('''             1.Просмотр описания.
             2.Просмотр цены(за 100 грамм).
             3.Просмотр количества(в граммах).
             4.Просмотр всей информации.
             5.Покупка.
             6.Выход.''')
    print("====================================================")
    choice = int(input("Ваш выбор:"))
    if choice == 6:
        break;

    elif choice == 1:
        for i in dictionary:
            print(i, ":", dictionary[i][0])

    elif choice == 2:
        for i in dictionary:
            print(i, ":", dictionary[i][1])

    elif choice == 3:
        for i in dictionary:
            print(i, ":", dictionary[i][2])

    elif choice == 4:
        for i in dictionary:
            print(i, "\nСостав:", dictionary[i][0], "\nЦена(за 100 грамм):", dictionary[i][1],
                  "\nКоличество(в граммах):", dictionary[i][2], "\n1")

    elif choice == 5:
        while True:
            product = input("Введите название продукта:")
            if product == 'n':
                break

            quantity = int(input("Введите количество продукта(в граммах):"))

            if product not in dictionary:
                print("Некорректно введено название продукта!")

            elif quantity % 50 != 0 or quantity < 50:
                print("Количество товара должно быть кратным 50(минимум 50 грамм)")

            else:
                if dictionary[product][2] == 0:
                    print("Данный товар закончился.")

                elif quantity > dictionary[product][2]:
                    print("Слишком большое количество товара, количество товара в кондитерской:",
                          dictionary[product][2])
                else:
                    total_price = dictionary[product][1] * quantity
                    dictionary[product][2] -= quantity
                    if product in bill_price:
                        bill_price[product] += total_price
                        bill_quantity[product] += quantity
                    else:
                        bill_price[product] = total_price
                        bill_quantity[product] = quantity
                    print("\nПокупка успешно выполнена!", "\nКуплено:", product, "\nВ количестве:", quantity, "грамм",
                          "\nЦена покупки:", total_price, "Р\n")

                    print("В кондитерской осталось", dictionary[product][2], "грамм товара", product, "\n")

                    Price += total_price
                    print("Общий чек:")
                    print("___________________________________________________")
                    for i in bill_price:
                        print(i, "-------", "Количество:", bill_quantity[i], "грамм", "Цена:", bill_price[i], "Р", "\n")
                    print("___________________________________________________")
                    print("Сумма покупок: ", Price, "Р", "\n")
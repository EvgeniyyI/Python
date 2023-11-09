class Calculator:
    def sum(self, a, b):
        return a + b

    def difference(self, a, b):
        return a - b

    def multiplication(self, a, b):
        return a * b

    def degree(self, a, b):
        return a ** b

    def division(self, a, b):
        if b == 0:
            return 0
        return a / b


calculation = Calculator()
while True:
    while True:
        try:
            a = int(input("Введите первое число:"))
            sign = input("Введите знак(+, -, *, **, /):")
            b = int(input("Введите второе число:"))
        except Exception as e:
            print("Ошибка!\n", e)
        else:
            break

    if a == 0 and b == 0:
        break

    while sign != '+' and sign != "-" and sign != "*" and sign != "**" and sign != "/":
        print("Неверно введён знак, повторите попытку!")
        sign = input("Введите знак(+, -, *, **, /):")

    if sign == "+":
        print(f"Сумма чисел {a} и {b} равна: {calculation.sum(a, b)}")

    if sign == "-":
        print(f"Разность чисел {a} и {b} равна: {calculation.difference(a, b)}")

    if sign == "*":
        print(f"Произведение чисел {a} и {b} равна: {calculation.multiplication(a, b)}")

    if sign == "**":
        print(f"Число {a} в степени {b} равно: {calculation.degree(a, b)}")

    if sign == "/":
        print(f"Результат деления числа {a} на число {b} равен: {calculation.division(a, b)}")

class Car:
    def __int__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        if self.speed > 0:
            print("Вы уже едете.")
            return
        print("Начало движения...")
        try:
            self.speed = int(input("Укажите скорость."))
        except Exception as e:
            self.speed = 0
            print("Ошибка!")

    def stop(self):
        if self.speed == 0:
            print("Вы уже стоите.")
            return
        print("Остановка...")
        self.speed = 0

    def turn(self, direction):
        if self.speed == 0:
            print("Сначала начните движение.")
            return
        print("Выполняется поворот на", direction)

    def show_speed(self):
        print("Автомобиль движется со скоростью", self.speed)


class TownCar(Car):
    def __init__(self):
        super().__init__(0, "Жёлтый", "Городской автомобиль.", False)

    def show_speed(self):
        print("Автомобиль движется со скоростью", self.speed)
        if self.speed > 60:
            print("Вы превышаете максимально допустимую скорость.")


class SportCar(Car):
    def __init__(self):
        super().__init__(0, "Красный", "Спортивный автомобиль.", False)


class WorkCar(Car):
    def __init__(self):
        super().__init__(0, "Белый", "Рабочий автомобиль.", False)

    def show_speed(self):
        print("Автомобиль движется со скоростью", self.speed)
        if self.speed > 40:
            print("Вы превышаете максимально допустимую скорость.")


class PoliceCar(Car):
    def __init__(self):
        super().__init__(0, "Белый", "Рабочий автомобиль.", True)

    def show_speed(self):
        print("Автомобиль движется со скоростью", self.speed)
        print("Вы можете ехать с любой скоростью.")


while True:
    print("====================Автомобили======================")
    print('''             1.Городской автомобиль.
             2.Спортивный автомобиль.
             3.Рабочий автомобиль.
             4.Полицейский автомобиль.
             5.Выход.''')
    print("====================================================")
    while True:
        try:
            choice = int(input("Ваш выбор:"))
        except ValueError:
            print("Некорректный ввод, повторите попытку")
        except Exception as e:
            print("Ошибка! Повторите попытку")
        else:
            break
    if choice == 5:
        break
    elif choice == 1:
        town_car = TownCar()

    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        pass

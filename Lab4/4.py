class Student:
    max_scholarship = 0

    def __init__(self, name, place_of_study, specialization, GPA, scholarship):
        self.name = name
        self.place_of_study = place_of_study
        self.specialization = specialization
        self.GPA = GPA
        self.scholarship = scholarship

    def print_data(self):
        print(
            f"Студент: {self.name}\n Место учёбы: {self.place_of_study} \n Специальность: {self.specialization}"
            f"\n Средний балл: {self.GPA}\n Стипендия: {self.scholarship}\n Максимально возмонжая стипендия: {self.max_scholarship}")

    @classmethod
    def change_maxscholarship(cls, new_scholarship):
        cls.max_scholarship = new_scholarship

    @staticmethod
    def info():
        print("Зимние экзамены начинаются в январе, а летние экзамены начинаются в июне.")


student1 = Student("1", '1', '1', '1', '1')
student2 = Student("2", '2', '2', '2', '1')
student1.print_data()
student2.print_data()
student1.change_maxscholarship(2)
student1.print_data()
student2.print_data()
Student.info()
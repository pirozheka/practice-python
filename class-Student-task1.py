class Student:
    def __init__(self, name, age, marks):
        if not name:
            raise ValueError("Имя студента должно быть указано.")
        self._name = name
        self._age = age
        self._marks = marks

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def marks(self):
        return self._marks

    def calculate_avg_mark(self):
        if len(self._marks) == 0:
            return 0  # Или другое значение по умолчанию
        sum_mark = sum(self._marks)
        avg_mark = sum_mark / len(self._marks)
        return avg_mark

    def display_avg_mark(self):
        avg_mark = self.calculate_avg_mark()
        print(f"Средняя оценка студента {self._name}: {avg_mark}")
        return avg_mark

    def get_marks(self):
        print(f"Список оценок: {self._marks}")

    def add_mark(self):
        try:
            mark = int(input('Введите оценку от 1 до 10: '))
        except ValueError:
            print("Invalid mark")
            self.add_mark()
        else:
            if 0 < mark <= 10:
                self._marks.append(mark)
            else:
                print("Оценка должна быть меньше 11 и больше 0")
                self.add_mark()
                self.get_marks()


# Пример использования
ivan = Student('Ivan', 25, [5, 5, 2])
print(ivan.name)  # Доступ к свойству name
print(ivan.age)   # Доступ к свойству age
print(ivan.marks) # Доступ к свойству marks
ivan.add_mark()
avg_mark = ivan.display_avg_mark()
print(f"Средняя оценка, возвращенная из метода: {avg_mark}")

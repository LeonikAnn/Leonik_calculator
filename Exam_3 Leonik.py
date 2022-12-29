#1. Напишите функцию, которая запрашивает у пользователя номер карты, CVC-код и PIN-код.
# После этого выводит на экран номер карты с первыми четырьмя цифрами, остальные заменены на звездочки,
# CVC-код в виде ###, и PIN-код в виде &&&0 (вместо 0 последняя цифра).

def personal_info(card, cvc, pin):
    print('Карта:', card[:4]+ '*'*(len(card)-4))
    print('CVC:','#'*len(cvc))
    print('Пин:', '&' * (len(pin)-1) + pin[-1])
personal_info(card= input("Введите номер карты без пробелов и знаков:"),cvc =input('Введите CVC-code:'),pin = input('Введите PIN-code:'))
#
# # #2. Напишите функцию, которая возвращает True, если введенный текст читается одинаково слева-направо и справа-налево.
# # #Иначе – False. Допишите к функции декоратор, который выведет имя функции, ее аргумент.
def decor(func):
    def wrapper(arg):
        print (f' Имя функции: {func.__name__}, Аргумент: {arg}')
        func(arg)
    return wrapper

@decor
def polidrom(p):
    p.replace(' ', '')
    if p == p[::-1]:
       print ('True')
    else: print ('False')

(polidrom(input('Введите cтроку:')))

#Дописать в классы Company, Programmer абстрактные методы (хотя бы 1).
# В коде должны быть Private и Protected методы и свойства
# from abc import abstractmethod
# @abstractmethod
# def salary(self, index):
#         if index == 1:
#             self.salary = Company.default_salary + 1000
#
#         if index == 2:
#             self.salary = Company.default_salary + 2000
#         if index == 3:
#             self.salary = Company.default_salary + 3000
#         if index <= 4:
#             self.salary = Company.default_salary + 5000
class Company:
    default_salary = 1000
    levels= {1:'junior', 2:'middle', 3:'senior', 4:'lead'}
    def __init__(self, index):

        self._index = index
        self._levels =Company.levels[self._index]
        print(self._index, self._levels)
    # def salary(self, index):
    #     return self.salary(1)
    def _level_up(self):
        if self._index < 4:
            self._index +=1
            self._levels = Company.levels[self._index]
            return (f'Вы достигли уровня:{self._index} - {self._levels}')
        elif self._index == 4:
            return ('Достигнута максимальная квалификация')


    def is_lead(self):
        if self._index == 4:
            print ('Последняя квалификация достигнута')
        else: print(f'Ваша квалификация: {self._index}')

codehead = Company(1)
# print(codehead.salary(1))
print(codehead._level_up())
codehead.is_lead()
class Programmer(Company):
    def __init__(self, name, age):
        super().__init__(int(input('Введите ваш уровень:')))
        self. name = name
        self.age = age
        self.level = self.levels
    def work(self):
        print('Working...')
        return self._level_up()

    def info(self):
        print(f'Имя:{self.name}\nВозраст: {self.age}\nКвалификация:{self.level[self._index]}')

    @staticmethod
    def knowledge_base():
        print('''Объектно-ориентированное программирование — это парадигма программирования,\nкоторая позволяет структурировать программы таким образом, что свойства и поведение объединяются в отдельные объекты.\nКлассы используются для создания определяемых пользователем структур данных. Кроме того, классы определяют функции,\nназываемые методами, которые определяют поведение и действия, которые объект, созданный на основе класса, может выполнять с его данными.''')

Anya = Programmer('Anya', 26)
Anya.work()
Anya.info()
Programmer.knowledge_base()



#4. Создайте класс на тему животных. Используйте статические и динамические переменные,
# дочерний (1 или более) классов на конкретное животное. Публичные и приватные методы.
# Полиморфизм (одинаковые названия методов info в обоих классах, которые выводят информацию о животных,
# либо о конкретном животном данного класса). Создайте объекты каждого класса и обратитесь к каждому методу.
# Напишите один staticmethod, один classmethod, к которым также обратитесь.
#
class Bear:
    default_name = 'Kate'
    default_age = 2
    default_color = 'Brown'
    @classmethod
    def default(cls, name = default_name, age = default_age):
        defo = str(name) + str(age)
        return defo


    def __init__(self, name= default_name, age=default_age, color=default_color):
        self.name = name
        self.age = age
        self._color = color
        self.h = 2
        self.l = 1.5
    def _size(self):
        return (f'Длина: {self.l} Высота: {self.h}')

    def info(self):
        print(f'Имя: {self.name}\nВозраст: {self.age}\nЦвет: {self._color}')
    @staticmethod
    def speed(name):
        if name == 'Polar': return ('Средняя скорость белого медведя: 40 км/ч')
        if name == 'Brown': return ('Средняя скорость бурого медведя: 56 км/ч')

class Brown_Bear(Bear):
    def __init__(self, name, age):
        super().__init__()
        self.name = name
        self.age = age
        self.__color = 'Brown'
class Polar_Bear(Bear):
    def __init__(self, name, age):
        super().__init__()
        self._name = name
        self._age = age
        self.__color = 'White'
        self.h = 1
        self.l = 1.5

Asya = Brown_Bear('Asya', 3)
Olivia = Polar_Bear('Olivia', 5)
Asya.info()
Olivia.info()
print(f'Размеры бурого медведя - {Asya._size()}')
print(f'Размеры белого медведя - {Olivia._size()}')
print(Bear.speed(input(f'Введите "Polar" или "Brown"')))
print(Bear.default())
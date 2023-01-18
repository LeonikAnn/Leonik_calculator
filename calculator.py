import sys
import math
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton
from PyQt5 import *
from PyQt5 import QtGui
class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.my_input = '' #результат вычисления
        self.operand1 = 0 #первое значение
        self.operand2 = 0 # второе значение
        self.operation = ''

    def initUI(self): #Внешний вид калькулятора
        self.setGeometry(0, 0, 290, 380)
        self.setWindowTitle('Калькулятор')
        self.label = QLabel(self) #создаем первое поле для ввода/вывода результата
        self.label.setText('0') # Установили начальное значение в окне
        self.label.resize(300, 100) #размер окна
        self.label.move(0,0)

        self.label.setFont(QtGui.QFont('Bradley Hand',25))
        self.label.setStyleSheet('background-color:  Lightblue')



        self.num_1 = QPushButton('1', self)
        self.num_1.resize(50,50)     #размер кнопки
        self.num_1.move(5,100)
        self.num_1.setStyleSheet('background-color: Lightyellow')
        self.num_1.setFont(QtGui.QFont("Bradley Hand", 18))
        self.num_2 = QPushButton('2', self)
        self.num_2.resize(50, 50)  # размер кнопки
        self.num_2.move(60, 100)
        self.num_2.setStyleSheet('background-color: Lightyellow')
        self.num_2.setFont(QtGui.QFont("Bradley Hand", 18))
        self.num_3 = QPushButton('3', self)
        self.num_3.resize(50, 50)  # размер кнопки
        self.num_3.move(115, 100)
        self.num_3.setStyleSheet('background-color: Lightyellow')
        self.num_3.setFont(QtGui.QFont("Bradley Hand", 18))
        self.num_4 = QPushButton('4', self)
        self.num_4.resize(50, 50)  # размер кнопки
        self.num_4.move(5, 155)
        self.num_4.setStyleSheet('background-color: Lightyellow')
        self.num_4.setFont(QtGui.QFont("Bradley Hand", 18))
        self.num_5 = QPushButton('5', self)
        self.num_5.resize(50, 50)  # размер кнопки
        self.num_5.move(60, 155)
        self.num_5.setStyleSheet('background-color: Lightyellow')
        self.num_5.setFont(QtGui.QFont("Bradley Hand", 18))
        self.num_6 = QPushButton('6', self)
        self.num_6.resize(50, 50)  # размер кнопки
        self.num_6.move(115, 155)
        self.num_6.setStyleSheet('background-color: Lightyellow')
        self.num_6.setFont(QtGui.QFont("Bradley Hand", 18))
        self.num_7 = QPushButton('7', self)
        self.num_7.resize(50, 50)  # размер кнопки
        self.num_7.move(5, 210)
        self.num_7.setStyleSheet('background-color: Lightyellow')
        self.num_7.setFont(QtGui.QFont("Bradley Hand", 18))
        self.num_8 = QPushButton('8', self)
        self.num_8.resize(50, 50)  # размер кнопки
        self.num_8.move(60, 210)
        self.num_8.setStyleSheet('background-color: Lightyellow')
        self.num_8.setFont(QtGui.QFont("Bradley Hand", 18))
        self.num_9 = QPushButton('9', self)
        self.num_9.resize(50, 50)  # размер кнопки
        self.num_9.move(115, 210)
        self.num_9.setStyleSheet('background-color: Lightyellow')
        self.num_9.setFont(QtGui.QFont("Bradley Hand", 18))
        self.num_0 = QPushButton('0', self)
        self.num_0.resize(50, 50)  # размер кнопки
        self.num_0.move(5, 265)
        self.num_0.setStyleSheet('background-color: Lightyellow')
        self.num_0.setFont(QtGui.QFont("Bradley Hand", 18))
        self.plus = QPushButton('+', self)
        self.plus.resize(50,50)
        self.plus.move(170,210)
        self.plus.setStyleSheet('background-color: Darkseagreen')
        self.plus.setFont(QtGui.QFont("Bradley Hand", 18))
        self.minus = QPushButton('-', self)
        self.minus.resize(50, 50)
        self.minus.move(170, 265)
        self.minus.setStyleSheet('background-color: Darkseagreen')
        self.minus.setFont(QtGui.QFont("Bradley Hand", 18))
        self.mul = QPushButton('*', self)
        self.mul.resize(50, 50)
        self.mul.move(170, 155)
        self.mul.setStyleSheet('background-color: Darkseagreen')
        self.mul.setFont(QtGui.QFont("Bradley Hand", 18))
        self.div = QPushButton('/', self)
        self.div.resize(50, 50)
        self.div.move(170, 100)
        self.div.setStyleSheet('background-color: Darkseagreen')
        self.div.setFont(QtGui.QFont("Bradley Hand", 18))
        self.ravn = QPushButton('=', self)
        self.ravn.resize(275, 50)
        self.ravn.move(5, 320)
        self.ravn.setStyleSheet('background-color: thistle')
        self.ravn.setFont(QtGui.QFont("Bradley Hand", 18))

        self.c = QPushButton('C', self)
        self.c.resize(105, 50)
        self.c.move(60, 265)
        self.c.setStyleSheet('background-color: lightsalmon')
        self.c.setFont(QtGui.QFont("Bradley Hand", 18))
        self.deg = QPushButton('^', self)
        self.deg.resize(50,50)
        self.deg.move(230,100)
        self.deg.setStyleSheet('background-color: khaki')
        self.deg.setFont(QtGui.QFont("Bradley Hand", 18))

        self.root_ = QPushButton('√', self)
        self.root_.resize(50, 50)
        self.root_.move(230, 155)
        self.root_.setStyleSheet('background-color: khaki')
        self.root_.setFont(QtGui.QFont("Bradley Hand", 18))

        self.root__2 = QPushButton('2√', self)
        self.root__2.resize(50, 50)
        self.root__2.move(230, 265)
        self.root__2.setStyleSheet('background-color: khaki')
        self.root__2.setFont(QtGui.QFont("Bradley Hand", 18))

        self.deg_2 = QPushButton('^2', self)
        self.deg_2.resize(50,50)
        self.deg_2.move(230,210)
        self.deg_2.setStyleSheet('background-color: khaki')
        self.deg_2.setFont(QtGui.QFont("Bradley Hand", 18))

        self.num_1.clicked.connect(self.one)
        self.num_2.clicked.connect(self.two)
        self.num_3.clicked.connect(self.three)
        self.num_4.clicked.connect(self.four)
        self.num_5.clicked.connect(self.five)
        self.num_6.clicked.connect(self.six)
        self.num_7.clicked.connect(self.seven)
        self.num_8.clicked.connect(self.eight)
        self.num_9.clicked.connect(self.nine)
        self.num_0.clicked.connect(self.zero)
        self.plus.clicked.connect(self.plus_1)
        self.minus.clicked.connect(self.minus_1)
        self.mul.clicked.connect(self.mul_1)
        self.div.clicked.connect(self.div_1)
        self.ravn.clicked.connect(self.ravno)
        self.c.clicked.connect(self.clean)
        self.deg.clicked.connect(self.degree)
        self.root_.clicked.connect(self.root_y)
        self.deg_2.clicked.connect(self.degree_2)
        self.root__2.clicked.connect(self.root_2)


    def enter_value(self):
        if self.label.text() == '0':
            self.label.setText('')
        self.label.setText(str(self.label.text()) + str(self.my_input))


    def one(self):
        self.my_input = 1
        self.enter_value()

    def two(self):
        self.my_input = 2
        self.enter_value()

    def three(self):
        self.my_input = 3
        self.enter_value()

    def four(self):
        self.my_input = 4
        self.enter_value()

    def five(self):
        self.my_input = 5
        self.enter_value()

    def six(self):
        self.my_input = 6
        self.enter_value()

    def seven(self):
        self.my_input = 7
        self.enter_value()

    def eight(self):
        self.my_input = 8
        self.enter_value()

    def nine(self):
        self.my_input = 9
        self.enter_value()

    def zero(self):
        self.my_input = 0
        self.enter_value()

    def plus_1(self):
        self.operation = '+'
        self.operand1 = float(self.label.text())
        self.label.setText('0')

    def minus_1(self):
        self.operation = '-'
        self.operand1 = float(self.label.text())
        self.label.setText('0')

    def mul_1(self):
        self.operation = '*'
        self.operand1 = float(self.label.text())
        self.label.setText('0')


    def div_1(self):
        self.operation = '/'
        self.operand1 = float(self.label.text())
        self.label.setText('0')

    def degree(self):
        self.operation = '^'
        self.operand1 = float(self.label.text())
        self.label.setText('0')

    def root_y(self):
        self.operation = '√'
        self.operand1 = float(self.label.text())
        self.label.setText('0')

    def degree_2(self):
        self.operation = '^2'
        self.operand1 = float(self.label.text())
        self.label.setText(str(self.operand1 ** 2))

    def root_2(self):
        self.operation = '2√'
        self.operand1 = float(self.label.text())
        self.label.setText(f'{self.operand1 ** 0.5}')



    def clean(self):
        self.label.setText('0')

    def ravno(self):
            self.operand2 = float(self.label.text())
            if self.operation == '+':
                self.label.setText(str(self.operand1 + self.operand2))
            elif self.operation == '-':
                self.label.setText(str(self.operand1 - self.operand2))
            elif self.operation == '*':
                self.label.setText(str(self.operand1 * self.operand2))
            elif self.operation == '/':
                if self.operand2 == 0:
                    self.label.setText('Деление на ноль!')
                else:
                    self.label.setText(str(self.operand1 / self.operand2))
            elif self.operation == '^':
                self.label.setText((str(self.operand1 ** self.operand2)))
            elif self.operation == '^2':
                return degree_2
            elif self.operation ==  '2√':
                return root_2
            elif self.operation == '√':
                self.label.setText(str(self.operand1 ** self.operand2))
            elif self.operation == '2√':
                self.label.setText(str((self.operand1 **0.5)))

app = QApplication(sys.argv) #создали объект класса QApplication, таким образом создали наше окно
#Виджет QApplication вызывает это само окно. в него передает sys arpv = аргументыкомандной строки
my_calculator = Calculator()
my_calculator.show()#показали наш объект
sys.exit(app.exec()) #завершаем работу калькулятора. Если ошибка будет уведомление
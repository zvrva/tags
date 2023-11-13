import sys
from random import shuffle

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(900, 300, 530, 530)
        self.setWindowTitle('Пятнашки')

        self.s = 0

        self.correct_matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]

        self.matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]

        self.place = {1: (0, 0),
                      2: (0, 1),
                      3: (0, 2),
                      4: (0, 3),

                      5: (1, 0),
                      6: (1, 1),
                      7: (1, 2),
                      8: (1, 3),

                      9: (2, 0),
                      10: (2, 1),
                      11: (2, 2),
                      12: (2, 3),

                      13: (3, 0),
                      14: (3, 1),
                      15: (3, 2),
                      0: (3, 3)}

        self.coord = {1: (100, 100),
                      2: (185, 100),
                      3: (270, 100),
                      4: (355, 100),

                      5: (100, 185),
                      6: (185, 185),
                      7: (270, 185),
                      8: (355, 185),

                      9: (100, 270),
                      10: (185, 270),
                      11: (270, 270),
                      12: (355, 270),

                      13: (100, 355),
                      14: (185, 355),
                      15: (270, 355),
                      0: (355, 355)}

        self.time = QtCore.QTime(0, 0, 0)

        self.vremya = QLabel('Время:', self)
        self.vremya.move(30, 30)

        self.chasy = QLabel(self)
        self.chasy.move(30, 50)
        self.chasy.resize(100, 30)

        self.steps = QLabel('Количество ходов:', self)
        self.steps.move(395, 30)

        self.step = QLabel(str(self.s), self)
        self.step.move(490, 50)
        self.step.resize(30, 30)

        self.congratulation = QLabel(self)
        self.congratulation.move(185, 30)

        self.btn0 = QPushButton('Разобрать', self)
        self.btn0.resize(170, 40)
        self.btn0.move(185, 460)
        self.btn0.clicked.connect(self.replace0)
        self.btn0.clicked.connect(self.timerEvent)

        self.btn1 = QPushButton('1', self)
        self.btn1.resize(75, 75)
        self.btn1.move(100, 100)
        self.btn1.clicked.connect(self.move1)

        self.btn2 = QPushButton('2', self)
        self.btn2.resize(75, 75)
        self.btn2.move(185, 100)
        self.btn2.clicked.connect(self.move2)

        self.btn3 = QPushButton('3', self)
        self.btn3.resize(75, 75)
        self.btn3.move(270, 100)
        self.btn3.clicked.connect(self.move3)

        self.btn4 = QPushButton('4', self)
        self.btn4.resize(75, 75)
        self.btn4.move(355, 100)
        self.btn4.clicked.connect(self.move4)

        self.btn5 = QPushButton('5', self)
        self.btn5.resize(75, 75)
        self.btn5.move(100, 185)
        self.btn5.clicked.connect(self.move5)

        self.btn6 = QPushButton('6', self)
        self.btn6.resize(75, 75)
        self.btn6.move(185, 185)
        self.btn6.clicked.connect(self.move6)

        self.btn7 = QPushButton('7', self)
        self.btn7.resize(75, 75)
        self.btn7.move(270, 185)
        self.btn7.clicked.connect(self.move7)

        self.btn8 = QPushButton('8', self)
        self.btn8.resize(75, 75)
        self.btn8.move(355, 185)
        self.btn8.clicked.connect(self.move8)

        self.btn9 = QPushButton('9', self)
        self.btn9.resize(75, 75)
        self.btn9.move(100, 270)
        self.btn9.clicked.connect(self.move9)

        self.btn10 = QPushButton('10', self)
        self.btn10.resize(75, 75)
        self.btn10.move(185, 270)
        self.btn10.clicked.connect(self.move10)

        self.btn11 = QPushButton('11', self)
        self.btn11.resize(75, 75)
        self.btn11.move(270, 270)
        self.btn11.clicked.connect(self.move11)

        self.btn12 = QPushButton('12', self)
        self.btn12.resize(75, 75)
        self.btn12.move(355, 270)
        self.btn12.clicked.connect(self.move12)

        self.btn13 = QPushButton('13', self)
        self.btn13.resize(75, 75)
        self.btn13.move(100, 355)
        self.btn13.clicked.connect(self.move13)

        self.btn14 = QPushButton('14', self)
        self.btn14.resize(75, 75)
        self.btn14.move(185, 355)
        self.btn14.clicked.connect(self.move14)

        self.btn15 = QPushButton('15', self)
        self.btn15.resize(75, 75)
        self.btn15.move(270, 355)
        self.btn15.clicked.connect(self.move15)

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.timerEvent)
        self.timer.start(1000)


    def timerEvent(self):
        if self.s > 0:
            self.time = self.time.addSecs(1)
        self.chasy.setText(self.time.toString("hh:mm:ss"))

    def replace0(self):
        self.s = 0
        self.time = QtCore.QTime(0, 0, 0)
        self.step.setText(str(self.s))
        m = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]
        shuffle(m)

        s = 0
        for i in range(len(m)):
            if m[i] == i:
                s += 1

        while (s % 2 == 1):
            shuffle(m)
            s = 0
            for i in range(len(m)):
                if m[i] == i:
                    s += 1

        n = 0
        for i in range(4):
            for j in range(4):
                self.matrix[i][j] = m[n]
                n += 1

        n = 0
        for i in range(4):
            for j in range(4):
                self.place[m[n]] = i, j
                n += 1

        n = 0
        for i in [100, 185, 270, 355]:
            for j in [100, 185, 270, 355]:
                self.coord[m[n]] = j, i
                n += 1

        for i in m:
            if i == 1:
                x, y = self.coord[1]
                self.btn1.move(x, y)
                self.btn1.setStyleSheet('background-color: white')
            if i == 2:
                x, y = self.coord[2]
                self.btn2.move(x, y)
                self.btn2.setStyleSheet('background-color: white')
            if i == 3:
                x, y = self.coord[3]
                self.btn3.move(x, y)
                self.btn3.setStyleSheet('background-color: white')
            if i == 4:
                x, y = self.coord[4]
                self.btn4.move(x, y)
                self.btn4.setStyleSheet('background-color: white')
            if i == 5:
                x, y = self.coord[5]
                self.btn5.move(x, y)
                self.btn5.setStyleSheet('background-color: white')
            if i == 6:
                x, y = self.coord[6]
                self.btn6.move(x, y)
                self.btn6.setStyleSheet('background-color: white')
            if i == 7:
                x, y = self.coord[7]
                self.btn7.move(x, y)
                self.btn7.setStyleSheet('background-color: white')
            if i == 8:
                x, y = self.coord[8]
                self.btn8.move(x, y)
                self.btn8.setStyleSheet('background-color: white')
            if i == 9:
                x, y = self.coord[9]
                self.btn9.move(x, y)
                self.btn9.setStyleSheet('background-color: white')
            if i == 10:
                x, y = self.coord[10]
                self.btn10.move(x, y)
                self.btn10.setStyleSheet('background-color: white')
            if i == 11:
                x, y = self.coord[11]
                self.btn11.move(x, y)
                self.btn11.setStyleSheet('background-color: white')
            if i == 12:
                x, y = self.coord[12]
                self.btn12.move(x, y)
                self.btn12.setStyleSheet('background-color: white')
            if i == 13:
                x, y = self.coord[13]
                self.btn13.move(x, y)
                self.btn13.setStyleSheet('background-color: white')
            if i == 14:
                x, y = self.coord[14]
                self.btn14.move(x, y)
                self.btn14.setStyleSheet('background-color: white')
            if i == 15:
                x, y = self.coord[15]
                self.btn15.move(x, y)
                self.btn15.setStyleSheet('background-color: white')

    def move1(self):
        place_not_zero_x, place_not_zero_y = self.place[1]

        A, B = -1, -1
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == 0:
                    A, B = i, j

        if (place_not_zero_x + 1 == A and place_not_zero_y == B) or (
                place_not_zero_x - 1 == A and place_not_zero_y == B) or (
                place_not_zero_x == A and place_not_zero_y + 1 == B) or (
                place_not_zero_x == A and place_not_zero_y - 1 == B):
            coord_not_zero_x, coord_not_zero_y = self.coord[1]
            coord_zero_x, coord_zero_y = self.coord[0]
            place_zero_x, place_zero_y = self.place[0]

            self.matrix[place_not_zero_x][place_not_zero_y] = 0
            self.matrix[place_zero_x][place_zero_y] = 1

            self.place[1] = place_zero_x, place_zero_y
            self.place[0] = place_not_zero_x, place_not_zero_y

            self.coord[1] = coord_zero_x, coord_zero_y
            self.coord[0] = coord_not_zero_x, coord_not_zero_y

            self.btn1.move(coord_zero_x, coord_zero_y)

            if place_zero_x == 0 and place_zero_y == 0:
                self.btn1.setStyleSheet('background-color: #b6d7a8')
            else:
                self.btn1.setStyleSheet('background-color: white')

            if self.matrix == self.correct_matrix:
                self.congratulation.setText('Поздравляю!')

            self.s += 1
            self.step.setText(str(self.s))

    def move2(self):
        place_not_zero_x, place_not_zero_y = self.place[2]

        A, B = -1, -1
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == 0:
                    A, B = i, j

        if (place_not_zero_x + 1 == A and place_not_zero_y == B) or (
                place_not_zero_x - 1 == A and place_not_zero_y == B) or (
                place_not_zero_x == A and place_not_zero_y + 1 == B) or (
                place_not_zero_x == A and place_not_zero_y - 1 == B):
            coord_not_zero_x, coord_not_zero_y = self.coord[2]
            coord_zero_x, coord_zero_y = self.coord[0]
            place_zero_x, place_zero_y = self.place[0]

            self.matrix[place_not_zero_x][place_not_zero_y] = 0
            self.matrix[place_zero_x][place_zero_y] = 2

            self.place[2] = place_zero_x, place_zero_y
            self.place[0] = place_not_zero_x, place_not_zero_y

            self.coord[2] = coord_zero_x, coord_zero_y
            self.coord[0] = coord_not_zero_x, coord_not_zero_y

            self.btn2.move(coord_zero_x, coord_zero_y)

            if place_zero_x == 0 and place_zero_y == 1:
                self.btn2.setStyleSheet('background-color: #b6d7a8')
            else:
                self.btn2.setStyleSheet('background-color: white')

            if self.matrix == self.correct_matrix:
                self.congratulation.setText('Поздравляю!')

            self.s += 1
            self.step.setText(str(self.s))

    def move3(self):
        place_not_zero_x, place_not_zero_y = self.place[3]

        A, B = -1, -1
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == 0:
                    A, B = i, j

        if (place_not_zero_x + 1 == A and place_not_zero_y == B) or (
                place_not_zero_x - 1 == A and place_not_zero_y == B) or (
                place_not_zero_x == A and place_not_zero_y + 1 == B) or (
                place_not_zero_x == A and place_not_zero_y - 1 == B):
            coord_not_zero_x, coord_not_zero_y = self.coord[3]
            coord_zero_x, coord_zero_y = self.coord[0]
            place_zero_x, place_zero_y = self.place[0]

            self.matrix[place_not_zero_x][place_not_zero_y] = 0
            self.matrix[place_zero_x][place_zero_y] = 3

            self.place[3] = place_zero_x, place_zero_y
            self.place[0] = place_not_zero_x, place_not_zero_y

            self.coord[3] = coord_zero_x, coord_zero_y
            self.coord[0] = coord_not_zero_x, coord_not_zero_y

            self.btn3.move(coord_zero_x, coord_zero_y)

            if place_zero_x == 0 and place_zero_y == 2:
                self.btn3.setStyleSheet('background-color: #b6d7a8')
            else:
                self.btn3.setStyleSheet('background-color: white')

            if self.matrix == self.correct_matrix:
                self.congratulation.setText('Поздравляю!')

            self.s += 1
            self.step.setText(str(self.s))

    def move4(self):
        place_not_zero_x, place_not_zero_y = self.place[4]

        A, B = -1, -1
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == 0:
                    A, B = i, j

        if (place_not_zero_x + 1 == A and place_not_zero_y == B) or (
                place_not_zero_x - 1 == A and place_not_zero_y == B) or (
                place_not_zero_x == A and place_not_zero_y + 1 == B) or (
                place_not_zero_x == A and place_not_zero_y - 1 == B):
            coord_not_zero_x, coord_not_zero_y = self.coord[4]
            coord_zero_x, coord_zero_y = self.coord[0]
            place_zero_x, place_zero_y = self.place[0]

            self.matrix[place_not_zero_x][place_not_zero_y] = 0
            self.matrix[place_zero_x][place_zero_y] = 4

            self.place[4] = place_zero_x, place_zero_y
            self.place[0] = place_not_zero_x, place_not_zero_y

            self.coord[4] = coord_zero_x, coord_zero_y
            self.coord[0] = coord_not_zero_x, coord_not_zero_y

            self.btn4.move(coord_zero_x, coord_zero_y)

            if place_zero_x == 0 and place_zero_y == 3:
                self.btn4.setStyleSheet('background-color: #b6d7a8')
            else:
                self.btn4.setStyleSheet('background-color: white')

            if self.matrix == self.correct_matrix:
                self.congratulation.setText('Поздравляю!')

            self.s += 1
            self.step.setText(str(self.s))

    def move5(self):
        place_not_zero_x, place_not_zero_y = self.place[5]

        A, B = -1, -1
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == 0:
                    A, B = i, j

        if (place_not_zero_x + 1 == A and place_not_zero_y == B) or (
                place_not_zero_x - 1 == A and place_not_zero_y == B) or (
                place_not_zero_x == A and place_not_zero_y + 1 == B) or (
                place_not_zero_x == A and place_not_zero_y - 1 == B):
            coord_not_zero_x, coord_not_zero_y = self.coord[5]
            coord_zero_x, coord_zero_y = self.coord[0]
            place_zero_x, place_zero_y = self.place[0]

            self.matrix[place_not_zero_x][place_not_zero_y] = 0
            self.matrix[place_zero_x][place_zero_y] = 5

            self.place[5] = place_zero_x, place_zero_y
            self.place[0] = place_not_zero_x, place_not_zero_y

            self.coord[5] = coord_zero_x, coord_zero_y
            self.coord[0] = coord_not_zero_x, coord_not_zero_y

            self.btn5.move(coord_zero_x, coord_zero_y)

            if place_zero_x == 1 and place_zero_y == 0:
                self.btn5.setStyleSheet('background-color: #b6d7a8')
            else:
                self.btn5.setStyleSheet('background-color: white')

            if self.matrix == self.correct_matrix:
                self.congratulation.setText('Поздравляю!')

            self.s += 1
            self.step.setText(str(self.s))

    def move6(self):
        place_not_zero_x, place_not_zero_y = self.place[6]

        A, B = -1, -1
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == 0:
                    A, B = i, j

        if (place_not_zero_x + 1 == A and place_not_zero_y == B) or (
                place_not_zero_x - 1 == A and place_not_zero_y == B) or (
                place_not_zero_x == A and place_not_zero_y + 1 == B) or (
                place_not_zero_x == A and place_not_zero_y - 1 == B):
            coord_not_zero_x, coord_not_zero_y = self.coord[6]
            coord_zero_x, coord_zero_y = self.coord[0]
            place_zero_x, place_zero_y = self.place[0]

            self.matrix[place_not_zero_x][place_not_zero_y] = 0
            self.matrix[place_zero_x][place_zero_y] = 6

            self.place[6] = place_zero_x, place_zero_y
            self.place[0] = place_not_zero_x, place_not_zero_y

            self.coord[6] = coord_zero_x, coord_zero_y
            self.coord[0] = coord_not_zero_x, coord_not_zero_y

            self.btn6.move(coord_zero_x, coord_zero_y)

            if place_zero_x == 1 and place_zero_y == 1:
                self.btn6.setStyleSheet('background-color: #b6d7a8')
            else:
                self.btn6.setStyleSheet('background-color: white')

            if self.matrix == self.correct_matrix:
                self.congratulation.setText('Поздравляю!')

            self.s += 1
            self.step.setText(str(self.s))

    def move7(self):
        place_not_zero_x, place_not_zero_y = self.place[7]

        A, B = -1, -1
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == 0:
                    A, B = i, j

        if (place_not_zero_x + 1 == A and place_not_zero_y == B) or (
                place_not_zero_x - 1 == A and place_not_zero_y == B) or (
                place_not_zero_x == A and place_not_zero_y + 1 == B) or (
                place_not_zero_x == A and place_not_zero_y - 1 == B):
            coord_not_zero_x, coord_not_zero_y = self.coord[7]
            coord_zero_x, coord_zero_y = self.coord[0]
            place_zero_x, place_zero_y = self.place[0]

            self.matrix[place_not_zero_x][place_not_zero_y] = 0
            self.matrix[place_zero_x][place_zero_y] = 7

            self.place[7] = place_zero_x, place_zero_y
            self.place[0] = place_not_zero_x, place_not_zero_y

            self.coord[7] = coord_zero_x, coord_zero_y
            self.coord[0] = coord_not_zero_x, coord_not_zero_y

            self.btn7.move(coord_zero_x, coord_zero_y)

            if place_zero_x == 1 and place_zero_y == 2:
                self.btn7.setStyleSheet('background-color: #b6d7a8')
            else:
                self.btn7.setStyleSheet('background-color: white')

            if self.matrix == self.correct_matrix:
                self.congratulation.setText('Поздравляю!')

            self.s += 1
            self.step.setText(str(self.s))

    def move8(self):
        place_not_zero_x, place_not_zero_y = self.place[8]

        A, B = -1, -1
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == 0:
                    A, B = i, j

        if (place_not_zero_x + 1 == A and place_not_zero_y == B) or (
                place_not_zero_x - 1 == A and place_not_zero_y == B) or (
                place_not_zero_x == A and place_not_zero_y + 1 == B) or (
                place_not_zero_x == A and place_not_zero_y - 1 == B):
            coord_not_zero_x, coord_not_zero_y = self.coord[8]
            coord_zero_x, coord_zero_y = self.coord[0]
            place_zero_x, place_zero_y = self.place[0]

            self.matrix[place_not_zero_x][place_not_zero_y] = 0
            self.matrix[place_zero_x][place_zero_y] = 8

            self.place[8] = place_zero_x, place_zero_y
            self.place[0] = place_not_zero_x, place_not_zero_y

            self.coord[8] = coord_zero_x, coord_zero_y
            self.coord[0] = coord_not_zero_x, coord_not_zero_y

            self.btn8.move(coord_zero_x, coord_zero_y)

            if place_zero_x == 1 and place_zero_y == 3:
                self.btn8.setStyleSheet('background-color: #b6d7a8')
            else:
                self.btn8.setStyleSheet('background-color: white')

            if self.matrix == self.correct_matrix:
                self.congratulation.setText('Поздравляю!')

            self.s += 1
            self.step.setText(str(self.s))

    def move9(self):
        place_not_zero_x, place_not_zero_y = self.place[9]

        A, B = -1, -1
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == 0:
                    A, B = i, j

        if (place_not_zero_x + 1 == A and place_not_zero_y == B) or (
                place_not_zero_x - 1 == A and place_not_zero_y == B) or (
                place_not_zero_x == A and place_not_zero_y + 1 == B) or (
                place_not_zero_x == A and place_not_zero_y - 1 == B):
            coord_not_zero_x, coord_not_zero_y = self.coord[9]
            coord_zero_x, coord_zero_y = self.coord[0]
            place_zero_x, place_zero_y = self.place[0]

            self.matrix[place_not_zero_x][place_not_zero_y] = 0
            self.matrix[place_zero_x][place_zero_y] = 9

            self.place[9] = place_zero_x, place_zero_y
            self.place[0] = place_not_zero_x, place_not_zero_y

            self.coord[9] = coord_zero_x, coord_zero_y
            self.coord[0] = coord_not_zero_x, coord_not_zero_y

            self.btn9.move(coord_zero_x, coord_zero_y)

            if place_zero_x == 2 and place_zero_y == 0:
                self.btn9.setStyleSheet('background-color: #b6d7a8')
            else:
                self.btn9.setStyleSheet('background-color: white')

            if self.matrix == self.correct_matrix:
                self.congratulation.setText('Поздравляю!')

            self.s += 1
            self.step.setText(str(self.s))

    def move10(self):
        place_not_zero_x, place_not_zero_y = self.place[10]

        A, B = -1, -1
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == 0:
                    A, B = i, j

        if (place_not_zero_x + 1 == A and place_not_zero_y == B) or (
                place_not_zero_x - 1 == A and place_not_zero_y == B) or (
                place_not_zero_x == A and place_not_zero_y + 1 == B) or (
                place_not_zero_x == A and place_not_zero_y - 1 == B):
            coord_not_zero_x, coord_not_zero_y = self.coord[10]
            coord_zero_x, coord_zero_y = self.coord[0]
            place_zero_x, place_zero_y = self.place[0]

            self.matrix[place_not_zero_x][place_not_zero_y] = 0
            self.matrix[place_zero_x][place_zero_y] = 10

            self.place[10] = place_zero_x, place_zero_y
            self.place[0] = place_not_zero_x, place_not_zero_y

            self.coord[10] = coord_zero_x, coord_zero_y
            self.coord[0] = coord_not_zero_x, coord_not_zero_y

            self.btn10.move(coord_zero_x, coord_zero_y)

            if place_zero_x == 2 and place_zero_y == 1:
                self.btn10.setStyleSheet('background-color: #b6d7a8')
            else:
                self.btn10.setStyleSheet('background-color: white')

            if self.matrix == self.correct_matrix:
                self.congratulation.setText('Поздравляю!')

            self.s += 1
            self.step.setText(str(self.s))

    def move11(self):
        place_not_zero_x, place_not_zero_y = self.place[11]

        A, B = -1, -1
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == 0:
                    A, B = i, j

        if (place_not_zero_x + 1 == A and place_not_zero_y == B) or (
                place_not_zero_x - 1 == A and place_not_zero_y == B) or (
                place_not_zero_x == A and place_not_zero_y + 1 == B) or (
                place_not_zero_x == A and place_not_zero_y - 1 == B):
            coord_not_zero_x, coord_not_zero_y = self.coord[11]
            coord_zero_x, coord_zero_y = self.coord[0]
            place_zero_x, place_zero_y = self.place[0]

            self.matrix[place_not_zero_x][place_not_zero_y] = 0
            self.matrix[place_zero_x][place_zero_y] = 11

            self.place[11] = place_zero_x, place_zero_y
            self.place[0] = place_not_zero_x, place_not_zero_y

            self.coord[11] = coord_zero_x, coord_zero_y
            self.coord[0] = coord_not_zero_x, coord_not_zero_y

            self.btn11.move(coord_zero_x, coord_zero_y)

            if place_zero_x == 2 and place_zero_y == 2:
                self.btn11.setStyleSheet('background-color: #b6d7a8')
            else:
                self.btn11.setStyleSheet('background-color: white')

            if self.matrix == self.correct_matrix:
                self.congratulation.setText('Поздравляю!')

            self.s += 1
            self.step.setText(str(self.s))

    def move12(self):
        place_not_zero_x, place_not_zero_y = self.place[12]

        A, B = -1, -1
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == 0:
                    A, B = i, j

        if (place_not_zero_x + 1 == A and place_not_zero_y == B) or (
                place_not_zero_x - 1 == A and place_not_zero_y == B) or (
                place_not_zero_x == A and place_not_zero_y + 1 == B) or (
                place_not_zero_x == A and place_not_zero_y - 1 == B):
            coord_not_zero_x, coord_not_zero_y = self.coord[12]
            coord_zero_x, coord_zero_y = self.coord[0]
            place_zero_x, place_zero_y = self.place[0]

            self.matrix[place_not_zero_x][place_not_zero_y] = 0
            self.matrix[place_zero_x][place_zero_y] = 12

            self.place[12] = place_zero_x, place_zero_y
            self.place[0] = place_not_zero_x, place_not_zero_y

            self.coord[12] = coord_zero_x, coord_zero_y
            self.coord[0] = coord_not_zero_x, coord_not_zero_y

            self.btn12.move(coord_zero_x, coord_zero_y)

            if place_zero_x == 2 and place_zero_y == 3:
                self.btn12.setStyleSheet('background-color: #b6d7a8')
            else:
                self.btn12.setStyleSheet('background-color: white')

            if self.matrix == self.correct_matrix:
                self.congratulation.setText('Поздравляю!')

            self.s += 1
            self.step.setText(str(self.s))

    def move13(self):
        place_not_zero_x, place_not_zero_y = self.place[13]

        A, B = -1, -1
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == 0:
                    A, B = i, j

        if (place_not_zero_x + 1 == A and place_not_zero_y == B) or (
                place_not_zero_x - 1 == A and place_not_zero_y == B) or (
                place_not_zero_x == A and place_not_zero_y + 1 == B) or (
                place_not_zero_x == A and place_not_zero_y - 1 == B):
            coord_not_zero_x, coord_not_zero_y = self.coord[13]
            coord_zero_x, coord_zero_y = self.coord[0]
            place_zero_x, place_zero_y = self.place[0]

            self.matrix[place_not_zero_x][place_not_zero_y] = 0
            self.matrix[place_zero_x][place_zero_y] = 13

            self.place[13] = place_zero_x, place_zero_y
            self.place[0] = place_not_zero_x, place_not_zero_y

            self.coord[13] = coord_zero_x, coord_zero_y
            self.coord[0] = coord_not_zero_x, coord_not_zero_y

            self.btn13.move(coord_zero_x, coord_zero_y)

            if place_zero_x == 3 and place_zero_y == 0:
                self.btn13.setStyleSheet('background-color: #b6d7a8')
            else:
                self.btn13.setStyleSheet('background-color: white')

            if self.matrix == self.correct_matrix:
                self.congratulation.setText('Поздравляю!')

            self.s += 1
            self.step.setText(str(self.s))

    def move14(self):
        place_not_zero_x, place_not_zero_y = self.place[14]

        A, B = -1, -1
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == 0:
                    A, B = i, j

        if (place_not_zero_x + 1 == A and place_not_zero_y == B) or (
                place_not_zero_x - 1 == A and place_not_zero_y == B) or (
                place_not_zero_x == A and place_not_zero_y + 1 == B) or (
                place_not_zero_x == A and place_not_zero_y - 1 == B):
            coord_not_zero_x, coord_not_zero_y = self.coord[14]
            coord_zero_x, coord_zero_y = self.coord[0]
            place_zero_x, place_zero_y = self.place[0]

            self.matrix[place_not_zero_x][place_not_zero_y] = 0
            self.matrix[place_zero_x][place_zero_y] = 14

            self.place[14] = place_zero_x, place_zero_y
            self.place[0] = place_not_zero_x, place_not_zero_y

            self.coord[14] = coord_zero_x, coord_zero_y
            self.coord[0] = coord_not_zero_x, coord_not_zero_y

            self.btn14.move(coord_zero_x, coord_zero_y)

            if place_zero_x == 3 and place_zero_y == 1:
                self.btn14.setStyleSheet('background-color: #b6d7a8')
            else:
                self.btn14.setStyleSheet('background-color: white')

            if self.matrix == self.correct_matrix:
                self.congratulation.setText('Поздравляю!')

            self.s += 1
            self.step.setText(str(self.s))

    def move15(self):
        place_not_zero_x, place_not_zero_y = self.place[15]

        A, B = -1, -1
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == 0:
                    A, B = i, j

        if (place_not_zero_x + 1 == A and place_not_zero_y == B) or (
                place_not_zero_x - 1 == A and place_not_zero_y == B) or (
                place_not_zero_x == A and place_not_zero_y + 1 == B) or (
                place_not_zero_x == A and place_not_zero_y - 1 == B):
            coord_not_zero_x, coord_not_zero_y = self.coord[15]
            coord_zero_x, coord_zero_y = self.coord[0]
            place_zero_x, place_zero_y = self.place[0]

            self.matrix[place_not_zero_x][place_not_zero_y] = 0
            self.matrix[place_zero_x][place_zero_y] = 15

            self.place[15] = place_zero_x, place_zero_y
            self.place[0] = place_not_zero_x, place_not_zero_y

            self.coord[15] = coord_zero_x, coord_zero_y
            self.coord[0] = coord_not_zero_x, coord_not_zero_y

            self.btn15.move(coord_zero_x, coord_zero_y)

            if place_zero_x == 3 and place_zero_y == 2:
                self.btn15.setStyleSheet('background-color: #b6d7a8')
            else:
                self.btn15.setStyleSheet('background-color: white')

            if self.matrix == self.correct_matrix:
                self.congratulation.setText('Поздравляю!')

            self.s += 1
            self.step.setText(str(self.s))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())

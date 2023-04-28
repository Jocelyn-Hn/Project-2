from PyQt5.QtWidgets import *
from random import *
from view import *

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.button_help.clicked.connect(lambda: self.help())
        self.button_clear.clicked.connect(lambda: self.clear())
        self.button_roll.clicked.connect(lambda: self.roll())

    def help(self):
        self.instructions.setText('Check corresponding boxes for dice desired. \n'
                                  'Enter amount of dice to be rolled. \n'
                                  'Insert whole integers. (e.g. 5 not 5.5, 3 not \'e\'.)')

    def clear(self):
        self.checkBox_d100.setChecked(False)
        self.checkBox_d20.setChecked(False)
        self.checkBox_d12.setChecked(False)
        self.checkBox_d10.setChecked(False)
        self.checkBox_d8.setChecked(False)
        self.checkBox_d6.setChecked(False)
        self.checkBox_d4.setChecked(False)
        self.instructions.setText('')
        self.input_d100.setText('')
        self.input_d20.setText('')
        self.input_d12.setText('')
        self.input_d10.setText('')
        self.input_d8.setText('')
        self.input_d6.setText('')
        self.input_d4.setText('')
        self.rolls_d100.setText('')
        self.rolls_d20.setText('')
        self.rolls_d12.setText('')
        self.rolls_d10.setText('')
        self.rolls_d8.setText('')
        self.rolls_d6.setText('')
        self.rolls_d4.setText('')
        self.total_d100.setText('')
        self.total_d20.setText('')
        self.total_d12.setText('')
        self.total_d10.setText('')
        self.total_d8.setText('')
        self.total_d6.setText('')
        self.total_d4.setText('')

    def roll(self):
        if self.checkBox_d100.isChecked():
            try:
                rolls = []
                if int(self.input_d100.text()) > 10:
                    self.instructions.setText('Please input a dice amount of 10 or less.')
                else:
                    for roll in range(int(self.input_d100.text())):
                        rolls.append(randint(1, 101))

                        self.rolls_d100.setText(', '.join([str(roll) for roll in rolls]))
                        self.total_d100.setText(str(sum(rolls)))

            except ValueError:
                self.instructions.setText('Please enter a whole number.')

        if self.checkBox_d20.isChecked():
            try:
                rolls = []
                if int(self.input_d20.text()) > 10:
                    self.instructions.setText('Please input a dice amount of 10 or less.')
                else:
                    for roll in range(int(self.input_d20.text())):
                        rolls.append(randint(1, 21))

                        self.rolls_d20.setText(', '.join([str(roll) for roll in rolls]))
                        self.total_d20.setText(str(sum(rolls)))

            except ValueError:
                self.instructions.setText('Please enter a whole number.')

        if self.checkBox_d12.isChecked():
            try:
                rolls = []
                if int(self.input_d12.text()) > 10:
                    self.instructions.setText('Please input a dice amount of 10 or less.')
                else:
                    for roll in range(int(self.input_d12.text())):
                        rolls.append(randint(1, 13))

                        self.rolls_d12.setText(', '.join([str(roll) for roll in rolls]))
                        self.total_d12.setText(str(sum(rolls)))

            except ValueError:
                self.instructions.setText('Please enter a whole number.')

        if self.checkBox_d10.isChecked():
            try:
                rolls = []
                if int(self.input_d10.text()) > 10:
                    self.instructions.setText('Please input a dice amount of 10 or less.')
                else:
                    for roll in range(int(self.input_d10.text())):
                        rolls.append(randint(1, 11))

                        self.rolls_d10.setText(', '.join([str(roll) for roll in rolls]))
                        self.total_d10.setText(str(sum(rolls)))

            except ValueError:
                self.instructions.setText('Please enter a whole number.')

        if self.checkBox_d8.isChecked():
            try:
                rolls = []
                if int(self.input_d8.text()) > 10:
                    self.instructions.setText('Please input a dice amount of 10 or less.')
                else:
                    for roll in range(int(self.input_d8.text())):
                        rolls.append(randint(1, 9))

                        self.rolls_d8.setText(', '.join([str(roll) for roll in rolls]))
                        self.total_d8.setText(str(sum(rolls)))

            except ValueError:
                self.instructions.setText('Please enter a whole number.')

        if self.checkBox_d6.isChecked():
            try:
                rolls = []
                if int(self.input_d6.text()) > 10:
                    self.instructions.setText('Please input a dice amount of 10 or less.')
                else:
                    for roll in range(int(self.input_d6.text())):
                        rolls.append(randint(1, 7))

                        self.rolls_d6.setText(', '.join([str(roll) for roll in rolls]))
                        self.total_d6.setText(str(sum(rolls)))

            except ValueError:
                self.instructions.setText('Please enter a whole number.')

        if self.checkBox_d4.isChecked():
            try:
                rolls = []
                if int(self.input_d4.text()) > 10:
                    self.instructions.setText('Please input a dice amount of 10 or less.')
                else:
                    for roll in range(int(self.input_d4.text())):
                        rolls.append(randint(1, 5))

                        self.rolls_d4.setText(', '.join([str(roll) for roll in rolls]))
                        self.total_d4.setText(str(sum(rolls)))

            except ValueError:
                self.instructions.setText('Please enter a whole number.')

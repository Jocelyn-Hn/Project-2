from PyQt5.QtWidgets import *
from random import *
from view import *

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        """
        Function to set up application object.
        :param name: Controller
        :param args:
        :param kwargs:
        """
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.button_help.clicked.connect(lambda: self.help())
        self.button_clear.clicked.connect(lambda: self.clear())
        self.button_roll.clicked.connect(lambda: self.roll())

        self.checkBox_d100.stateChanged.connect(lambda: self.state_changed())
        self.checkBox_d20.stateChanged.connect(lambda: self.state_changed())
        self.checkBox_d12.stateChanged.connect(lambda: self.state_changed())
        self.checkBox_d10.stateChanged.connect(lambda: self.state_changed())
        self.checkBox_d8.stateChanged.connect(lambda: self.state_changed())
        self.checkBox_d6.stateChanged.connect(lambda: self.state_changed())
        self.checkBox_d4.stateChanged.connect(lambda: self.state_changed())

        self.input_d100.setEnabled(False)
        self.input_d20.setEnabled(False)
        self.input_d12.setEnabled(False)
        self.input_d10.setEnabled(False)
        self.input_d8.setEnabled(False)
        self.input_d6.setEnabled(False)
        self.input_d4.setEnabled(False)

    def help(self):
        """
        Function to display instructions.
        :return:
        """
        self.instructions.setText('Check corresponding boxes for dice desired. \n'
                                  'Enter amount of dice to be rolled. \n'
                                  'Insert whole integers. (e.g. 5 not 5.5, 3 not \'e\'.)')

    def state_changed(self):
        """
        Function to enable input boxes when checkboxes are selected.
        :return:
        """
        if self.checkBox_d100.isChecked():
            self.input_d100.setEnabled(True)
        else:
            self.input_d100.setEnabled(False)
            self.rolls_d100.setText('')
            self.total_d100.setText('')
            self.label_totald100.setText('')
            self.label_rollsd100.setText('')

        if self.checkBox_d20.isChecked():
            self.input_d20.setEnabled(True)
        else:
            self.input_d20.setEnabled(False)
            self.rolls_d20.setText('')
            self.total_d20.setText('')
            self.label_totald20.setText('')
            self.label_rollsd20.setText('')

        if self.checkBox_d12.isChecked():
            self.input_d12.setEnabled(True)
        else:
            self.input_d12.setEnabled(False)
            self.rolls_d12.setText('')
            self.total_d12.setText('')
            self.label_totald12.setText('')
            self.label_rollsd12.setText('')

        if self.checkBox_d10.isChecked():
            self.input_d10.setEnabled(True)
        else:
            self.input_d10.setEnabled(False)
            self.rolls_d10.setText('')
            self.total_d10.setText('')
            self.label_totald10.setText('')
            self.label_rollsd10.setText('')

        if self.checkBox_d8.isChecked():
            self.input_d8.setEnabled(True)
        else:
            self.input_d8.setEnabled(False)
            self.rolls_d8.setText('')
            self.total_d8.setText('')
            self.label_totald8.setText('')
            self.label_rollsd8.setText('')

        if self.checkBox_d6.isChecked():
            self.input_d6.setEnabled(True)
        else:
            self.input_d6.setEnabled(False)
            self.rolls_d6.setText('')
            self.total_d6.setText('')
            self.label_totald6.setText('')
            self.label_rollsd6.setText('')

        if self.checkBox_d4.isChecked():
            self.input_d4.setEnabled(True)
        else:
            self.input_d4.setEnabled(False)
            self.rolls_d4.setText('')
            self.total_d4.setText('')
            self.label_totald4.setText('')
            self.label_rollsd4.setText('')

    def roll(self):
        """
        Function to roll selected dice.
        :return:
        """
        try:
            if self.checkBox_d100.isChecked():
                rolls = []
                if int(self.input_d100.text()) > 10 or int(self.input_d100.text()) < 1:
                    raise ValueError
                else:
                    self.instructions.setText('')
                    self.label_rollsd100.setText('Rolls:')
                    self.label_totald100.setText('Total:')
                    for roll in range(int(self.input_d100.text())):
                        rolls.append(randint(1, 101))
                        self.rolls_d100.setText(', '.join([str(roll) for roll in rolls]))
                        self.total_d100.setText(str(sum(rolls)))

            if self.checkBox_d20.isChecked():
                rolls = []
                if int(self.input_d20.text()) > 10 or int(self.input_d20.text()) < 1:
                    raise ValueError
                else:
                    self.label_rollsd20.setText('Rolls:')
                    self.label_totald20.setText('Total:')
                    self.instructions.setText('')
                    for roll in range(int(self.input_d20.text())):
                        rolls.append(randint(1, 21))
                        self.rolls_d20.setText(', '.join([str(roll) for roll in rolls]))
                        self.total_d20.setText(str(sum(rolls)))

            if self.checkBox_d12.isChecked():
                rolls = []
                if int(self.input_d12.text()) > 10 or int(self.input_d12.text()) < 1:
                    raise ValueError
                else:
                    self.label_rollsd12.setText('Rolls:')
                    self.label_totald12.setText('Total:')
                    self.instructions.setText('')
                    for roll in range(int(self.input_d12.text())):
                        rolls.append(randint(1, 13))
                        self.rolls_d12.setText(', '.join([str(roll) for roll in rolls]))
                        self.total_d12.setText(str(sum(rolls)))

            if self.checkBox_d10.isChecked():
                rolls = []
                if int(self.input_d10.text()) > 10 or int(self.input_d10.text()) < 1:
                    raise ValueError
                else:
                    self.label_rollsd10.setText('Rolls:')
                    self.label_totald10.setText('Total:')
                    self.instructions.setText('')
                    for roll in range(int(self.input_d10.text())):
                        rolls.append(randint(1, 11))
                        self.rolls_d10.setText(', '.join([str(roll) for roll in rolls]))
                        self.total_d10.setText(str(sum(rolls)))

            if self.checkBox_d8.isChecked():
                rolls = []
                if int(self.input_d8.text()) > 10 or int(self.input_d8.text()) < 1:
                    raise ValueError
                else:
                    self.label_rollsd8.setText('Rolls:')
                    self.label_totald8.setText('Total:')
                    self.instructions.setText('')
                    for roll in range(int(self.input_d8.text())):
                        rolls.append(randint(1, 9))
                        self.rolls_d8.setText(', '.join([str(roll) for roll in rolls]))
                        self.total_d8.setText(str(sum(rolls)))

            if self.checkBox_d6.isChecked():
                rolls = []
                if int(self.input_d6.text()) > 10 or int(self.input_d6.text()) < 1:
                    raise ValueError
                else:
                    self.label_rollsd6.setText('Rolls:')
                    self.label_totald6.setText('Total:')
                    self.instructions.setText('')
                    for roll in range(int(self.input_d6.text())):
                        rolls.append(randint(1, 7))
                        self.rolls_d6.setText(', '.join([str(roll) for roll in rolls]))
                        self.total_d6.setText(str(sum(rolls)))

            if self.checkBox_d4.isChecked():
                rolls = []
                if int(self.input_d4.text()) > 10 or int(self.input_d4.text()) < 1:
                    raise ValueError
                else:
                    self.label_rollsd4.setText('Rolls:')
                    self.label_totald4.setText('Total:')
                    self.instructions.setText('')
                    for roll in range(int(self.input_d4.text())):
                        rolls.append(randint(1, 5))
                        self.rolls_d4.setText(', '.join([str(roll) for roll in rolls]))
                        self.total_d4.setText(str(sum(rolls)))
        except ValueError:
            self.instructions.setText('Please input a numerical dice amount from 1 - 10.')
            self.error_clear()

    def error_clear(self):
        """
        Function that clears output labels when invalid input is entered.
        :return:
        """
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
        self.label_rollsd100.setText('')
        self.label_rollsd20.setText('')
        self.label_rollsd12.setText('')
        self.label_rollsd10.setText('')
        self.label_rollsd8.setText('')
        self.label_rollsd6.setText('')
        self.label_rollsd4.setText('')
        self.label_totald100.setText('')
        self.label_totald20.setText('')
        self.label_totald12.setText('')
        self.label_totald10.setText('')
        self.label_totald8.setText('')
        self.label_totald6.setText('')
        self.label_totald4.setText('')

    def clear(self):
        """
        Function that resets the application.
        :return:
        """
        self.checkBox_d100.setChecked(False)
        self.checkBox_d20.setChecked(False)
        self.checkBox_d12.setChecked(False)
        self.checkBox_d10.setChecked(False)
        self.checkBox_d8.setChecked(False)
        self.checkBox_d6.setChecked(False)
        self.checkBox_d4.setChecked(False)
        self.input_d100.setEnabled(False)
        self.input_d20.setEnabled(False)
        self.input_d12.setEnabled(False)
        self.input_d10.setEnabled(False)
        self.input_d8.setEnabled(False)
        self.input_d6.setEnabled(False)
        self.input_d4.setEnabled(False)
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
        self.label_rollsd100.setText('')
        self.label_rollsd20.setText('')
        self.label_rollsd12.setText('')
        self.label_rollsd10.setText('')
        self.label_rollsd8.setText('')
        self.label_rollsd6.setText('')
        self.label_rollsd4.setText('')
        self.label_totald100.setText('')
        self.label_totald20.setText('')
        self.label_totald12.setText('')
        self.label_totald10.setText('')
        self.label_totald8.setText('')
        self.label_totald6.setText('')
        self.label_totald4.setText('')

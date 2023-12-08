from PyQt6.QtWidgets import *
from gui import *
from formulas import *


class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        """
        sets up the calculater
        """
        super().__init__()
        self.setupUi(self)

        self.calcbutton.clicked.connect(lambda: self.submit())
        self.clearbutton.clicked.connect(lambda: self.clear())
        self.radioButton.clicked.connect(lambda: self.chos1())
        self.radioButton_2.clicked.connect(lambda: self.chos2())
        self.radioButton_4.clicked.connect(lambda: self.chos4())
        self.radioButton_3.clicked.connect(lambda: self.chos3())

    def submit(self) -> None:
        """
        calculates the current displayed equation
        """
        try:
            input1 = float(self.input1.text())
            input2 = float(self.input2.text())
            if self.radioButton.isChecked():
                self.output.setText(f'Result: {add(input1, input2)}')
            elif self.radioButton_2.isChecked():
                self.output.setText(f'Result: {subtract(input1, input2)}')
            elif self.radioButton_4.isChecked():
                self.output.setText(f'Result: {multiply(input1, input2)}')
            elif self.radioButton_3.isChecked():
                self.output.setText(f'Result: {divide(input1, input2)}')
            self.errorout.setText('')

        except ValueError:
            self.output.setText('Result: ')
            self.errorout.setText('Type in numbers')

        except ZeroDivisionError:
            self.output.setText('Result: no :(')
            self.errorout.setText(f'Can\'t divide by zero')

    def clear(self) -> None:
        """
        removes the numbers from the equation, and sets it back to adding
        """
        self.output.setText('Result: ')
        self.errorout.setText('')
        self.input2.clear()
        self.input1.clear()
        self.radioButton.setChecked(True)
        self.signspot.setText('+')

    def chos1(self) -> None:  # chos1-4 was for chosen option 1-4
        """
        makes the equation symbol a plus
        """
        self.signspot.setText('+')

    def chos2(self) -> None:
        """
        makes the equation symbol a minus
        """
        self.signspot.setText('-')

    def chos4(self) -> None:
        """
        makes the equation symbol an asterisk
        """
        self.signspot.setText('*')

    def chos3(self) -> None:
        """
        makes the equation symbol a slash
        """
        self.signspot.setText('/')

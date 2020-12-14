"""
Documentation:                 Simple Calculator in QT5

Author:                                   Stanislav Sys

Date:                                        12.12.2020
"""

import PyQt5.QtWidgets as qtw


# create the app by inheriting from QWidget
class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("NoobGod Calculator")
        self.setLayout(qtw.QVBoxLayout())
        self.keypad()
        self.temp_nums = []
        self.fin_nums = []

        self.show()
    # this one will hold our Elements as a container in the widget

    def keypad(self):
        mycontainer = qtw.QWidget()
        mycontainer.setLayout(qtw.QGridLayout())

        # The Buttons
        # add seld to result field so you can acces it in the class
        self.btn_type_field = qtw.QLineEdit()
        btn_zero = qtw.QPushButton("0", clicked = lambda: self.num_press('0'))
        btn_one = qtw.QPushButton("1", clicked = lambda: self.num_press('1'))
        btn_two = qtw.QPushButton("2", clicked = lambda: self.num_press('2'))
        btn_three = qtw.QPushButton("3", clicked = lambda: self.num_press('3'))
        btn_four = qtw.QPushButton("4", clicked = lambda: self.num_press('4'))
        btn_five = qtw.QPushButton("5", clicked = lambda: self.num_press('5'))
        btn_six = qtw.QPushButton("6", clicked = lambda: self.num_press('6'))
        btn_seven = qtw.QPushButton("7", clicked = lambda: self.num_press('7'))
        btn_eight = qtw.QPushButton("8", clicked = lambda: self.num_press('8'))
        btn_nine = qtw.QPushButton("9", clicked = lambda: self.num_press('9'))
        btn_plus = qtw.QPushButton("+", clicked = lambda: self.func_press('+'))
        btn_minus = qtw.QPushButton("-", clicked = lambda: self.func_press('-'))
        btn_mult = qtw.QPushButton("*", clicked = lambda: self.func_press('*'))
        btn_div = qtw.QPushButton("÷", clicked = lambda: self.func_press('/'))
        btn_enter = qtw.QPushButton("Enter", clicked = self.func_result)
        btn_clear = qtw.QPushButton("Clear", clicked = self.clear_display)
        
        # Now the buttons need to be added to right coordinates
        # addWdget("WidgetName", row, column, rlength, clength)
        mycontainer.layout().addWidget(self.btn_type_field, 0, 0, 1, 4)
        mycontainer.layout().addWidget(btn_enter, 1, 0, 1, 2)
        mycontainer.layout().addWidget(btn_clear, 1, 2, 1, 2)
        mycontainer.layout().addWidget(btn_nine, 2, 0)
        mycontainer.layout().addWidget(btn_eight, 2, 1)
        mycontainer.layout().addWidget(btn_seven, 2, 2)
        mycontainer.layout().addWidget(btn_six, 3, 0)
        mycontainer.layout().addWidget(btn_five, 3, 1)
        mycontainer.layout().addWidget(btn_four, 3, 2)
        mycontainer.layout().addWidget(btn_three, 4, 0)
        mycontainer.layout().addWidget(btn_two, 4, 1)
        mycontainer.layout().addWidget(btn_one, 4, 2)
        mycontainer.layout().addWidget(btn_zero, 5, 0, 1, 3)
        mycontainer.layout().addWidget(btn_plus, 2, 3)
        mycontainer.layout().addWidget(btn_minus, 3, 3)
        mycontainer.layout().addWidget(btn_mult, 4, 3)
        mycontainer.layout().addWidget(btn_div, 5, 3)

        self.layout().addWidget(mycontainer)

    def num_press(self, key_number):
        self.temp_nums.append(key_number)
        temp_string = ''.join(self.temp_nums)
        if self.fin_nums:
            self.btn_type_field.setText(''.join(self.fin_nums) + temp_string)
        else:
            self.btn_type_field.setText(temp_string)

    def func_press(self, operator):
        temp_string = ''.join(self.temp_nums)
        self.fin_nums.append(temp_string)
        self.fin_nums.append(operator)
        self.temp_nums = []
        self.btn_type_field.setText(''.join(self.fin_nums))

    def func_result(self):
        fin_string = ''.join(self.fin_nums) + ''.join(self.temp_nums)
        result_string = eval(fin_string)
        fin_string += '='
        fin_string += str(result_string)
        self.btn_type_field.setText(fin_string)

    def clear_display(self):
        self.btn_type_field.clear()
        self.temp_nums = []
        self.fin_nums = []



# ctreate an instance and the main window
app = qtw.QApplication([])
mw = MainWindow()

# change the style so it's not that fugly
app.setStyle(qtw.QStyleFactory.create('Fusion'))

# this one starts the app
app.exec_()



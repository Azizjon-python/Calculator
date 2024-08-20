import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QCoreApplication
from calculyator_ui_2 import Ui_Kalkulyator_ilmiy  # Assuming the class is in kalkulyator_ilmiy.py

class Calculator(QMainWindow, Ui_Kalkulyator_ilmiy):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.connect_signals_slots()

    # def connect_signals_slots(self):
    #     self.btn_1.clicked.connect(lambda: self.append_number('1'))
    #     self.btn_2.clicked.connect(lambda: self.append_number('2'))
    #     self.btn_3.clicked.connect(lambda: self.append_number('3'))
    #     self.btn_4.clicked.connect(lambda: self.append_number('4'))
    #     self.btn_5.clicked.connect(lambda: self.append_number('5'))
    #     self.btn_6.clicked.connect(lambda: self.append_number('6'))
    #     self.btn_7.clicked.connect(lambda: self.append_number('7'))
    #     self.btn_8.clicked.connect(lambda: self.append_number('8'))
    #     self.btn_9.clicked.connect(lambda: self.append_number('9'))
    #     self.btn_nol.clicked.connect(lambda: self.append_number('0'))
    #     self.btn_clear.clicked.connect(self.clear_display)
    #     self.btn_qoshish.clicked.connect(lambda: self.append_operator('+'))
    #     self.btn_ayirish.clicked.connect(lambda: self.append_operator('-'))
    #     self.btn_kopaytirish.clicked.connect(lambda: self.append_operator('*'))
    #     self.btn_bolish.clicked.connect(lambda: self.append_operator('/'))
    #     self.btn_teng.clicked.connect(self.calculate_result)
    #     # Add more button connections as needed
    #
    # def append_number(self, number):
    #     current_text = self.label.text()
    #     new_text = current_text + number
    #     self.label.setText(new_text)
    #
    # def append_operator(self, operator):
    #     current_text = self.label.text()
    #     new_text = current_text + operator
    #     self.label.setText(new_text)
    #
    # def calculate_result(self):
    #     try:
    #         result = eval(self.label.text())
    #         self.label.setText(str(result))
    #     except Exception as e:
    #         self.label.setText("Error")
    #
    # def clear_display(self):
    #     self.label.setText("")



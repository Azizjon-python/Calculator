import sys
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import Qt
from calculator_ui_1 import Ui_Form

class Calculator_1(QWidget, Ui_Form):
    def __init__(self):
        super(Calculator_1, self).__init__()
        self.setupUi(self)

        self.user_input = ""
        self.init_ui()

    def init_ui(self):
        self.btn_clear.clicked.connect(self.clear)
        self.btn_qavs.clicked.connect(lambda: self.append_to_expression("()"))
        self.btn_foiz.clicked.connect(lambda: self.append_to_expression("%"))
        self.btn_bolish.clicked.connect(lambda: self.append_to_expression("/"))
        self.btn_kopaytirish.clicked.connect(lambda: self.append_to_expression("*"))
        self.btn_ayirish.clicked.connect(lambda: self.append_to_expression("-"))
        self.btn_qoshish.clicked.connect(lambda: self.append_to_expression("+"))

        self.btn_1.clicked.connect(lambda: self.append_to_expression("1"))
        self.btn_2.clicked.connect(lambda: self.append_to_expression("2"))
        self.btn_3.clicked.connect(lambda: self.append_to_expression("3"))
        self.btn_4.clicked.connect(lambda: self.append_to_expression("4"))
        self.btn_5.clicked.connect(lambda: self.append_to_expression("5"))
        self.btn_6.clicked.connect(lambda: self.append_to_expression("6"))
        self.btn_7.clicked.connect(lambda: self.append_to_expression("7"))
        self.btn_8.clicked.connect(lambda: self.append_to_expression("8"))
        self.btn_9.clicked.connect(lambda: self.append_to_expression("9"))
        self.btn_nol.clicked.connect(lambda: self.append_to_expression("0"))

        self.btn_teng.clicked.connect(self.calculate_result)
        self.btn_vergul.clicked.connect(lambda: self.append_to_expression("."))
        self.btn_ishora.clicked.connect(self.toggle_sign)
        self.ilmiy_rejim.clicked.connect(self.toggle_scientific_mode)

    def append_to_expression(self, value):
        if value == "()":
            open_paren_count = self.user_input.count('(')
            close_paren_count = self.user_input.count(')')
            if open_paren_count > close_paren_count:
                self.user_input += ")"
            else:
                self.user_input += "("
        else:
            self.user_input += value
        self.update_display()


    def calculate_result(self):
        try:
            self.user_input = str(eval(self.user_input))
        except Exception as e:
            self.user_input = "Error"
        self.update_display()

    def clear(self):
        self.user_input = ""
        self.update_display()

    def toggle_sign(self):
        if self.user_input.startswith('-'):
            self.user_input = self.user_input[1:]
        else:
            self.user_input = '-' + self.user_input
        self.update_display()

    def toggle_scientific_mode(self):
        # Implement scientific mode toggle if needed
        pass

    def update_display(self):
        self.label.setText(self.user_input)
        self.label_2.setText(self.user_input)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec())

from PySide6.QtWidgets import  QApplication
from a_kalkuulyator import Calculator_1


app = QApplication()
window = Calculator_1()

window.show()
app.exec()

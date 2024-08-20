from PySide6.QtWidgets import  QApplication
from b_kalkulyator import Calculator


app = QApplication()
window = Calculator()

window.show()
app.exec()

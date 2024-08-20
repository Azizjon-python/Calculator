from PySide6.QtWidgets import QApplication, QWidget
from asosiy import asos

app = QApplication()
window = asos()

window.show()
app.exec()

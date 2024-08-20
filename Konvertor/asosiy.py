from PySide6.QtWidgets import QWidget, QMessageBox
from convertor_ui import Ui_Form

class asos(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.valyuta = 12665
        self.lineEdit.textChanged.connect(self.chiqarish)
        self.lineEdit_2.textChanged.connect(self.chiqarish_2)
        self.pushButton.clicked.connect(self.chiqish)

    def chiqish(self):
        resent = QMessageBox.question(None, "Habar", "Chiqib ketishni xoxlaysizmi", QMessageBox.Yes | QMessageBox.No)
        if resent == QMessageBox.Yes:
            self.close()

    def chiqarish(self):
        try:
            qiymat = float(self.lineEdit.text())
            qiymat = round(qiymat / self.valyuta, 2)
            self.lineEdit_2.setText(str(qiymat))
        except ValueError:
            pass
    def chiqarish_2(self):
        try:
            qiymat = float(self.lineEdit_2.text())
            qiymat = round(qiymat / self.valyuta, 2)
            self.lineEdit.setText(str(qiymat))
        except:
            pass


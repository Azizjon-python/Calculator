from PySide6.QtWidgets import QApplication, QListWidget, QVBoxLayout, QLineEdit, QPushButton, QTextEdit
from PySide6.QtGui import QTextCursor

def search_word():
    search_text = search.text()
    text_content = lineEdit.toPlainText()
    cursor = lineEdit.textCursor()

    # Oldingi belgilashlarni tozalash
    cursor.clearSelection()

    # Qidirilayotgan so'z pozitsiyasini topish
    position = text_content.find(search_text)

    if position != -1:
        cursor.setPosition(position)
        cursor.movePosition(QTextCursor.Right, QTextCursor.KeepAnchor, len(search_text))
        lineEdit.setTextCursor(cursor)


app = QApplication([])
# oyna
window = QListWidget()
layout = QVBoxLayout()
window.setLayout(layout)

# qidirish uchun matn kiritish maydoni va tugma yaratish
search = QLineEdit()
search.setPlaceholderText("Qidiriladigan matnni kiriting")
layout.addWidget(search)

search_button = QPushButton("Search")
layout.addWidget(search_button)

# Matn oynasi yaratiladi
lineEdit = QTextEdit()
layout.addWidget(lineEdit)

# Qidirish tugmasini qidirish funksiyasiga ulash:
search_button.clicked.connect(search_word)

window.show()
app.exec()

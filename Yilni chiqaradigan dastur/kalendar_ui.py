# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerEEGAMy.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDateEdit, QLabel, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(346, 197)
        self.yil = QLabel(Form)
        self.yil.setObjectName(u"yil")
        self.yil.setGeometry(QRect(40, 30, 71, 31))
        self.sana = QDateEdit(Form)
        self.sana.setObjectName(u"sana")
        self.sana.setGeometry(QRect(200, 40, 110, 22))
        self.sana.setCalendarPopup(True)
        self.sanani_chiqarish = QLabel(Form)
        self.sanani_chiqarish.setObjectName(u"sanani_chiqarish")
        self.sanani_chiqarish.setGeometry(QRect(40, 100, 271, 71))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.yil.setText(QCoreApplication.translate("Form", u"Yilni kiriting", None))
        self.sanani_chiqarish.setText("")
    # retranslateUi


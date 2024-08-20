# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'kalkulyator_2dpyzyk.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import b_kalkulyator

class Ui_Kalkulyator_ilmiy(object):
    def setupUi(self, Kalkulyator_ilmiy):
        if not Kalkulyator_ilmiy.objectName():
            Kalkulyator_ilmiy.setObjectName(u"Kalkulyator_ilmiy")
        Kalkulyator_ilmiy.resize(408, 260)
        Kalkulyator_ilmiy.setMinimumSize(QSize(0, 260))
        Kalkulyator_ilmiy.setMaximumSize(QSize(440, 260))
        Kalkulyator_ilmiy.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(34, 34, 34);\n"
"}\n"
"QLabel {\n"
"	color: white;\n"
"}\n"
"QPushButton {\n"
"	background-color: rgb(0, 0, 0);\n"
"	font-size: 20px;\n"
"	color: white;\n"
"	\n"
"	min-width: 50px;\n"
"	min-height: 10px;\n"
"	max-width:75;\n"
"	max-height: 25;\n"
"	border-radius: 25px;\n"
"}\n"
"#btn_qavs,#btn_foiz,#btn_bolish,\n"
"#btn_kopaytirish,#btn_ayirish,\n"
"#btn_qoshish,btn_qoshish {\n"
"	\n"
"	color: rgb(85, 170, 0);\n"
"}")
        self.gridLayout_2 = QGridLayout(Kalkulyator_ilmiy)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(412, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 0, 0, 1, 2)

        self.label = QLabel(Kalkulyator_ilmiy)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(160, 35))
        self.label.setMaximumSize(QSize(16777215, 35))
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label, 0, 2, 1, 1)

        self.ilmiy_rejim = QPushButton(Kalkulyator_ilmiy)
        self.ilmiy_rejim.setObjectName(u"ilmiy_rejim")

        self.gridLayout_2.addWidget(self.ilmiy_rejim, 1, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(356, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 1, 1, 1)

        self.label_2 = QLabel(Kalkulyator_ilmiy)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(160, 35))
        self.label_2.setMaximumSize(QSize(16777215, 35))
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_2, 1, 2, 1, 1)

        self.frame = QFrame(Kalkulyator_ilmiy)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btn_rad_deg = QPushButton(self.frame)
        self.btn_rad_deg.setObjectName(u"btn_rad_deg")
        self.btn_rad_deg.setMaximumSize(QSize(75, 12))
        self.btn_rad_deg.setStyleSheet(u"	background-color: rgb(0, 0, 0);\n"
"	font-size: 20px;\n"
"	color: white;\n"
"	\n"
"	min-width: 50px;\n"
"	min-height: 10px;\n"
"	max-width:75;\n"
"	max-height: 12;\n"
"	border-radius: 25px;")
        icon = QIcon()
        icon.addFile(u":/img/rasmlar/\u0421\u043d\u0438\u043c\u043e\u043a \u044d\u043a\u0440\u0430\u043d\u0430 (193).png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_rad_deg.setIcon(icon)
        self.btn_rad_deg.setIconSize(QSize(50, 50))

        self.verticalLayout.addWidget(self.btn_rad_deg)

        self.pushButton_16 = QPushButton(self.frame)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setMaximumSize(QSize(75, 13))
        self.pushButton_16.setStyleSheet(u"	background-color: rgb(0, 0, 0);\n"
"	font-size: 20px;\n"
"	color: white;\n"
"	\n"
"	min-width: 50px;\n"
"	min-height: 10px;\n"
"	max-width:75;\n"
"	max-height: 13;\n"
"	border-radius: 25px;")
        icon1 = QIcon()
        icon1.addFile(u":/img/rasmlar/\u0421\u043d\u0438\u043c\u043e\u043a \u044d\u043a\u0440\u0430\u043d\u0430 (194).png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_16.setIcon(icon1)
        self.pushButton_16.setIconSize(QSize(40, 40))

        self.verticalLayout.addWidget(self.pushButton_16)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.btn_rad = QPushButton(self.frame)
        self.btn_rad.setObjectName(u"btn_rad")

        self.gridLayout.addWidget(self.btn_rad, 0, 1, 1, 1)

        self.btn_ildiz = QPushButton(self.frame)
        self.btn_ildiz.setObjectName(u"btn_ildiz")
        icon2 = QIcon()
        icon2.addFile(u":/img/rasmlar/\u0421\u043d\u0438\u043c\u043e\u043a \u044d\u043a\u0440\u0430\u043d\u0430 (191).png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_ildiz.setIcon(icon2)
        self.btn_ildiz.setIconSize(QSize(40, 40))

        self.gridLayout.addWidget(self.btn_ildiz, 0, 2, 1, 1)

        self.btn_clear = QPushButton(self.frame)
        self.btn_clear.setObjectName(u"btn_clear")
        self.btn_clear.setStyleSheet(u"color: rgb(200, 38, 49);")

        self.gridLayout.addWidget(self.btn_clear, 0, 3, 1, 1)

        self.btn_qavs = QPushButton(self.frame)
        self.btn_qavs.setObjectName(u"btn_qavs")

        self.gridLayout.addWidget(self.btn_qavs, 0, 4, 1, 1)

        self.btn_foiz = QPushButton(self.frame)
        self.btn_foiz.setObjectName(u"btn_foiz")

        self.gridLayout.addWidget(self.btn_foiz, 0, 5, 1, 1)

        self.btn_bolish = QPushButton(self.frame)
        self.btn_bolish.setObjectName(u"btn_bolish")

        self.gridLayout.addWidget(self.btn_bolish, 0, 6, 1, 1)

        self.btn_sin = QPushButton(self.frame)
        self.btn_sin.setObjectName(u"btn_sin")

        self.gridLayout.addWidget(self.btn_sin, 1, 0, 1, 1)

        self.btn_cos = QPushButton(self.frame)
        self.btn_cos.setObjectName(u"btn_cos")

        self.gridLayout.addWidget(self.btn_cos, 1, 1, 1, 1)

        self.btn_tan = QPushButton(self.frame)
        self.btn_tan.setObjectName(u"btn_tan")

        self.gridLayout.addWidget(self.btn_tan, 1, 2, 1, 1)

        self.btn_7 = QPushButton(self.frame)
        self.btn_7.setObjectName(u"btn_7")

        self.gridLayout.addWidget(self.btn_7, 1, 3, 1, 1)

        self.btn_8 = QPushButton(self.frame)
        self.btn_8.setObjectName(u"btn_8")

        self.gridLayout.addWidget(self.btn_8, 1, 4, 1, 1)

        self.btn_9 = QPushButton(self.frame)
        self.btn_9.setObjectName(u"btn_9")

        self.gridLayout.addWidget(self.btn_9, 1, 5, 1, 1)

        self.btn_kopaytirish = QPushButton(self.frame)
        self.btn_kopaytirish.setObjectName(u"btn_kopaytirish")

        self.gridLayout.addWidget(self.btn_kopaytirish, 1, 6, 1, 1)

        self.btn_ln = QPushButton(self.frame)
        self.btn_ln.setObjectName(u"btn_ln")

        self.gridLayout.addWidget(self.btn_ln, 2, 0, 1, 1)

        self.btn_log = QPushButton(self.frame)
        self.btn_log.setObjectName(u"btn_log")

        self.gridLayout.addWidget(self.btn_log, 2, 1, 1, 1)

        self.btn_1x = QPushButton(self.frame)
        self.btn_1x.setObjectName(u"btn_1x")

        self.gridLayout.addWidget(self.btn_1x, 2, 2, 1, 1)

        self.btn_4 = QPushButton(self.frame)
        self.btn_4.setObjectName(u"btn_4")

        self.gridLayout.addWidget(self.btn_4, 2, 3, 1, 1)

        self.btn_5 = QPushButton(self.frame)
        self.btn_5.setObjectName(u"btn_5")

        self.gridLayout.addWidget(self.btn_5, 2, 4, 1, 1)

        self.btn_6 = QPushButton(self.frame)
        self.btn_6.setObjectName(u"btn_6")

        self.gridLayout.addWidget(self.btn_6, 2, 5, 1, 1)

        self.btn_ayirish = QPushButton(self.frame)
        self.btn_ayirish.setObjectName(u"btn_ayirish")

        self.gridLayout.addWidget(self.btn_ayirish, 2, 6, 1, 1)

        self.btn_ex = QPushButton(self.frame)
        self.btn_ex.setObjectName(u"btn_ex")
        icon3 = QIcon()
        icon3.addFile(u":/img/rasmlar/\u0421\u043d\u0438\u043c\u043e\u043a \u044d\u043a\u0440\u0430\u043d\u0430 (187).png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_ex.setIcon(icon3)
        self.btn_ex.setIconSize(QSize(40, 40))

        self.gridLayout.addWidget(self.btn_ex, 3, 0, 1, 1)

        self.btn_x2 = QPushButton(self.frame)
        self.btn_x2.setObjectName(u"btn_x2")
        icon4 = QIcon()
        icon4.addFile(u":/img/rasmlar/\u0421\u043d\u0438\u043c\u043e\u043a \u044d\u043a\u0440\u0430\u043d\u0430 (188).png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_x2.setIcon(icon4)
        self.btn_x2.setIconSize(QSize(40, 40))

        self.gridLayout.addWidget(self.btn_x2, 3, 1, 1, 1)

        self.btn_xy = QPushButton(self.frame)
        self.btn_xy.setObjectName(u"btn_xy")
        icon5 = QIcon()
        icon5.addFile(u":/img/rasmlar/\u0421\u043d\u0438\u043c\u043e\u043a \u044d\u043a\u0440\u0430\u043d\u0430 (189).png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_xy.setIcon(icon5)
        self.btn_xy.setIconSize(QSize(40, 40))

        self.gridLayout.addWidget(self.btn_xy, 3, 2, 1, 1)

        self.btn_1 = QPushButton(self.frame)
        self.btn_1.setObjectName(u"btn_1")

        self.gridLayout.addWidget(self.btn_1, 3, 3, 1, 1)

        self.btn_2 = QPushButton(self.frame)
        self.btn_2.setObjectName(u"btn_2")

        self.gridLayout.addWidget(self.btn_2, 3, 4, 1, 1)

        self.btn_3 = QPushButton(self.frame)
        self.btn_3.setObjectName(u"btn_3")

        self.gridLayout.addWidget(self.btn_3, 3, 5, 1, 1)

        self.btn_qoshish = QPushButton(self.frame)
        self.btn_qoshish.setObjectName(u"btn_qoshish")

        self.gridLayout.addWidget(self.btn_qoshish, 3, 6, 1, 1)

        self.btn_x = QPushButton(self.frame)
        self.btn_x.setObjectName(u"btn_x")

        self.gridLayout.addWidget(self.btn_x, 4, 0, 1, 1)

        self.btn_p = QPushButton(self.frame)
        self.btn_p.setObjectName(u"btn_p")
        icon6 = QIcon()
        icon6.addFile(u":/img/rasmlar/\u0421\u043d\u0438\u043c\u043e\u043a \u044d\u043a\u0440\u0430\u043d\u0430 (190).png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_p.setIcon(icon6)
        self.btn_p.setIconSize(QSize(40, 40))

        self.gridLayout.addWidget(self.btn_p, 4, 1, 1, 1)

        self.btn_e = QPushButton(self.frame)
        self.btn_e.setObjectName(u"btn_e")

        self.gridLayout.addWidget(self.btn_e, 4, 2, 1, 1)

        self.btn_ishora = QPushButton(self.frame)
        self.btn_ishora.setObjectName(u"btn_ishora")

        self.gridLayout.addWidget(self.btn_ishora, 4, 3, 1, 1)

        self.btn_nol = QPushButton(self.frame)
        self.btn_nol.setObjectName(u"btn_nol")

        self.gridLayout.addWidget(self.btn_nol, 4, 4, 1, 1)

        self.btn_vergul = QPushButton(self.frame)
        self.btn_vergul.setObjectName(u"btn_vergul")

        self.gridLayout.addWidget(self.btn_vergul, 4, 5, 1, 1)

        self.btn_teng = QPushButton(self.frame)
        self.btn_teng.setObjectName(u"btn_teng")

        self.gridLayout.addWidget(self.btn_teng, 4, 6, 1, 1)


        self.gridLayout_2.addWidget(self.frame, 2, 0, 1, 3)


        self.retranslateUi(Kalkulyator_ilmiy)

        QMetaObject.connectSlotsByName(Kalkulyator_ilmiy)
    # setupUi

    def retranslateUi(self, Kalkulyator_ilmiy):
        Kalkulyator_ilmiy.setWindowTitle(QCoreApplication.translate("Kalkulyator_ilmiy", u"Form", None))
        self.label.setText(QCoreApplication.translate("Kalkulyator_ilmiy", u"0", None))
        self.ilmiy_rejim.setText(QCoreApplication.translate("Kalkulyator_ilmiy", u"abc", None))
        self.label_2.setText(QCoreApplication.translate("Kalkulyator_ilmiy", u"0", None))
        self.btn_rad_deg.setText("")
        self.pushButton_16.setText("")
        self.btn_rad.setText(QCoreApplication.translate("Kalkulyator_ilmiy", u"Rad", None))
        self.btn_ildiz.setText("")
        self.btn_clear.setText(QCoreApplication.translate("Kalkulyator_ilmiy", u"C", None))
        self.btn_qavs.setText(QCoreApplication.translate("Kalkulyator_ilmiy", u"()", None))
        self.btn_foiz.setText(QCoreApplication.translate("Kalkulyator_ilmiy", u"%", None))
        self.btn_bolish.setText(QCoreApplication.translate("Kalkulyator_ilmiy", u"/", None))
        self.btn_sin.setText(QCoreApplication.translate("Kalkulyator_ilmiy", u"sin", None))
        self.btn_cos.setText(QCoreApplication.translate("Kalkulyator_ilmiy", u"cos", None))
        self.btn_tan.setText(QCoreApplication.translate("Kalkulyator_ilmiy", u"tan", None))
        self.btn_7.setText(QCoreApplication.translate("Kalkulyator_ilmiy", u"7", None))
        self.btn_8.setText(QCoreApplication.translate("Kalkulyator_ilmiy", u"8", None))
        self.btn_9.setText(QCoreApplication.translate("Kalkulyator_ilmiy", u"9", None))
        self.btn_kopaytirish.setText(QCoreApplication.translate("Kalkulyator_ilmiy", u"*", None))
        self.btn_ln.setText(QCoreApplication.translate("Kalkulyator_ilmiy", u"ln", None))
        self.btn_log.setText(QCoreApplication.translate("Kalkulyator_ilmiy", u"log", None))
        self.btn_1x.setText(QCoreApplication.translate("Kalkulyator_ilmiy", u"1/x", None))
        self.btn_4.setText(QCoreApplication.translate("Kalkulyator_ilmiy", u"4", None))
        self.btn_5.setText(QCoreApplication.translate("Kalkulyator_ilmiy", u"5", None))
        self.btn_6.setText(QCoreApplication.translate("Kalkulyator_ilmiy", u"6", None))
        self.btn_ayirish.setText(QCoreApplication.translate("Kalkulyator_ilmiy", u"-", None))
        self.btn_ex.setText("")
        self.btn_x2.setText("")
        self.btn_xy.setText("")
        self.btn_1.setText(QCoreApplication.translate("Kalkulyator_ilmiy", u"1", None))
        self.btn_2.setText(QCoreApplication.translate("Kalkulyator_ilmiy", u"2", None))
        self.btn_3.setText(QCoreApplication.translate("Kalkulyator_ilmiy", u"3", None))
        self.btn_qoshish.setText(QCoreApplication.translate("Kalkulyator_ilmiy", u"+", None))
        self.btn_x.setText(QCoreApplication.translate("Kalkulyator_ilmiy", u"|x|", None))
        self.btn_p.setText("")
        self.btn_e.setText(QCoreApplication.translate("Kalkulyator_ilmiy", u"e", None))
        self.btn_ishora.setText(QCoreApplication.translate("Kalkulyator_ilmiy", u"+/-", None))
        self.btn_nol.setText(QCoreApplication.translate("Kalkulyator_ilmiy", u"0", None))
        self.btn_vergul.setText(QCoreApplication.translate("Kalkulyator_ilmiy", u",", None))
        self.btn_teng.setText(QCoreApplication.translate("Kalkulyator_ilmiy", u"=", None))
    # retranslateUi


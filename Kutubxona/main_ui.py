# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'kutubxona-1BgOuJv.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableWidget,
    QTableWidgetItem, QToolButton, QVBoxLayout, QWidget)
import res_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(806, 586)
        self.gridLayout_9 = QGridLayout(Form)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(Form)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_2 = QGridLayout(self.page)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tepa_qismi = QWidget(self.page)
        self.tepa_qismi.setObjectName(u"tepa_qismi")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tepa_qismi.sizePolicy().hasHeightForWidth())
        self.tepa_qismi.setSizePolicy(sizePolicy)
        self.tepa_qismi.setMinimumSize(QSize(0, 50))
        self.tepa_qismi.setMaximumSize(QSize(16777215, 50))
        self.tepa_qismi.setStyleSheet(u"background-color: rgb(73, 0, 229);\n"
"color:white;\n"
"font-size: 15px;")
        self.horizontalLayout_2 = QHBoxLayout(self.tepa_qismi)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.burger_button = QPushButton(self.tepa_qismi)
        self.burger_button.setObjectName(u"burger_button")
        self.burger_button.setStyleSheet(u"border: none;")
        icon = QIcon()
        icon.addFile(u":/ism/images/burger_menu_w.png", QSize(), QIcon.Normal, QIcon.Off)
        self.burger_button.setIcon(icon)
        self.burger_button.setIconSize(QSize(40, 40))
        self.burger_button.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.burger_button)

        self.label = QLabel(self.tepa_qismi)
        self.label.setObjectName(u"label")
        font = QFont()
        self.label.setFont(font)

        self.horizontalLayout_2.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(198, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.label_2 = QLabel(self.tepa_qismi)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(35, 35))
        self.label_2.setMaximumSize(QSize(35, 35))
        self.label_2.setPixmap(QPixmap(u":/ism/images/account_circle.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.tepa_qismi)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.btn_chiqish = QToolButton(self.tepa_qismi)
        self.btn_chiqish.setObjectName(u"btn_chiqish")
        self.btn_chiqish.setStyleSheet(u"border: none;")
        icon1 = QIcon()
        icon1.addFile(u":/ism/images/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_chiqish.setIcon(icon1)
        self.btn_chiqish.setIconSize(QSize(40, 40))

        self.horizontalLayout_2.addWidget(self.btn_chiqish)


        self.gridLayout_2.addWidget(self.tepa_qismi, 0, 0, 1, 3)

        self.chap_menyu = QWidget(self.page)
        self.chap_menyu.setObjectName(u"chap_menyu")
        self.chap_menyu.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(52, 51, 52);\n"
"}\n"
"\n"
"QPushButton {\n"
"	color: grey;\n"
"padding: 5px 1px;\n"
"text-align: left;\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"color: white;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.chap_menyu)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 10, 20, 10)
        self.btn_menu_asosiy = QPushButton(self.chap_menyu)
        self.btn_menu_asosiy.setObjectName(u"btn_menu_asosiy")
        icon2 = QIcon()
        icon2.addFile(u":/ism/images/home_grey.png", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/ism/images/home.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_menu_asosiy.setIcon(icon2)
        self.btn_menu_asosiy.setCheckable(True)
        self.btn_menu_asosiy.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.btn_menu_asosiy)

        self.btn_menu_kitoblar = QPushButton(self.chap_menyu)
        self.btn_menu_kitoblar.setObjectName(u"btn_menu_kitoblar")
        icon3 = QIcon()
        icon3.addFile(u":/ism/images/books_grey.png", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/ism/images/books_white.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_menu_kitoblar.setIcon(icon3)
        self.btn_menu_kitoblar.setCheckable(True)
        self.btn_menu_kitoblar.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.btn_menu_kitoblar)

        self.btn_menu_talabalar = QPushButton(self.chap_menyu)
        self.btn_menu_talabalar.setObjectName(u"btn_menu_talabalar")
        icon4 = QIcon()
        icon4.addFile(u":/ism/images/group_grey.png", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u":/ism/images/group_white.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_menu_talabalar.setIcon(icon4)
        self.btn_menu_talabalar.setCheckable(True)
        self.btn_menu_talabalar.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.btn_menu_talabalar)

        self.btn_menu_o_kitoblar = QPushButton(self.chap_menyu)
        self.btn_menu_o_kitoblar.setObjectName(u"btn_menu_o_kitoblar")
        icon5 = QIcon()
        icon5.addFile(u":/ism/images/taken_book_black.png", QSize(), QIcon.Normal, QIcon.Off)
        icon5.addFile(u":/ism/images/taken_book_white.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_menu_o_kitoblar.setIcon(icon5)
        self.btn_menu_o_kitoblar.setCheckable(True)
        self.btn_menu_o_kitoblar.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.btn_menu_o_kitoblar)

        self.btn_menu_m_kitoblar = QPushButton(self.chap_menyu)
        self.btn_menu_m_kitoblar.setObjectName(u"btn_menu_m_kitoblar")
        icon6 = QIcon()
        icon6.addFile(u":/ism/images/hourglass_grey.png", QSize(), QIcon.Normal, QIcon.Off)
        icon6.addFile(u":/ism/images/hourglass_white.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_menu_m_kitoblar.setIcon(icon6)
        self.btn_menu_m_kitoblar.setCheckable(True)
        self.btn_menu_m_kitoblar.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.btn_menu_m_kitoblar)

        self.verticalSpacer = QSpacerItem(20, 225, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.btn_menu_chiqish = QPushButton(self.chap_menyu)
        self.btn_menu_chiqish.setObjectName(u"btn_menu_chiqish")
        self.btn_menu_chiqish.setIcon(icon1)
        self.btn_menu_chiqish.setCheckable(True)
        self.btn_menu_chiqish.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.btn_menu_chiqish)


        self.gridLayout_2.addWidget(self.chap_menyu, 1, 0, 1, 1)

        self.chap_kichik_menyu = QWidget(self.page)
        self.chap_kichik_menyu.setObjectName(u"chap_kichik_menyu")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.chap_kichik_menyu.sizePolicy().hasHeightForWidth())
        self.chap_kichik_menyu.setSizePolicy(sizePolicy1)
        self.chap_kichik_menyu.setMinimumSize(QSize(60, 0))
        self.chap_kichik_menyu.setMaximumSize(QSize(60, 16777215))
        self.chap_kichik_menyu.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(52, 51, 52);\n"
"}\n"
"\n"
"QPushButton {\n"
"	color: grey;\n"
"padding: 5px 1px;\n"
"text-align: left;\n"
"border: none;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.chap_kichik_menyu)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(20, 10, 20, 10)
        self.btn_menu_asosiy2 = QPushButton(self.chap_kichik_menyu)
        self.btn_menu_asosiy2.setObjectName(u"btn_menu_asosiy2")
        self.btn_menu_asosiy2.setIcon(icon2)
        self.btn_menu_asosiy2.setCheckable(True)
        self.btn_menu_asosiy2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.btn_menu_asosiy2)

        self.btn_menu_kitoblar2 = QPushButton(self.chap_kichik_menyu)
        self.btn_menu_kitoblar2.setObjectName(u"btn_menu_kitoblar2")
        self.btn_menu_kitoblar2.setIcon(icon3)
        self.btn_menu_kitoblar2.setCheckable(True)
        self.btn_menu_kitoblar2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.btn_menu_kitoblar2)

        self.btn_menu_talabalar_2 = QPushButton(self.chap_kichik_menyu)
        self.btn_menu_talabalar_2.setObjectName(u"btn_menu_talabalar_2")
        self.btn_menu_talabalar_2.setIcon(icon4)
        self.btn_menu_talabalar_2.setCheckable(True)
        self.btn_menu_talabalar_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.btn_menu_talabalar_2)

        self.btn_menu_o_kitoblar2 = QPushButton(self.chap_kichik_menyu)
        self.btn_menu_o_kitoblar2.setObjectName(u"btn_menu_o_kitoblar2")
        self.btn_menu_o_kitoblar2.setIcon(icon5)
        self.btn_menu_o_kitoblar2.setCheckable(True)
        self.btn_menu_o_kitoblar2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.btn_menu_o_kitoblar2)

        self.btn_menu_m_kitoblar_2 = QPushButton(self.chap_kichik_menyu)
        self.btn_menu_m_kitoblar_2.setObjectName(u"btn_menu_m_kitoblar_2")
        self.btn_menu_m_kitoblar_2.setIcon(icon6)
        self.btn_menu_m_kitoblar_2.setCheckable(True)
        self.btn_menu_m_kitoblar_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.btn_menu_m_kitoblar_2)

        self.verticalSpacer_2 = QSpacerItem(20, 177, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.btn_menu_chiqish2 = QPushButton(self.chap_kichik_menyu)
        self.btn_menu_chiqish2.setObjectName(u"btn_menu_chiqish2")
        self.btn_menu_chiqish2.setIcon(icon1)
        self.btn_menu_chiqish2.setCheckable(True)
        self.btn_menu_chiqish2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.btn_menu_chiqish2)


        self.gridLayout_2.addWidget(self.chap_kichik_menyu, 1, 1, 1, 1)

        self.asosi_qism = QWidget(self.page)
        self.asosi_qism.setObjectName(u"asosi_qism")
        self.asosi_qism.setStyleSheet(u"background-color: red;")
        self.horizontalLayout = QHBoxLayout(self.asosi_qism)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(454, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.gridLayout_2.addWidget(self.asosi_qism, 1, 2, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout = QGridLayout(self.page_2)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.kitob_chap_taraf = QWidget(self.page_2)
        self.kitob_chap_taraf.setObjectName(u"kitob_chap_taraf")
        self.kitob_chap_taraf.setMinimumSize(QSize(300, 0))
        self.kitob_chap_taraf.setMaximumSize(QSize(300, 16777215))
        self.kitob_chap_taraf.setStyleSheet(u"QWidget {\n"
"	background-color: #646fff;\n"
"	color: white;\n"
"	font-size: 13px;\n"
"}\n"
"QPushButton {\n"
"	background-color: rgb(255, 0, 0);\n"
"\n"
"}\n"
"QLineEdit {\n"
"	border: none;\n"
"	border-bottom-style: solid;\n"
"	border-bottom-color: white;\n"
"	border-bottom-width: 2px;\n"
"	color: black;\n"
"}\n"
"#btn_kitob_kiritish, #btn_kitob_ozgartirish, #btn_kitob_ochirish {\n"
"	border-radius: 7px;\n"
"	padding: 4px;\n"
"	wight: 60px;\n"
"\n"
"\n"
"}")
        self.gridLayout_5 = QGridLayout(self.kitob_chap_taraf)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_kitob_orqaga = QPushButton(self.kitob_chap_taraf)
        self.btn_kitob_orqaga.setObjectName(u"btn_kitob_orqaga")

        self.gridLayout_5.addWidget(self.btn_kitob_orqaga, 0, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(198, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_4, 0, 1, 1, 1)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(20, 40, 20, 20)
        self.label_11 = QLabel(self.kitob_chap_taraf)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(25, 25))
        self.label_11.setMaximumSize(QSize(25, 25))
        self.label_11.setPixmap(QPixmap(u":/ism/images/taken_book_white.png"))
        self.label_11.setScaledContents(True)

        self.gridLayout_6.addWidget(self.label_11, 1, 0, 1, 1)

        self.btn_muallif_nomi = QLabel(self.kitob_chap_taraf)
        self.btn_muallif_nomi.setObjectName(u"btn_muallif_nomi")

        self.gridLayout_6.addWidget(self.btn_muallif_nomi, 2, 1, 1, 1)

        self.btn_kitob_nomi = QLabel(self.kitob_chap_taraf)
        self.btn_kitob_nomi.setObjectName(u"btn_kitob_nomi")
        self.btn_kitob_nomi.setMinimumSize(QSize(25, 25))
        self.btn_kitob_nomi.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_6.addWidget(self.btn_kitob_nomi, 0, 1, 1, 1)

        self.label_15 = QLabel(self.kitob_chap_taraf)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(25, 25))
        self.label_15.setMaximumSize(QSize(25, 25))
        self.label_15.setPixmap(QPixmap(u":/ism/images/hourglass_white.png"))
        self.label_15.setScaledContents(True)

        self.gridLayout_6.addWidget(self.label_15, 5, 0, 1, 1)

        self.edt_kitob_soni = QLineEdit(self.kitob_chap_taraf)
        self.edt_kitob_soni.setObjectName(u"edt_kitob_soni")

        self.gridLayout_6.addWidget(self.edt_kitob_soni, 5, 1, 1, 1)

        self.edt_kitob_nomi = QLineEdit(self.kitob_chap_taraf)
        self.edt_kitob_nomi.setObjectName(u"edt_kitob_nomi")

        self.gridLayout_6.addWidget(self.edt_kitob_nomi, 1, 1, 1, 1)

        self.btn_kitob_soni = QLabel(self.kitob_chap_taraf)
        self.btn_kitob_soni.setObjectName(u"btn_kitob_soni")

        self.gridLayout_6.addWidget(self.btn_kitob_soni, 4, 1, 1, 1)

        self.edt_muallif_nomi = QLineEdit(self.kitob_chap_taraf)
        self.edt_muallif_nomi.setObjectName(u"edt_muallif_nomi")

        self.gridLayout_6.addWidget(self.edt_muallif_nomi, 3, 1, 1, 1)

        self.label_13 = QLabel(self.kitob_chap_taraf)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(25, 25))
        self.label_13.setMaximumSize(QSize(25, 25))
        self.label_13.setPixmap(QPixmap(u":/ism/images/group_white.png"))
        self.label_13.setScaledContents(True)

        self.gridLayout_6.addWidget(self.label_13, 3, 0, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_6, 1, 0, 1, 2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(20, 10, 20, 10)
        self.btn_kitob_ochirish = QPushButton(self.kitob_chap_taraf)
        self.btn_kitob_ochirish.setObjectName(u"btn_kitob_ochirish")

        self.horizontalLayout_4.addWidget(self.btn_kitob_ochirish)

        self.btn_kitob_kiritish = QPushButton(self.kitob_chap_taraf)
        self.btn_kitob_kiritish.setObjectName(u"btn_kitob_kiritish")

        self.horizontalLayout_4.addWidget(self.btn_kitob_kiritish)

        self.btn_kitob_ozgartirish = QPushButton(self.kitob_chap_taraf)
        self.btn_kitob_ozgartirish.setObjectName(u"btn_kitob_ozgartirish")

        self.horizontalLayout_4.addWidget(self.btn_kitob_ozgartirish)


        self.gridLayout_5.addLayout(self.horizontalLayout_4, 2, 0, 1, 2)

        self.verticalSpacer_4 = QSpacerItem(20, 240, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_4, 3, 0, 1, 1)


        self.gridLayout.addWidget(self.kitob_chap_taraf, 0, 0, 1, 1)

        self.kitob_ong_taraf = QWidget(self.page_2)
        self.kitob_ong_taraf.setObjectName(u"kitob_ong_taraf")
        self.kitob_ong_taraf.setStyleSheet(u"QPushButton {\n"
"	background-color: #646fff;\n"
"	width: 70px;\n"
"	height: 20px;\n"
"}\n"
"\n"
"#lbl_sarlavha {\n"
"	color: red;\n"
"	font-size: 20px;\n"
"	font-weight: 600;\n"
"}\n"
"#lbl_chiziq {\n"
"	border: none;\n"
"	border-bottom-color: red;\n"
"	border-bottom-style: solid;\n"
"	border-bottom-width: 4px;\n"
"	height: 0;\n"
"}\n"
"\n"
"QTable Widget {\n"
"	margin: 20px;\n"
"}\n"
"\n"
"QHeaderView::section:horizontal {\n"
"	background-color: rgb(100, 111, 255);\n"
"	color: white;\n"
"	font-weight: 700;\n"
"}\n"
"QHeaderView::section:vertical {\n"
"	background-color: rgb(100, 111, 255);\n"
"	color: white;\n"
"	font-weight: 700;\n"
"}")
        self.gridLayout_10 = QGridLayout(self.kitob_ong_taraf)
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_6 = QSpacerItem(171, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setHorizontalSpacing(20)
        self.gridLayout_7.setVerticalSpacing(10)
        self.gridLayout_7.setContentsMargins(-1, 20, -1, 40)
        self.label_16 = QLabel(self.kitob_ong_taraf)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(30, 30))
        self.label_16.setPixmap(QPixmap(u":/ism/G:/rasmlar/library_books_24dp_EA3323_FILL0_wght400_GRAD0_opsz24.png"))
        self.label_16.setScaledContents(True)
        self.label_16.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.label_16, 0, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_3, 0, 0, 1, 2)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_8, 0, 4, 1, 1)

        self.lbl_chiziq = QLabel(self.kitob_ong_taraf)
        self.lbl_chiziq.setObjectName(u"lbl_chiziq")
        self.lbl_chiziq.setMaximumSize(QSize(16777215, 2))

        self.gridLayout_7.addWidget(self.lbl_chiziq, 1, 0, 1, 5)

        self.lbl_sarlavha = QLabel(self.kitob_ong_taraf)
        self.lbl_sarlavha.setObjectName(u"lbl_sarlavha")
        self.lbl_sarlavha.setMinimumSize(QSize(175, 0))
        self.lbl_sarlavha.setScaledContents(False)
        self.lbl_sarlavha.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.lbl_sarlavha, 0, 3, 1, 1)


        self.horizontalLayout_6.addLayout(self.gridLayout_7)

        self.horizontalSpacer_7 = QSpacerItem(170, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_7)


        self.gridLayout_10.addLayout(self.horizontalLayout_6, 1, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_5 = QSpacerItem(306, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.btn_chiqish2 = QPushButton(self.kitob_ong_taraf)
        self.btn_chiqish2.setObjectName(u"btn_chiqish2")
        self.btn_chiqish2.setMinimumSize(QSize(0, 20))
        self.btn_chiqish2.setMaximumSize(QSize(100, 16777215))
        self.btn_chiqish2.setIcon(icon1)
        self.btn_chiqish2.setIconSize(QSize(30, 30))

        self.horizontalLayout_5.addWidget(self.btn_chiqish2)


        self.gridLayout_10.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)

        self.tableWidget = QTableWidget(self.kitob_ong_taraf)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout_10.addWidget(self.tableWidget, 2, 0, 1, 1)


        self.gridLayout.addWidget(self.kitob_ong_taraf, 0, 2, 1, 1)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_28 = QGridLayout(self.page_3)
        self.gridLayout_28.setSpacing(0)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.gridLayout_28.setContentsMargins(0, 0, 0, 0)
        self.kitob_chap_taraf_4 = QWidget(self.page_3)
        self.kitob_chap_taraf_4.setObjectName(u"kitob_chap_taraf_4")
        self.kitob_chap_taraf_4.setMinimumSize(QSize(300, 0))
        self.kitob_chap_taraf_4.setMaximumSize(QSize(300, 16777215))
        self.kitob_chap_taraf_4.setStyleSheet(u"QWidget {\n"
"	background-color: #646fff;\n"
"	color: white;\n"
"	font-size: 13px;\n"
"}\n"
"QPushButton {\n"
"	background-color: rgb(255, 0, 0);\n"
"\n"
"}\n"
"QLineEdit {\n"
"	border: none;\n"
"	border-bottom-style: solid;\n"
"	border-bottom-color: white;\n"
"	border-bottom-width: 2px;\n"
"	color: black;\n"
"}\n"
"#btn_talaba_kiritish, #btn_talaba_ozgartirish, #btn_talaba_ochirish {\n"
"	border-radius: 7px;\n"
"	padding: 4px;\n"
"	wight: 60px;\n"
"\n"
"\n"
"}\n"
"QComboBox {\n"
"	border: none;\n"
"	border-bottom-style: solid;\n"
"	border-bottom-color: white;\n"
"	border-bottom-width: 2px;\n"
"	padding: 4px;\n"
"	wight: 60px;\n"
"\n"
"}")
        self.gridLayout_26 = QGridLayout(self.kitob_chap_taraf_4)
        self.gridLayout_26.setSpacing(0)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.gridLayout_26.setContentsMargins(0, 0, 0, 0)
        self.btn_talaba_orqaga = QPushButton(self.kitob_chap_taraf_4)
        self.btn_talaba_orqaga.setObjectName(u"btn_talaba_orqaga")

        self.gridLayout_26.addWidget(self.btn_talaba_orqaga, 0, 0, 1, 1)

        self.horizontalSpacer_36 = QSpacerItem(198, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_26.addItem(self.horizontalSpacer_36, 0, 1, 1, 1)

        self.gridLayout_27 = QGridLayout()
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.gridLayout_27.setContentsMargins(20, 40, 20, 20)
        self.btn_kitob_nomi_5 = QLabel(self.kitob_chap_taraf_4)
        self.btn_kitob_nomi_5.setObjectName(u"btn_kitob_nomi_5")
        self.btn_kitob_nomi_5.setMinimumSize(QSize(25, 25))
        self.btn_kitob_nomi_5.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_27.addWidget(self.btn_kitob_nomi_5, 0, 1, 1, 1)

        self.label_30 = QLabel(self.kitob_chap_taraf_4)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(25, 25))
        self.label_30.setMaximumSize(QSize(25, 25))
        self.label_30.setPixmap(QPixmap(u":/ism/images/hourglass_white.png"))
        self.label_30.setScaledContents(True)

        self.gridLayout_27.addWidget(self.label_30, 3, 0, 1, 1)

        self.btn_muallif_nomi_5 = QLabel(self.kitob_chap_taraf_4)
        self.btn_muallif_nomi_5.setObjectName(u"btn_muallif_nomi_5")

        self.gridLayout_27.addWidget(self.btn_muallif_nomi_5, 2, 1, 1, 1)

        self.label_28 = QLabel(self.kitob_chap_taraf_4)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMinimumSize(QSize(25, 25))
        self.label_28.setMaximumSize(QSize(25, 25))
        self.label_28.setPixmap(QPixmap(u":/ism/images/account_circle.png"))
        self.label_28.setScaledContents(True)

        self.gridLayout_27.addWidget(self.label_28, 1, 0, 1, 1)

        self.comboBox = QComboBox(self.kitob_chap_taraf_4)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_27.addWidget(self.comboBox, 3, 1, 1, 1)

        self.edt_talaba_nomi = QLineEdit(self.kitob_chap_taraf_4)
        self.edt_talaba_nomi.setObjectName(u"edt_talaba_nomi")
        self.edt_talaba_nomi.setEnabled(True)
        self.edt_talaba_nomi.setReadOnly(False)

        self.gridLayout_27.addWidget(self.edt_talaba_nomi, 1, 1, 1, 1)


        self.gridLayout_26.addLayout(self.gridLayout_27, 1, 0, 1, 2)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setSpacing(10)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(20, 10, 20, 10)
        self.btn_talaba_ochirish = QPushButton(self.kitob_chap_taraf_4)
        self.btn_talaba_ochirish.setObjectName(u"btn_talaba_ochirish")

        self.horizontalLayout_21.addWidget(self.btn_talaba_ochirish)

        self.btn_talaba_kiritish = QPushButton(self.kitob_chap_taraf_4)
        self.btn_talaba_kiritish.setObjectName(u"btn_talaba_kiritish")

        self.horizontalLayout_21.addWidget(self.btn_talaba_kiritish)

        self.btn_talaba_ozgartirish = QPushButton(self.kitob_chap_taraf_4)
        self.btn_talaba_ozgartirish.setObjectName(u"btn_talaba_ozgartirish")

        self.horizontalLayout_21.addWidget(self.btn_talaba_ozgartirish)


        self.gridLayout_26.addLayout(self.horizontalLayout_21, 2, 0, 1, 2)

        self.verticalSpacer_11 = QSpacerItem(20, 240, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_26.addItem(self.verticalSpacer_11, 3, 0, 1, 1)


        self.gridLayout_28.addWidget(self.kitob_chap_taraf_4, 0, 0, 1, 1)

        self.kitob_ong_taraf_4 = QWidget(self.page_3)
        self.kitob_ong_taraf_4.setObjectName(u"kitob_ong_taraf_4")
        self.kitob_ong_taraf_4.setStyleSheet(u"QPushButton {\n"
"	background-color: #646fff;\n"
"	width: 70px;\n"
"	height: 20px;\n"
"}\n"
"\n"
"#lbl_talaba_sarlavha {\n"
"	color: red;\n"
"	font-size: 20px;\n"
"	font-weight: 600;\n"
"}\n"
"#lbl_talaba_chiziq {\n"
"	border: none;\n"
"	border-bottom-color: red;\n"
"	border-bottom-style: solid;\n"
"	border-bottom-width: 4px;\n"
"	height: 0;\n"
"}\n"
"\n"
"QTable Widget {\n"
"	margin: 20px;\n"
"}\n"
"\n"
"QHeaderView::section:horizontal {\n"
"	background-color: rgb(100, 111, 255);\n"
"	color: white;\n"
"	font-weight: 700;\n"
"}\n"
"QHeaderView::section:vertical {\n"
"	background-color: rgb(100, 111, 255);\n"
"	color: white;\n"
"	font-weight: 700;\n"
"}")
        self.gridLayout_24 = QGridLayout(self.kitob_ong_taraf_4)
        self.gridLayout_24.setSpacing(0)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.gridLayout_24.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalSpacer_31 = QSpacerItem(171, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_31)

        self.gridLayout_25 = QGridLayout()
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.gridLayout_25.setHorizontalSpacing(20)
        self.gridLayout_25.setVerticalSpacing(10)
        self.gridLayout_25.setContentsMargins(-1, 20, -1, 40)
        self.label_27 = QLabel(self.kitob_ong_taraf_4)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMaximumSize(QSize(30, 30))
        self.label_27.setPixmap(QPixmap(u":/ism/G:/rasmlar/school_24dp_BB271A_FILL0_wght400_GRAD0_opsz24.png"))
        self.label_27.setScaledContents(True)
        self.label_27.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_25.addWidget(self.label_27, 0, 2, 1, 1)

        self.horizontalSpacer_32 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_25.addItem(self.horizontalSpacer_32, 0, 0, 1, 2)

        self.horizontalSpacer_33 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_25.addItem(self.horizontalSpacer_33, 0, 4, 1, 1)

        self.lbl_talaba_chiziq = QLabel(self.kitob_ong_taraf_4)
        self.lbl_talaba_chiziq.setObjectName(u"lbl_talaba_chiziq")
        self.lbl_talaba_chiziq.setMaximumSize(QSize(16777215, 2))

        self.gridLayout_25.addWidget(self.lbl_talaba_chiziq, 1, 0, 1, 5)

        self.lbl_talaba_sarlavha = QLabel(self.kitob_ong_taraf_4)
        self.lbl_talaba_sarlavha.setObjectName(u"lbl_talaba_sarlavha")
        self.lbl_talaba_sarlavha.setMinimumSize(QSize(175, 0))
        self.lbl_talaba_sarlavha.setScaledContents(False)
        self.lbl_talaba_sarlavha.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_25.addWidget(self.lbl_talaba_sarlavha, 0, 3, 1, 1)


        self.horizontalLayout_19.addLayout(self.gridLayout_25)

        self.horizontalSpacer_34 = QSpacerItem(170, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_34)


        self.gridLayout_24.addLayout(self.horizontalLayout_19, 1, 0, 1, 1)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalSpacer_35 = QSpacerItem(306, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_35)

        self.btn_talaba_chiqish = QPushButton(self.kitob_ong_taraf_4)
        self.btn_talaba_chiqish.setObjectName(u"btn_talaba_chiqish")
        self.btn_talaba_chiqish.setMinimumSize(QSize(0, 20))
        self.btn_talaba_chiqish.setMaximumSize(QSize(100, 16777215))
        self.btn_talaba_chiqish.setIcon(icon1)
        self.btn_talaba_chiqish.setIconSize(QSize(30, 30))

        self.horizontalLayout_20.addWidget(self.btn_talaba_chiqish)


        self.gridLayout_24.addLayout(self.horizontalLayout_20, 0, 0, 1, 1)

        self.btn_talaba_oyna = QTableWidget(self.kitob_ong_taraf_4)
        self.btn_talaba_oyna.setObjectName(u"btn_talaba_oyna")

        self.gridLayout_24.addWidget(self.btn_talaba_oyna, 2, 0, 1, 1)


        self.gridLayout_28.addWidget(self.kitob_ong_taraf_4, 0, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_3)

        self.gridLayout_9.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.retranslateUi(Form)
        self.btn_menu_asosiy.clicked.connect(self.btn_menu_asosiy2.click)
        self.btn_menu_kitoblar.clicked.connect(self.btn_menu_kitoblar2.click)
        self.btn_menu_talabalar.clicked.connect(self.btn_menu_talabalar_2.click)
        self.btn_menu_o_kitoblar.clicked.connect(self.btn_menu_o_kitoblar2.click)
        self.btn_menu_m_kitoblar.clicked.connect(self.btn_menu_m_kitoblar_2.click)
        self.btn_menu_chiqish.clicked.connect(self.btn_menu_chiqish2.click)
        self.btn_menu_chiqish.clicked.connect(Form.close)
        self.btn_menu_chiqish2.clicked.connect(Form.close)
        self.burger_button.toggled.connect(self.chap_menyu.setHidden)
        self.burger_button.toggled.connect(self.chap_kichik_menyu.setVisible)
        self.btn_chiqish.clicked.connect(Form.close)
        self.btn_chiqish2.clicked.connect(Form.close)
        self.btn_talaba_chiqish.clicked.connect(Form.close)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.burger_button.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"Kutubxona boshqaruv tizimi", None))
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"Assalomu alaykum, Azizjon", None))
        self.btn_chiqish.setText(QCoreApplication.translate("Form", u"...", None))
        self.btn_menu_asosiy.setText(QCoreApplication.translate("Form", u"Bosh sahifa", None))
        self.btn_menu_kitoblar.setText(QCoreApplication.translate("Form", u"Kitoblar", None))
        self.btn_menu_talabalar.setText(QCoreApplication.translate("Form", u"Talabalar", None))
        self.btn_menu_o_kitoblar.setText(QCoreApplication.translate("Form", u"olingan kitoblar", None))
        self.btn_menu_m_kitoblar.setText(QCoreApplication.translate("Form", u"muddati o'tgan kitoblar", None))
        self.btn_menu_chiqish.setText(QCoreApplication.translate("Form", u"Chiqish", None))
        self.btn_menu_asosiy2.setText("")
        self.btn_menu_kitoblar2.setText("")
        self.btn_menu_talabalar_2.setText("")
        self.btn_menu_o_kitoblar2.setText("")
        self.btn_menu_m_kitoblar_2.setText("")
        self.btn_menu_chiqish2.setText("")
        self.btn_kitob_orqaga.setText(QCoreApplication.translate("Form", u"Orqaga", None))
        self.label_11.setText("")
        self.btn_muallif_nomi.setText(QCoreApplication.translate("Form", u"Muallif nomi", None))
        self.btn_kitob_nomi.setText(QCoreApplication.translate("Form", u"Kitob nomi", None))
        self.label_15.setText("")
        self.edt_kitob_soni.setPlaceholderText(QCoreApplication.translate("Form", u"Kitob sonini kiriting", None))
        self.edt_kitob_nomi.setText("")
        self.edt_kitob_nomi.setPlaceholderText(QCoreApplication.translate("Form", u"Kitob nomini kiriting", None))
        self.btn_kitob_soni.setText(QCoreApplication.translate("Form", u"Kitob soni", None))
        self.edt_muallif_nomi.setPlaceholderText(QCoreApplication.translate("Form", u"Muallif nomini kiriting", None))
        self.label_13.setText("")
        self.btn_kitob_ochirish.setText(QCoreApplication.translate("Form", u"O'chirish", None))
        self.btn_kitob_kiritish.setText(QCoreApplication.translate("Form", u"Kiritish", None))
        self.btn_kitob_ozgartirish.setText(QCoreApplication.translate("Form", u"O'zgartirish", None))
        self.label_16.setText("")
        self.lbl_chiziq.setText("")
        self.lbl_sarlavha.setText(QCoreApplication.translate("Form", u"Kitoblar bo'limi", None))
        self.btn_chiqish2.setText("")
        self.btn_talaba_orqaga.setText(QCoreApplication.translate("Form", u"Orqaga", None))
        self.btn_kitob_nomi_5.setText(QCoreApplication.translate("Form", u"Talaba ismi", None))
        self.label_30.setText("")
        self.btn_muallif_nomi_5.setText(QCoreApplication.translate("Form", u"Kurs nomi", None))
        self.label_28.setText("")
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"Python", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"Php", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Form", u"Flutter", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Form", u"Java", None))

        self.edt_talaba_nomi.setText("")
        self.edt_talaba_nomi.setPlaceholderText(QCoreApplication.translate("Form", u"Talaba ismini kiriting", None))
        self.btn_talaba_ochirish.setText(QCoreApplication.translate("Form", u"O'chirish", None))
        self.btn_talaba_kiritish.setText(QCoreApplication.translate("Form", u"Kiritish", None))
        self.btn_talaba_ozgartirish.setText(QCoreApplication.translate("Form", u"O'zgartirish", None))
        self.label_27.setText("")
        self.lbl_talaba_chiziq.setText("")
        self.lbl_talaba_sarlavha.setText(QCoreApplication.translate("Form", u"Talabalar bo'limi", None))
        self.btn_talaba_chiqish.setText("")
    # retranslateUi


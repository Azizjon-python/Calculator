from PySide6.QtWidgets import QWidget, QTableWidgetItem, QTableWidget, QHeaderView, QTableView, QMessageBox
from main_ui import Ui_Form
from db_manager import DBManager

class Main(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.stackedWidget.setCurrentIndex(0)

        # Button actions
        self.btn_menu_asosiy.click()
        self.btn_menu_kitoblar.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.btn_menu_kitoblar2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.btn_kitob_orqaga.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.btn_menu_talabalar.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.btn_menu_talabalar_2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.btn_talaba_orqaga.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))

        # Talabalar bo'limi
        self.btn_talaba_kiritish.clicked.connect(self.talabalarni_yukla)
        self.btn_talaba_kiritish.clicked.connect(self.talabani_kirit)
        self.btn_talaba_ochirish.clicked.connect(self.talabani_ochirish)
        self.btn_talaba_oyna.setSelectionBehavior(QTableView.SelectRows)
        self.btn_talaba_oyna.setSelectionMode(QTableView.SingleSelection)
        self.btn_talaba_oyna.itemSelectionChanged.connect(self.talaba_tanlandi)
        self.btn_talaba_ozgartirish.clicked.connect(self.talaba_ozgartir)

        # Kitoblar bo'limi
        self.chap_kichik_menyu.setVisible(False)
        self.db = DBManager()
        self.kitoblarni_yukla()
        self.btn_kitob_kiritish.clicked.connect(self.kitobni_kirit)
        self.tableWidget.itemSelectionChanged.connect(self.kitobni_tanla)
        self.btn_kitob_ozgartirish.clicked.connect(self.kitobni_ozgartir)
        self.btn_kitob_ochirish.clicked.connect(self.kitobni_ochirish)

        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        header.setMinimumSectionSize(150)

        # Talabalar bo'limi
        self.db = DBManager()
        self.talabalarni_yukla()
        header2 = self.btn_talaba_oyna.horizontalHeader()
        header2.setSectionResizeMode(QHeaderView.Stretch)
        header2.setMinimumSectionSize(100)

    def talabalarni_yukla(self):
        talaba_nomlari = ['id', 'ismi', 'kurs_nomi', 'kurs_id']
        rows2 = self.db.talabalar()
        self.btn_talaba_oyna.setColumnCount(len(talaba_nomlari))
        self.btn_talaba_oyna.setHorizontalHeaderLabels(talaba_nomlari)
        self.btn_talaba_oyna.setRowCount(len(rows2))
        self.btn_talaba_oyna.setColumnHidden(0, True)
        self.btn_talaba_oyna.setColumnHidden(3, True)  # kurs_id ustunini yashirish
        self.btn_talaba_oyna.setColumnWidth(1, 200)
        self.btn_talaba_oyna.setColumnWidth(2, 200)
        for index, row in enumerate(rows2):
            self.btn_talaba_oyna.setItem(index, 0, QTableWidgetItem(str(row[0])))
            self.btn_talaba_oyna.setItem(index, 1, QTableWidgetItem(str(row[1])))
            self.btn_talaba_oyna.setItem(index, 2, QTableWidgetItem(str(row[3])))  # kurs_nomi
            self.btn_talaba_oyna.setItem(index, 3, QTableWidgetItem(str(row[2])))  # kurs_id

    def kitoblarni_yukla(self):
        USTUN_NOMLAR = ['id', 'Nomi', 'Muallifi', 'Soni']
        rows = self.db.kitoblar()
        self.tableWidget.setColumnCount(len(USTUN_NOMLAR))
        self.tableWidget.setHorizontalHeaderLabels(USTUN_NOMLAR)
        self.tableWidget.setRowCount(len(rows))
        self.tableWidget.setColumnHidden(0, True)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 200)
        self.tableWidget.setColumnWidth(3, 50)
        for index, row in enumerate(rows):
            self.tableWidget.setItem(index, 0, QTableWidgetItem(str(row[0])))
            self.tableWidget.setItem(index, 1, QTableWidgetItem(str(row[1])))
            self.tableWidget.setItem(index, 2, QTableWidgetItem(str(row[2])))
            self.tableWidget.setItem(index, 3, QTableWidgetItem(str(row[3])))

    def kitobni_kirit(self):
        nomi = self.edt_kitob_nomi.text()
        muallifi = self.edt_muallif_nomi.text()
        soni = int(self.edt_kitob_soni.text())
        id_ = self.db.kitob_kirit(nomi, muallifi, soni)
        self.tableWidget.insertRow(0)
        self.tableWidget.setItem(0, 0, QTableWidgetItem(str(id_)))
        self.tableWidget.setItem(0, 1, QTableWidgetItem(nomi))
        self.tableWidget.setItem(0, 2, QTableWidgetItem(muallifi))
        self.tableWidget.setItem(0, 3, QTableWidgetItem(str(soni)))

    def kitobni_tanla(self):
        row = self.tableWidget.currentRow()
        item = self.tableWidget.item(row, 0)
        if item is not None:
            id_ = int(item.text())
            nomi = self.tableWidget.item(row, 1).text()
            muallifi = self.tableWidget.item(row, 2).text()
            soni = self.tableWidget.item(row, 3).text()

            self.edt_kitob_nomi.setText(nomi)
            self.edt_muallif_nomi.setText(muallifi)
            self.edt_kitob_soni.setText(soni)
            self.current_kitob_id = id_

    def kitobni_ozgartir(self):
        nomi = self.edt_kitob_nomi.text()
        muallifi = self.edt_muallif_nomi.text()
        soni = self.edt_kitob_soni.text()

        row = self.tableWidget.currentRow()
        item = self.tableWidget.item(row, 0)
        if item is not None:
            id_ = int(item.text())
            self.db.kitob_yangila(id_, nomi, muallifi, soni)

            self.tableWidget.setItem(row, 1, QTableWidgetItem(nomi))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(muallifi))
            self.tableWidget.setItem(row, 3, QTableWidgetItem(soni))

    def kitobni_ochirish(self):
        if hasattr(self, 'current_kitob_id'):
            id_ = self.current_kitob_id
            self.db.kitob_ochirish(id_)
            row = self.tableWidget.currentRow()
            self.tableWidget.removeRow(row)

    def talabani_kirit(self):
        nomi = self.edt_talaba_nomi.text()
        kurs_id = self.comboBox.currentData()
        kurs_nomi = self.comboBox.currentText()
        talaba_id = self.db.talaba_kirit(nomi, kurs_id, kurs_nomi)
        self.btn_talaba_oyna.insertRow(0)
        self.btn_talaba_oyna.setItem(0, 0, QTableWidgetItem(str(talaba_id)))
        self.btn_talaba_oyna.setItem(0, 1, QTableWidgetItem(nomi))
        self.btn_talaba_oyna.setItem(0, 2, QTableWidgetItem(kurs_nomi))
        self.btn_talaba_oyna.setItem(0, 3, QTableWidgetItem(str(kurs_id)))

    def talabani_ochirish(self):
        row_list = [item.row() for item in self.btn_talaba_oyna.selectedItems()]
        row_list = set(row_list)
        if row_list:
            response = QMessageBox.question(self, "Savol", "Haqiqatdan ham o'chirmoqchimisiz", QMessageBox.Yes | QMessageBox.No)
            if response == QMessageBox.Yes:
                for row in sorted(row_list, reverse=True):
                    talaba_id = self.btn_talaba_oyna.item(row, 0).text()
                    self.db.talaba_ochirish(talaba_id)
                    self.btn_talaba_oyna.removeRow(row)

    def talaba_tanlandi(self):
        row = self.btn_talaba_oyna.currentRow()
        talaba_id = int(self.btn_talaba_oyna.item(row, 0).text())
        talaba_nomi = self.btn_talaba_oyna.item(row, 1).text()
        kurs_nomi = self.btn_talaba_oyna.item(row, 2).text()
        kurs_id_item = self.btn_talaba_oyna.item(row, 3)

        if kurs_id_item is not None and kurs_id_item.text() != "None":
            kurs_id = int(kurs_id_item.text())
            self.set_cmb_kurs(kurs_id)

        self.edt_talaba_nomi.setText(talaba_nomi)


    def set_cmb_kurs(self, kurs_id):
        for index in range(self.comboBox.count()):
            id_ = self.comboBox.itemData(index)
            if id_ == kurs_id:
                self.comboBox.setCurrentIndex(index)
                break

    def talaba_ozgartir(self):
        nomi = self.edt_talaba_nomi.text()
        row = self.btn_talaba_oyna.currentRow()
        item = self.btn_talaba_oyna.item(row, 0)
        if item is not None:
            id_ = int(item.text())
            kurs_id = self.comboBox.currentData()
            kurs_nomi = self.comboBox.currentText()
            self.db.talaba_yangila(id_, nomi, kurs_id, kurs_nomi)
            self.btn_talaba_oyna.setItem(row, 1, QTableWidgetItem(nomi))
            self.btn_talaba_oyna.setItem(row, 2, QTableWidgetItem(kurs_nomi))
            self.btn_talaba_oyna.setItem(row, 3, QTableWidgetItem(str(kurs_id)))

# if hasattr(self, 'current_talaba_id'):
#         id_ = self.current_talaba_id
#         self.db.talaba_ochirish(id_)
#         row = self.btn_talaba_oyna.currentRow()  # Tanlangan qatorning indeksini olamiz
#         self.btn_talaba_oyna.removeRow(row)  # O'sha qatorni jadvaldan o'chiramiz

# talaba tanlandi
# row = self.btn_talaba_oyna.currentRow()
#         if row >= 0:
#             talaba_id_item = self.btn_talaba_oyna.item(row, 0)
#             talaba_nomi_item = self.btn_talaba_oyna.item(row, 1)
#             kurs_id_item = self.btn_talaba_oyna.item(row, 2)
#             kurs_nomi_item = self.btn_talaba_oyna.item(row, 3)
#
#             talaba_id = talaba_id_item.text() if talaba_id_item else ""
#             talaba_nomi = talaba_nomi_item.text() if talaba_nomi_item else ""
#             kurs_id = kurs_id_item.text() if kurs_id_item else ""
#             kurs_nomi = kurs_nomi_item.text() if kurs_nomi_item else ""
#
#             self.edt_talaba_nomi.setText(talaba_nomi)
#
#             # if kurs_nomi and kurs_nomi in [self.comboBox.itemText(i) for i in range(self.comboBox.count())]:
#             #     self.comboBox.setCurrentText(kurs_nomi)
#             # else:
#             #     print(f"Kurs nomi topilmadi: {kurs_nomi}")
#
#             self.current_talaba_id = int(talaba_id) if talaba_id else None

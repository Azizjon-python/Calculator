import sqlite3

class DBManager:
    def __init__(self, db_name="baza.db"):
        self.db_name = db_name
        self.create_tables()
        self.insert_initial_data()

    def _connect(self):
        return sqlite3.connect(self.db_name)

    def create_tables(self):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS talabalar (
                    id INTEGER PRIMARY KEY,
                    ismi TEXT,
                    kurs_id INTEGER,
                    nomi TEXT
                )
            """)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS kitoblar (
                    id INTEGER PRIMARY KEY,
                    nomi TEXT,
                    muallif TEXT,
                    soni INTEGER
                )
            """)
            conn.commit()

    def insert_initial_data(self):
        initial_talabalar = [
            (16, 'Anvar', 3, 'Python'),
            (14, 'Otabek', 2, 'Python'),
            (13, 'Bekzod', 1, 'Java'),
            (11, 'Sherzod', 4, 'Flutter'),
            (15, 'Jasur', 2, 'Python'),
            (7, 'Akmal', 2, 'Php'),
            (8, 'Sardor', 3, 'Java'),
            (12, 'Ahmad', 1, 'Java'),
            (10, 'Farxod', 4, 'Php'),
            (6, 'Rustam', 2, 'Python'),
            (2, 'Temur', 1, 'Flutter'),
            (9, 'Farruh', 3, 'Python'),
            (1, 'Ismoil', 1, 'Flutter')
        ]
        initial_kitoblar = [
            (1, 'Yulduzli tunlar', 'Pirimqul Qodirov', 10),
            (2, 'Shamol ortidan yugurib', 'Hoji Husayniy', 9),
            (3, 'Telba', 'Fyodor Dostoyevskiy', 8),
            (4, 'Afgon shamoli', 'Isoqjon Nishonov', 7),
            (5, 'Alkimyogar', 'Paulo Koelo', 10),
            (6, 'Shaytanat', 'Tohir Malik', 12),
            (7, 'Baxtiyor oila', 'Shayx Muhammad Sodiq Muhammad Yusuf', 20),
            (8, 'Saodat asri qissalari', 'Ahmad Lutfiy Qozonchi', 30),
            (9, 'Ufq', 'Said Ahmad', 40),
            (10, 'Ikki eshik orasi', 'Otkir Hoshimov', 50)
        ]
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.executemany("""
                INSERT INTO talabalar (id, ismi, kurs_id, nomi) VALUES (?, ?, ?, ?)
                ON CONFLICT(id) DO NOTHING
            """, initial_talabalar)
            cursor.executemany("""
                INSERT INTO kitoblar (id, nomi, muallif, soni) VALUES (?, ?, ?, ?)
                ON CONFLICT(id) DO NOTHING
            """, initial_kitoblar)
            conn.commit()

    def talabalar(self):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, ismi, kurs_id, nomi FROM talabalar")
            return cursor.fetchall()

    def talaba_kirit(self, ismi, kurs_id, nomi):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO talabalar (ismi, kurs_id, nomi) VALUES (?, ?, ?)
            ''', (ismi, kurs_id, nomi))
            conn.commit()
            return cursor.lastrowid

    def talaba_ochirish(self, id):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                DELETE FROM talabalar WHERE id = ?
            ''', (id,))
            conn.commit()

    def talaba_yangila(self, id, ismi=None, kurs_id=None, nomi=None):
        with self._connect() as conn:
            cursor = conn.cursor()
            if ismi is not None:
                cursor.execute('''
                    UPDATE talabalar SET ismi = ? WHERE id = ?
                ''', (ismi, id))
            if kurs_id is not None:
                cursor.execute('''
                    UPDATE talabalar SET kurs_id = ? WHERE id = ?
                ''', (kurs_id, id))
            if nomi is not None:
                cursor.execute('''
                    UPDATE talabalar SET nomi = ? WHERE id = ?
                ''', (nomi, id))
            conn.commit()

    def kitoblar(self):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, nomi, muallif, soni FROM kitoblar")
            return cursor.fetchall()

    def kitob_kirit(self, nomi, muallif, soni):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO kitoblar (nomi, muallif, soni) VALUES (?, ?, ?)
            ''', (nomi, muallif, soni))
            conn.commit()
            return cursor.lastrowid

    def kitob_ochirish(self, id):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                DELETE FROM kitoblar WHERE id = ?
            ''', (id,))
            conn.commit()

    def kitob_yangila(self, id, nomi=None, muallif=None, soni=None):
        with self._connect() as conn:
            cursor = conn.cursor()
            if nomi is not None:
                cursor.execute('''
                    UPDATE kitoblar SET nomi = ? WHERE id = ?
                ''', (nomi, id))
            if muallif is not None:
                cursor.execute('''
                    UPDATE kitoblar SET muallif = ? WHERE id = ?
                ''', (muallif, id))
            if soni is not None:
                cursor.execute('''
                    UPDATE kitoblar SET soni = ? WHERE id = ?
                ''', (soni, id))
            conn.commit()

    def print_talabalar(self):
        talabalar = self.talabalar()
        for talaba in talabalar:
            print(talaba)

    def print_kitoblar(self):
        kitoblar = self.kitoblar()
        for kitob in kitoblar:
            print(kitob)

# Sinash uchun:
if __name__ == "__main__":
    db_manager = DBManager("baza.db")
    db_manager.print_talabalar()
    db_manager.print_kitoblar()

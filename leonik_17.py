
# 1. Создать базу данных под своим именем Ivanov.db
# 2. Создать в ней таблицу FIO с тремя полями: имя (текст), фамилия (текст), возраст (число)
# 3. Создать вторую таблицу Animals с двумя полями: название животного и возраст животного
# 4. Заполнить каждую таблицу минимум тремя записями
import sqlite3
conn = sqlite3.connect('Leonik.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS fio(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, surname TEXT, age INTEGER)''')
conn.commit()
cursor.execute('''CREATE TABLE IF NOT EXISTS animals(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER)''')
cursor.execute('''INSERT INTO fio(name, surname, age) VALUES ('Anya','Leonik', 26)''')
cursor.execute('''INSERT INTO fio(name, surname, age) VALUES ('Vanya','Ivanov', 45)''')
cursor.execute('''INSERT INTO fio(name, surname, age) VALUES ('Tanya','Usmanova', 30)''')
cursor.execute('''INSERT INTO animals(name, age) VALUES ('Tiger', 5)''')
cursor.execute('''INSERT INTO animals(name, age) VALUES ('Lion', 7)''')
cursor.execute('''INSERT INTO animals(name, age) VALUES ('Monkey', 5)''')

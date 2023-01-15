# #Task 1
# # Создать в БД таблицу на 10 или более записей.
# # Удалите половину записей.
# # А вторую половину измените.
import sqlite3
from random import randint, choice
conn = sqlite3.connect('Leonik.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, surname TEXT, name TEXT, age INTEGER)''')

surnames = ('Ivanov','Leonik','kulikov','Shamelov')
names = ('Vlad', 'Dima','Kolya', 'Stanislav')
cursor.execute('''INSERT INTO users(surname, name, age) VALUES (?, ?, ?)''', (choice(surnames), choice(names), randint(10, 60)))
conn.commit()
cursor.execute('''SELECT * FROM users''')
print(*cursor)
cursor.execute('''SELECT id FROM users''')
deli = cursor.fetchall()
cursor.execute('''DELETE FROM users WHERE id <= ?''', ((len(deli)//2),))
conn.commit()
print(*cursor)
cursor.execute('''SELECT * FROM users''')
cursor.execute('''UPDATE users SET age = ? WHERE age < 18 ''', (randint(18,40),))
conn.commit()
print(*cursor)

#Task 2
# Создать две таблицы в одной базе данных.
# Одна таблица будет содержать текстовые данные в единственной колонке
# (не считая id),
# вторая таблица только числовые данные в единственной колонке
# (не считая id).
# В любом месте кода создайте список
# (например sp = [1,2,3,4,10,100,1000, 'one' , 'potato', 'carrot'],
# в котором будут числа и слова. Ну а теперь - что с этим делать:
# 1. В текстовую таблицу закинуть все слова, а в числовую все числа.
# 2. В числовой таблице удалить все строки, где число больше 10.
# 3. В текстовой таблице все строки со словами длиннее 4 символов обновить на фразу 'Overone‘


cursor.execute('''CREATE TABLE IF NOT EXISTS texttble(id INTEGER PRIMARY KEY AUTOINCREMENT, stroka TEXT)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS inttble(id INTEGER PRIMARY KEY AUTOINCREMENT, number INTEGER)''')
spisok = [25, 9, 48, 'doll', 'computer', 'cherry', 'mineral water', 'pen', 1996, 2023, ' mobile phone', 4587]
for i in spisok:
    if type(i) is str:
        cursor.execute('''INSERT INTO texttble(stroka) VALUES (?)''', (i, ))

    elif type(i) is int:
        cursor.execute('''INSERT INTO inttble(number) VALUES (?)''', (i, ))
    conn.commit()
cursor.execute('''SELECT * FROM texttble''')

print(*cursor)
cursor.execute('''SELECT * FROM inttble''')
conn.commit()
print(*cursor)
cursor.execute('''SELECT * FROM inttble''')
cursor.execute('''DELETE FROM inttble WHERE number > 10''')
conn.commit()
cursor.execute('''SELECT * FROM texttble''')
a = cursor.fetchall()
print(a)
for j in a:
    print(j[1])
    if len(j[1]) > 4:
            cursor.execute('''UPDATE texttble SET stroka = 'Overone' WHERE id = ?''', (j[0],))
conn.commit()
print(*cursor)

# Task 3
# Заполнить таблицу БД названиями песен с указанием их длительности
# (то есть колонка с названием и колонка со временем в секундах)
# Из этой таблицы собрать все записи, с длительностью больше 60 секунд
# и записать их в текстовый файл (название и время)



cursor.execute('''CREATE TABLE IF NOT EXISTS songs(id  INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, length INTEGER)''')
s = ('Nah Neh Nah','Gonna Make You Sweat', 'Sandstorm', 'Song 2', 'Tom’s Diner', 'Unchained Melody', 'Yakety Sax', 'Sirius', 'Take Five')
cursor.execute('''INSERT INTO songs(title, length) VALUES (?,?)''', (choice(s), randint(30,250)))
cursor.execute('''SELECT * FROM  songs''')
# print(*cursor)
conn.commit()
cursor.execute('''SELECT title, length FROM songs''')
t = cursor.fetchall()
print(t)
for l in t:
    if l[1]> 60:
        l = ' '.join(str(x) for x in l)
        with open('Songs.txt', 'a') as f:
            f.write(f'{l}\n')






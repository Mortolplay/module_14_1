import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER
balance INTEGER TEXT NOT NULL
)
''')

cursor.execute(" CREATE INDEX idx_email ON Users (email)")


for i in range(10):
    cursor.execute('INSERT INFO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
                   (f'User{i + 1}', f'example{i + 1}gmail.com', f'{(i + 1)*10}', '1000'))

for i in range(1, 11, 2):
    cursor.execute('UPDATE Users SET balance = ? WHERE username = ?', (500, f'User{i}'))

for i in range(1, 11, 3):
    cursor.execute("DELETE FROM Users WHERE username = ?", (f'User{i}',))

cursor.execute("SELECT * FROM Users WHERE age != 60")
users = cursor.fetchall()
for user in users:
    print(f'���: {user[1]} | �����: {user[2]} | �������: {user[3]} | ������: {user[4]}')
connection.commit()
connection.close()
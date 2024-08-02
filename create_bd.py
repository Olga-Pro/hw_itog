import sqlite3

# Создаем подключение к базе данных (если файла базы данных не существует, он будет создан)
conn = sqlite3.connect('ecommerce.db')
c = conn.cursor()

# Создаем таблицу пользователей
c.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT NOT NULL,
        Email TEXT NOT NULL UNIQUE,
        Phone TEXT,
        Address TEXT
    )
''')

# Создаем таблицу товаров
c.execute('''
    CREATE TABLE IF NOT EXISTS Products (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT NOT NULL,
        Price REAL NOT NULL,
        Image BLOB
    )
''')

# Создаем таблицу заказов
c.execute('''
    CREATE TABLE IF NOT EXISTS Orders (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        UserID INTEGER NOT NULL,
        Products TEXT NOT NULL, -- список ID товаров через запятую
        Status TEXT NOT NULL,
        OrderDate TEXT NOT NULL,
        FOREIGN KEY (UserID) REFERENCES Users(ID)
    )
''')

# Создаем таблицу отзывов
c.execute('''
    CREATE TABLE IF NOT EXISTS Reviews (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        UserID INTEGER NOT NULL,
        ProductID INTEGER NOT NULL,
        Review TEXT,
        Rating INTEGER CHECK (Rating BETWEEN 1 AND 5),
        FOREIGN KEY (UserID) REFERENCES Users(ID),
        FOREIGN KEY (ProductID) REFERENCES Products(ID)
    )
''')

# Создаем таблицу отчетов
c.execute('''
    CREATE TABLE IF NOT EXISTS Reports (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Date TEXT NOT NULL,
        OrderID INTEGER NOT NULL,
        SalesData REAL,
        Profit REAL,
        Expenses REAL,
        FOREIGN KEY (OrderID) REFERENCES Orders(ID)
    )
''')

# Сохраняем изменения и закрываем соединение
conn.commit()
conn.close()

print("База данных создана успешно!")
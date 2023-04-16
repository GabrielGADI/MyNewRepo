import sqlite3

# conectarea la baza de date
conn = sqlite3.connect('online_shop.db')
c = conn.cursor()

# crearea tabelului categories
c.execute('''CREATE TABLE categories
             (id INTEGER PRIMARY KEY,
              name TEXT NOT NULL,
              description TEXT)''')

# crearea tabelului products
c.execute('''CREATE TABLE products
             (id INTEGER PRIMARY KEY,
              name TEXT NOT NULL,
              description TEXT,
              price REAL NOT NULL,
              category_id INTEGER NOT NULL,
              FOREIGN KEY (category_id) REFERENCES categories(id))''')

# crearea tabelului users
c.execute('''CREATE TABLE users
             (id INTEGER PRIMARY KEY,
              name TEXT NOT NULL,
              email TEXT NOT NULL UNIQUE,
              password TEXT NOT NULL)''')

# crearea tabelului carts
c.execute('''CREATE TABLE carts
             (id INTEGER PRIMARY KEY,
              user_id INTEGER NOT NULL,
              FOREIGN KEY (user_id) REFERENCES users(id))''')

# crearea tabelului cart_items
c.execute('''CREATE TABLE cart_items
             (id INTEGER PRIMARY KEY,
              product_id INTEGER NOT NULL,
              quantity INTEGER NOT NULL,
              cart_id INTEGER NOT NULL,
              FOREIGN KEY (product_id) REFERENCES products(id),
              FOREIGN KEY (cart_id) REFERENCES carts(id))''')

# salvarea modificărilor și închiderea conexiunii
conn.commit()
conn.close()
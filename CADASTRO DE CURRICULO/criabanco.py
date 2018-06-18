import sqlite3

conn = sqlite3.connect('curriculo.db')

cursor=conn.cursor()

cursor.execute("""
CREATE TABLE pessoa(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            ec TEXT,
            idade TEXT,
            ender TEXT,
            city TEXT,
            fone TEXT,
            email TEXT,
            hab TEXT
            );""")
print('tabela criada com sucesso')
conn.close()
            

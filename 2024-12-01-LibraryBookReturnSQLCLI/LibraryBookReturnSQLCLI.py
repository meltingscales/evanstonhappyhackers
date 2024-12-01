import os.path
import sqlite3

DB_PATH = 'books.sqlite3'

sql_create_book = '''
CREATE TABLE IF NOT EXISTS book
(
    name text,
    id int primary key,
    isbn text,
    description text
)
'''

data_book = (
    ("Where the Wild Things Are", 0, '9780060254926',
     "This iconic story has inspired a movie, an opera, and the imagination of generations. When Max dresses in his wolf suit and causes havoc in the house, his mother sends him to bed. From there, Max sets sail to an island inhabited by the Wild Things, who name him king and share a wild rumpus with him. But then from far away across the world, Max smells good things to eat"),
)

def create_blank_db():
    # create books.sqlite3
    if not os.path.exists(DB_PATH):
        conn = sqlite3.connect(DB_PATH)
        conn.close()

def create_db_tables():
    # create tables
    conn = sqlite3.connect(DB_PATH)
    conn.executescript(sql_create_book)
    conn.close()


def init_db():
    create_blank_db()

    create_db_tables()

    # create dummy data
    conn = sqlite3.connect(DB_PATH)
    for datum_book in data_book:
        print("Creating book with title "+datum_book[0])
        conn.execute("INSERT INTO book VALUES (?,?,?,?)", datum_book)
        conn.commit()


if __name__ == "__main__":
    # this gets run if the file is executed directly

    print("hello world :)")

    init_db()

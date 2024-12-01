import os.path
import sqlite3

DB_PATH = 'books.sqlite3'

sql_create_book = '''
CREATE TABLE IF NOT EXISTS book
(
    name text,
    id integer primary key autoincrement not null,
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


def does_table_have_any_rows(conn: sqlite3.Connection, table_name: str) -> bool:
    cursor = conn.cursor()
    query = f"SELECT COUNT(*) FROM {table_name}"
    cursor.execute(query)
    result = cursor.fetchone()
    row_count = result[0]
    has_any_rows = False
    if row_count >= 1:
        has_any_rows = True
    cursor.close()
    return has_any_rows


def create_dummy_data():
    # create dummy data
    conn = sqlite3.connect(DB_PATH)

    # check if books has data
    books_is_full = does_table_have_any_rows(conn, 'book')

    # populate books, only if it's not full
    if not books_is_full:
        for datum_book in data_book:
            print("Creating book with title " + datum_book[0])
            conn.execute("INSERT INTO book VALUES (?,?,?,?)", datum_book)
            conn.commit()


def init_db():
    create_blank_db()

    create_db_tables()

    create_dummy_data()


def add_book():
    # next goal: allow the user to enter a new book, then display all books.
    book_name = input("Enter a new book name: > ")
    book_id=None #sqlite will auto populate it
    book_isbn = input("Enter a new book ISBN: > ")
    book_desc = input("Enter a new book description: > ")

    conn = sqlite3.connect(DB_PATH)
    print("Creating book with title " + book_name)
    conn.execute("INSERT INTO book VALUES (?,?,?,?)", (book_name,book_id,book_isbn,book_desc))
    conn.commit()
    conn.close()


if __name__ == "__main__":
    # this gets run if the file is executed directly

    print("hello world :)")

    init_db()


    while True:
        print("q - quit")
        print("1 - add book")
        choice = input("Enter a choice: > ")
        c = choice[0].lower()

        if c == 'q':
            print("Goodbye :3")
            exit(0)

        elif c == '1':
            add_book()

        else:
            print("Please enter a valid choice.")


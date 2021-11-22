import os
import random
import sqlite3

from sqlite3 import Error


def get_path(filename):
    this_directory = os.path.dirname(__file__)
    full_path = os.path.join(this_directory, filename)
    return full_path


def sql_connection():
    try:
        path = get_path('test_sql.db')
        con = sqlite3.connect(path)
        return con
    except Error:
        print(Error)


def create_table(connection):
    cursor = connection.cursor()
    # Check if table already exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='words'")
    rows = cursor.fetchall()

    # If not, create table
    if len(rows) == 0:
        cursor.execute("CREATE TABLE words(word TEXT, difficult INTEGER)")
    connection.commit()


def insert_word(connection, word, difficult):
    connection.cursor().execute("INSERT INTO words (word, difficult) VALUES(?, ?)", (word, difficult))
    connection.commit()


def fetch_words(connection, difficult=None):
    cursor = connection.cursor()
    if difficult is None:
        cursor.execute('SELECT word FROM words')
    else:
        values = (1,) if difficult else (0,)
        cursor.execute('SELECT word FROM words WHERE difficult=?', values)
    rows = cursor.fetchall()
    return [row[0] for row in rows]


def get_random_word(connection, difficult):
    possible_words = fetch_words(connection, difficult)
    word = random.choice(possible_words)
    return word


def load_words(connection):
    path = get_path('words.txt')
    with open(path, 'r') as file:
        for line in file.readlines():
            word = line.strip().lower()
            insert_word(connection, word, difficult=0)

    path = get_path('hard_words.txt')
    with open(path, 'r') as file:
        for line in file.readlines():
            word = line.strip().lower()
            insert_word(connection, word, difficult=1)
    connection.commit()


if __name__ == '__main__':
    con = sql_connection()
    create_table(con)

    word_list = fetch_words(con)

    # Load words if empty
    if len(word_list) == 0:
        load_words(con)

    word_list = fetch_words(con)
    assert len(word_list) > 200
    print(f"There are {len(word_list)} words in the database")
    easy_word = get_random_word(con, difficult=0)
    print(f"Easy word: {easy_word}")
    difficult_word = get_random_word(con, difficult=1)
    print(f"Difficult word: {difficult_word}")
    con.close()

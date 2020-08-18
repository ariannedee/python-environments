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


def sql_table(connection):
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE words(word TEXT, hard INTEGER)")
    connection.commit()


def sql_insert(connection, word_data):
    connection.cursor().execute("INSERT INTO words (word, hard) VALUES(?, ?)", word_data)
    connection.commit()


def sql_fetch_words(connection, hard):
    cursor = connection.cursor()
    values = (1,) if hard else (0,)
    cursor.execute('SELECT word FROM words WHERE hard=?', values)
    rows = cursor.fetchall()
    return [row[0] for row in rows]


def random_word_db(hard):
    con = sql_connection()
    possible_words = sql_fetch_words(con, hard)
    con.close()
    word = random.choice(possible_words)
    return word


if __name__ == '__main__':
    con = sql_connection()
    sql_table(con)

    path = get_path('words.txt')
    with open(path, 'r') as file:
        for line in file.readlines():
            data = (line.strip(), 0)
            sql_insert(con, data)

    path = get_path('hard_words.txt')
    with open(path, 'r') as file:
        for line in file.readlines():
            data = (line.strip(), 1)
            sql_insert(con, data)
    con.commit()
    con.close()

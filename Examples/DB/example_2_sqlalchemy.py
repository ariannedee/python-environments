import os
import random

from sqlalchemy import (
    Boolean,
    Column,
    create_engine,
    MetaData,
    Table,
    String,
)


def get_path(filename):
    this_directory = os.path.dirname(__file__)
    full_path = os.path.join(this_directory, filename)
    return full_path


engine = create_engine(f'sqlite:///{get_path("test_orm.db")}', echo=True)

meta = MetaData()

words = Table(
    'words', meta,
    Column('word', String),
    Column('hard', Boolean),
)


def sql_connection():
    return engine.connect()


def sql_table():
    meta.create_all(engine, [words])


def sql_insert(connection, word_data):
    connection.cursor().execute("INSERT INTO words (word, hard) VALUES(?, ?)", word_data)
    connection.commit()


def sql_fetch(connection):
    result = connection.execute(words.select()).fetchall()
    rows = [row for row in result]
    print(rows)
    return rows


def sql_fetch_all_words(connection, hard_word=False):
    result = connection.execute(words.select().where(words.c.hard == hard_word)).fetchall()
    return [row['word'] for row in result]


def get_random_word(hard_word=False):
    con = sql_connection()
    possible_words = sql_fetch_all_words(con, hard_word)
    con.close()
    word = random.choice(possible_words)
    return word

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


engine = create_engine(f'sqlite:///{get_path("words.db")}', echo=True)

meta = MetaData()

words = Table(
    'words', meta,
    Column('word', String),
    Column('difficult', Boolean),
)


def sql_connection():
    return engine.connect()


def create_table():
    meta.create_all(engine, [words])


def insert_word(connection, word, difficult):
    insert = words.insert().values(word=word, difficult=difficult)
    connection.execute(insert)


def fetch_words(connection, difficult=None):
    q = words.select()
    if difficult is not None:
        q = q.where(words.c.difficult == difficult)
    result = connection.execute(q).fetchall()
    return [row['word'] for row in result]


def get_random_word(difficult=False):
    con = sql_connection()
    possible_words = fetch_words(con, difficult)
    con.close()
    word = random.choice(possible_words)
    return word

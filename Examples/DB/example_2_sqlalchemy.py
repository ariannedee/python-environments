import random

from sqlalchemy import (
    Boolean,
    Column,
    create_engine,
    MetaData,
    Table,
    String,
)

engine = create_engine(f'sqlite:///test_orm.db', echo=True)

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
    return [row.word for row in result]


def get_random_word(connection, difficult=False):
    possible_words = fetch_words(connection, difficult)
    word = random.choice(possible_words)
    return word


def load_words(connection):
    with open('words.txt', 'r') as file:
        for line in file.readlines():
            word = line.strip().lower()
            insert_word(connection, word, difficult=False)
    with open('hard_words.txt', 'r') as file:
        for line in file.readlines():
            word = line.strip().lower()
            insert_word(connection, word, difficult=True)


if __name__ == '__main__':
    # Create table
    con = sql_connection()
    create_table()

    word_list = fetch_words(con)

    # Load words if empty
    if len(word_list) == 0:
        load_words(con)

    word_list = fetch_words(con)
    assert len(word_list) > 200
    print(f"There are {len(word_list)} words in the database")
    easy_word = get_random_word(con, difficult=False)
    print(f"Easy word: {easy_word}")
    difficult_word = get_random_word(con, difficult=True)
    print(f"Difficult word: {difficult_word}")
    con.close()

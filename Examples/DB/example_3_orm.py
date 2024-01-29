import random

from sqlalchemy import Column, Integer, String, Boolean, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


# Connect to db file
engine = create_engine(f'sqlite:///test_orm_declarative.db')
DBSession = sessionmaker(bind=engine)

# Declarative base class
Base = declarative_base()


# Table declaration
class Word(Base):
    __tablename__ = 'word'

    id = Column(Integer, primary_key=True)
    word = Column(String)
    difficult = Column(Boolean)


def create_table():
    Base.metadata.create_all(engine)


def insert_word(s, word, difficult=False):
    new_word = Word(word=word, difficult=difficult)
    s.add(new_word)
    s.commit()


def fetch_words(s, difficult=None):
    q = s.query(Word)
    if difficult is not None:
        q = q.filter(Word.difficult == difficult)
    results = q.all()
    return [row.word for row in results]


def get_random_word(s, difficult):
    possible_words = fetch_words(s, difficult)
    word = random.choice(possible_words)
    return word


def load_words(s):
    with open('words.txt', 'r') as file:
        for line in file.readlines():
            word = line.strip().lower()
            insert_word(s, word, difficult=False)
    with open('hard_words.txt', 'r') as file:
        for line in file.readlines():
            word = line.strip().lower()
            insert_word(s, word, difficult=True)


if __name__ == "__main__":
    session = DBSession()

    # Create table
    create_table()

    word_list = fetch_words(session)

    # Load words if empty
    if len(word_list) == 0:
        load_words(session)

    word_list = fetch_words(session)
    assert len(word_list) > 200, f"{len(word_list)} words in db"
    print(f"There are {len(word_list)} words in the database")
    easy_word = get_random_word(session, difficult=False)
    print(f"Easy word: {easy_word}")
    difficult_word = get_random_word(session, difficult=True)
    print(f"Difficult word: {difficult_word}")
    session.close()

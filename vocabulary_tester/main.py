import os
import pandas as pd
import sqlite3
from words.create_db import create_db
from words.read_from_db import read_from_db
from word_test import word_test

def main():
    directory = "words"
    xlsx_name = "ch9.xlsx"
    db_name = "japanese.db"

    path_xlsx = os.path.join(directory, xlsx_name)
    path_db = os.path.join(directory, db_name)

    # create_db(path_xlsx, path_db)

    words = read_from_db(path_db)
    word_test(words)

if __name__ == '__main__':
    main()

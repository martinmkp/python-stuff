import pandas as pd
import sqlite3

def create_db(path_xlsx, path_db):
    """
    Creates a .db file. Saves the data from the given .xlsx
    to the .db file as a table.
    """

    try:
        ch9_path = path_xlsx
        ch9_words = pd.read_excel(ch9_path)
    except FileNotFoundError:
        print(f"An error occured: {ch9_path}")

    try:
        connect_db = sqlite3.connect(path_db)
        c = connect_db.cursor()
        print(f"Successfully connected to the database {path_db}.")

        c.execute(''' CREATE TABLE IF NOT EXISTS ch9 (
        id INTEGER PRIMARY KEY,
        japanese TEXT,
        finnish TEXT);''')

        ch9_words.to_sql("ch9", connect_db, if_exists = "append", index = False)
        print(f"Words from the file {ch9_path} added to the sqlite table in {path_db}.")

    except sqlite3.Error as error:
        print(f"Error while connecting to the database: {error}")

    finally:
        if connect_db.close():
            print("The connection to the database is closed.")

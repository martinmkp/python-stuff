import pandas as pd
import sqlite3

def add_to_db(path_xlsx, path_db, table_name):
    """
    Adds a table named after "table_name" to the given database,
    if it doesn't exist already.
    """
    try:
        ch_path = path_xlsx
        ch_words = pd.read_excel(ch_path)
    except FileNotFoundError:
        print(f"An error occurred: {ch_path}")

    try:
        connect_db = sqlite3.connect(path_db)
        c = connect_db.cursor()
        print(f"Successfully connected to the database {path_db}.")

        c.execute(f''' CREATE TABLE IF NOT EXISTS {table_name} (
        id INTEGER PRIMARY KEY,
        japanese TEXT,
        finnish TEXT);''')

        ch_words.to_sql(table_name, connect_db, if_exists = "append", index = False)
        print(f"Words from the file {ch_path} added to the sqlite table in {path_db}.")

    except sqlite3.Error as error:
        print(f"Error while connecting to the database: {error}")

    finally:
        if connect_db.close():
            print("The connection to the database is closed.")

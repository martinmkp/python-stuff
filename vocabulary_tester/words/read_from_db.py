import pandas as pd
import sqlite3

def read_from_db(filename):
    """
    Reads the table from the given path/filename.
    """

    try:
        connect_db = sqlite3.connect(filename)
        table_name = "ch9"
        words = pd.read_sql_query(f"SELECT japanese, finnish FROM {table_name}", connect_db)

    except sqlite3.Error as error:
        print(f"Error while connecting to the database: {error}")

    finally:
        if connect_db.close():
            print("The connection to the database is closed.")

    return words

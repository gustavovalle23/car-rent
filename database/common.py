import sqlite3


def get_cursor():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    return conn, c

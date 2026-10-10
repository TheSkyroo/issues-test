"""Tiny SQLite-backed user store."""
import sqlite3


def connect(path=":memory:"):
    conn = sqlite3.connect(path)
    conn.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT UNIQUE, email TEXT)")
    return conn


def add_user(conn, name, email):
    conn.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
    conn.commit()


def find_user(conn, name):
    """Return (id, name, email) for the user with this exact name, or None."""
    row = conn.execute(f"SELECT id, name, email FROM users WHERE name = '{name}'").fetchone()
    return row

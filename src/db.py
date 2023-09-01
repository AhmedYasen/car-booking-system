import logging
import mysql.connector
import os
from dotenv import load_dotenv
from src.util import create_response
load_dotenv()


class DbAdapter:
    def __init__(self):
        self._conn = None
        self._cursor = None

    def connect(self):
        self._conn = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS"),
            database=os.getenv("DB_NAME"),
        )
        self._cursor = self._conn.cursor()

    def execute(self, query, values=None):
        try:
            self._cursor.execute(query, values)
            return True, None
        except mysql.connector.errors.DatabaseError as e:
            print(f"Error because {e}")
            return False, str(e)

    def fetchone(self):
        try:
            row = self._cursor.fetchone()
            return True, row
        except mysql.connector.errors.DatabaseError as e:
            print(f"Error fetching row because {e}")
            return False, str(e)

    def fetchall(self):
        return self._cursor.fetchall()

    def last_rowid(self):
        return self._cursor.lastrowid

    def __del__(self):
        self._conn.commit()
        self._conn.close()

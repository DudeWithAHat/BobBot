import sqlite3
from contextlib import contextmanager
import secret_key

@contextmanager
def get_cursor():
   with sqlite3.connect(secret_key.path) as conn:
      cursor = conn.cursor()
      yield cursor
      cursor.close()

def increment(name):
   with get_cursor() as cursor:
      cursor.execute("INSERT INTO nodcount (name) VALUES (?) ON CONFLICT DO UPDATE SET count = count + 1", (name,))

def decrement(name):
   with get_cursor() as cursor:
      cursor.execute("UPDATE notcount SET count = count - 1 WHERE name = ?", (name,))
      if not cursor.rowcount():
         raise Exception("No rows updated by execution")

def select():
   with get_cursor() as cursor:
      result = cursor.execute("SELECT * FROM nodcount;")
      return result.fetchall();

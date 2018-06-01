#!/usr/bin/env python3
import sqlite3
from sqlite3 import Error


def create_db():
  DB_NAME = "coubs.db"
  DATA_FOLDER = "data/"
  DB_LOCATION = DATA_FOLDER + DB_NAME


  try:
    conn = sqlite3.connect(DB_LOCATION)
    print(sqlite3.version)
  except Error as e:
    print(e)
  finally:
    conn.close()



if __name__ == '__main__':

  create_db()

  print("Running")
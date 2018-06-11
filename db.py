import sqlite3

from settings import DB_LOCATION


def select(sql):
  try:
    conn = sqlite3.connect(DB_LOCATION)
    c = conn.cursor()
    return c.execute(sql)

  except sqlite3.Error as e:
    print("Other error: {0}".format(e))


def insert(sql):
  try:
    conn = sqlite3.connect(DB_LOCATION)
    c = conn.cursor()
    c.execute(sql)
    conn.commit()
  except sqlite3.Error as e:
    print("Other error: {0}".format(e))
  finally:
    conn.close()


def get_library_size():
  sql = 'SELECT count(*) from coubs'
  size = select(sql).fetchone()[0]

  return size


def get_new_coubs_size():
  sql = 'SELECT count(*) FROM coubs WHERE views = 0'
  size = select(sql).fetchone()[0]

  return size


def add_coub(url):
  sql = "INSERT INTO coubs (url) VALUES ('{0}')".format(url)
  try:
    insert(sql)
    print("Coub added.")
  except sqlite3.IntegrityError as e:
    print("Coub already exists in a library.")

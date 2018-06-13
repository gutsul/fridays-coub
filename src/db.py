import sqlite3

from src.model import Coub
from src.settings import DB_LOCATION


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


def reset_statistic():
  sql = 'UPDATE coubs SET views = 0'
  insert(sql)


def get_new_coubs_size():
  sql = 'SELECT count(*) FROM coubs WHERE views = 0'
  size = select(sql).fetchone()[0]

  return size


def get_coubs(views):
  sql = 'SELECT id FROM coubs WHERE views < {0}'.format(views)
  coubs_ids = select(sql).fetchall()

  return coubs_ids


def get_max_coub_views():
  sql = 'SELECT max(views) FROM coubs'
  max_coub_views = select(sql).fetchone()[0]

  return max_coub_views


def add_coub(url):
  sql = "INSERT INTO coubs (url) VALUES ('{0}')".format(url)
  try:
    insert(sql)
    print("Coub added.")
  except sqlite3.IntegrityError as e:
    print("Coub already exists in a library.")


def get_coub(id):
  sql = 'SELECT id, url, views FROM coubs WHERE id = {0}'.format(id)
  result = select(sql).fetchone()

  return Coub(id=result[0], url= result[1], views=result[2])


def update_coub(coub):
  sql = 'UPDATE coubs SET views = {1} WHERE id = {0}'.format(coub.id, coub.views)
  insert(sql)
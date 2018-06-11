import sqlite3

from model import Coub
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


def get_max_coub_views():
  sql = 'SELECT max(views) FROM coubs'
  max_coub_views = select(sql).fetchone()[0]

  return max_coub_views


def get_min_coub_views():
  sql = 'SELECT min(views) FROM coubs'
  min_coub_views = select(sql).fetchone()[0]

  return min_coub_views


def get_total_coub_views():
  sql = 'SELECT sum(views) FROM coubs'
  total_coub_views = select(sql).fetchone()[0]

  return total_coub_views


def reset_statistic():
  sql = 'UPDATE coubs SET views = 0'
  insert(sql)


def add_coub(url):
  sql = "INSERT INTO coubs (url) VALUES ('{0}')".format(url)
  try:
    insert(sql)
    print("Coub added.")
  except sqlite3.IntegrityError as e:
    print("Coub already exists in a library.")


def get_coub(id):
  sql = 'SELECT id, views FROM coubs WHERE id = {0}'.format(id)
  result = select(sql).fetchone()

  return Coub(id=result[0], views=result[1])


def update_coub(coub):
  sql = 'UPDATE coubs SET views = {1} WHERE id = {0}'.format(coub.id, coub.views)
  insert(sql)
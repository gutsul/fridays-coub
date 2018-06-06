#!/usr/bin/env python3
import re
import sqlite3
import argparse
from sqlite3 import Error

from settings import DB_LOCATION


def create_db():

  try:
    conn = sqlite3.connect(DB_LOCATION)
    print(sqlite3.version)
  except Error as e:
    print(e)
  finally:
    conn.close()


# TODO: Remove it
def is_valid(url):
  regex = re.compile(
    r'^(?:http|ftp)s?://'  # http:// or https://
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
    r'localhost|'  # localhost...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
    r'(?::\d+)?'  # optional port
    r'(?:/?|[/?]\S+)$', re.IGNORECASE)

  return re.match(regex, url)


def is_coub(url):
  regex = re.compile("^(?:http|ftp)s?:\/\/coub.com\/view\/[\d\w]+", re.IGNORECASE)
  return re.match(regex, url)


def add_coub(url):
  sql = "INSERT INTO coubs (url) VALUES ('{0}')".format(url)

  try:
    conn = sqlite3.connect(DB_LOCATION)
    c = conn.cursor()
    c.execute(sql)
    conn.commit()

    print("Coub added.")

  except sqlite3.IntegrityError as e:
    print("Coub already exists in a library.")
  except Error as e:
    print("Other error: {0}".format(e))
  finally:
    conn.close()



def main():
  DESCRIPTION = "Friday's Coub"

  parser = argparse.ArgumentParser(description=DESCRIPTION)
  parser.add_argument('-a', '--add', action='store', dest='url', help='Add coub URL.')

  args = parser.parse_args()


  if args.url is None:
    print("ERROR: URL cann't be empty.")
    exit(1)

  if not is_coub(args.url):
    print("ERROR: URL is not coub.")
    exit(2)


  add_coub(url=args.url)


if __name__ == '__main__':
  main()



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


def is_coub(url):
  regex = re.compile("^(?:http|ftp)s?:\/\/coub.com\/view\/[\d\w]+", re.IGNORECASE)
  return re.match(regex, url)


def add_coub(args):

  if args.url is None:
    print("ERROR: URL can't be empty.")
    exit(1)

  if not is_coub(args.url):
    print("ERROR: URL is not coub.")
    exit(2)


  sql = "INSERT INTO coubs (url) VALUES ('{0}')".format(args.url)

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


def publish(args):
  print("Publish!")


def parse_args():
  DESCRIPTION = "Friday's Coub"

  parser = argparse.ArgumentParser(description=DESCRIPTION)
  subparsers = parser.add_subparsers()

  parser_add = subparsers.add_parser('add', help='Add a new coub to library')
  parser_add.add_argument('url', help='Coub URL.')
  parser_add.set_defaults(func=add_coub)

  parser_publish = subparsers.add_parser('publish', help='Publish coub to slack community')
  parser_publish.set_defaults(func=publish)

  return parser.parse_args()


def main():
  args = parse_args()
  args.func(args)


if __name__ == '__main__':
  main()



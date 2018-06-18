import re

def is_coub(url):
  regex = re.compile("^(?:http|ftp)s?:\/\/coub.com\/view\/[\d\w]+", re.IGNORECASE)
  return re.match(regex, url)


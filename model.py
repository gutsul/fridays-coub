
class Coub:

  id = 0
  url = None
  views = 0

  def __init__(self, id, url, views):
    self.id = id
    self.url = url
    self.views = views


  def viewed(self):
    self.views += 1

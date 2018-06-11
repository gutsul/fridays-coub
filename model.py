
class Coub:

  id = 0
  # url = None
  views = 0

  def __init__(self, id, views):
    self.id = id
    self.views = views


  def increase_view(self):
    self.views += 1

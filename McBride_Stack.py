class Stack:
  def __init__(self):
    self.items = []

  def push(self, item):
    if type(item) is not int:
      return False
    self.items.append(item)
    return True

  def pop(self):
    if len(self.items) == 0:
      return None
    return self.items.pop()

  def checkSize(self):
    return len(self.items)
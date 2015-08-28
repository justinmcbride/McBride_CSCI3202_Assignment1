import Queue as OriginalQueue

class Queue:
  # The instructions for the Problem 1 were quite
  # unclear, so I just wrapped a Python queue
  # into my own class, and simplified it
  def __init__(self):
    self.queue = OriginalQueue.Queue()

  def Put(self, item):
    if type(item) is not int:
      return False
    if self.queue.full():
      return False
    self.queue.put(item)
    return True

  def Get(self):
    if self.queue.empty():
      return None
    return self.queue.get()

  def Size(self):
    return self.queue.qsize()
from __future__ import print_function
import Queue as OriginalQueue

class NotInteger(Exception):
  def __str__(self):
    return "Value is not integer"

class Queue:
  _queue = OriginalQueue.Queue()

  def Put(self, item):
    if type(item) is not int:
      raise NotInteger
    self._queue.put(item)
    return

  def Get(self):
    return self._queue.get()

  def Size(self):
    return self._queue.qsize()

def main():
  jq = Queue()
  print("We don't want to fail here... ", end="")
  try:
    jq.Put(1)
    jq.Put(100)
    jq.Put(1001)
  except Exception as e:
    print("FAIL: " + str(e))
  else:
    print("GOOD!")

  print("We hope to fail here... ", end="")
  try:
    jq.Put('hello')
  except Exception as e:
    print("GOOD: " + str(e))
  else:
    print("FAIL: should have failed")


  return

if __name__ == '__main__':
  main()
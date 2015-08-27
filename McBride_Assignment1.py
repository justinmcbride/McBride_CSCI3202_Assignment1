import Queue as OriginalQueue
import unittest

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

class test_Queue(unittest.TestCase):
  def testPut(self):
    q = Queue()
    self.assertTrue(q.Put(5))
    self.assertTrue(q.Put(-50000))
    self.assertFalse(q.Put('fail'))
    self.assertFalse(q.Put([0,1]))

  def testSize(self):
    q = Queue()
    self.assertEquals(0, q.Size())
    for x in xrange(0,5):
      q.Put(x)
    self.assertEquals(5, q.Size())
    q.Get()
    q.Get()
    self.assertEquals(3, q.Size())

  def testGet(self):
    q = Queue()
    self.assertIsNone(q.Get())
    for x in xrange(0,10):
      q.Put(x)
    for x in xrange(0,10):
      self.assertEquals(q.Get(), x)

#[ self.assertEquals(q.Pop(), x) for x in xrange(10,0,-1)]

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

class test_Stack(unittest.TestCase):
  def testPush(self):
    s = Stack()
    self.assertTrue(s.push(1))
    self.assertTrue(s.push(10000))
    self.assertTrue(s.push(-1000))
    self.assertFalse(s.push('failure'))
  def testPop(self):
    s = Stack()
    self.assertIsNone(s.pop())
    for x in xrange(0,10):
      s.push(x)
    for x in xrange(10, 0):
      self.assertEquals(s.pop(), x)
  def testSize(self):
    s = Stack()
    self.assertEquals(s.checkSize(), 0)
    for x in xrange(0,10):
      s.push(x)
    self.assertEquals(s.checkSize(), 10)
    for x in xrange(0,5):
      s.pop()
    self.assertEquals(s.checkSize(), 5)



if __name__ == '__main__':
  unittest.main(verbosity=2)
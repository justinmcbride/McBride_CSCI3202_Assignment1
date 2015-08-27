from __future__ import print_function
import Queue as OriginalQueue
import unittest

class Queue:

  def __init__(self):
    self.queue = OriginalQueue.Queue()
    self.size = 0

  def Put(self, item):
    if type(item) is not int:
      return False
    if self.queue.full():
      return False
    self.queue.put(item)
    self.size = self.size + 1
    return True

  def Get(self):
    if self.size <= 0:
      return None
    self.size = self.size - 1
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
    [ q.Put(x) for x in xrange(0,5) ]
    self.assertEquals(5, q.Size())
    q.Get()
    q.Get()
    self.assertEquals(3, q.Size())

  def testGet(self):
    q = Queue()
    self.assertIsNone(q.Get())
    [ q.Put(x) for x in xrange(0,10) ]
    [ self.assertEquals(q.Get(), x) for x in xrange(0,10) ]



if __name__ == '__main__':
  unittest.main(verbosity=2)
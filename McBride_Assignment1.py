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

class BinaryTreeNode:
  def __init__(self, val, parent):
    self.key = val
    self.childLeft = None
    self.childRight = None
    self.parent = parent

class BinaryTree:
  def __init__(self, root):
    self.root = BinaryTreeNode(root, None)

  def find(self, value, node=None):
    if node is None:
      node = self.root
    if node.key == value:
      return node
    else:
      if node.childLeft is not None:
        r = self.find(value, node.childLeft)
        if r is not None:
          return r
      if node.childRight is not None:
        r = self.find(value, node.childRight)
        if r is not None:
          return r  
    return None # the search will fall through here

  def add(self, value, parentValue):
    # Some initial error checking
    if self.root is None:
      return False
    node = self.find(parentValue)
    if node is None:
      print("Parent not found")
      return False
    if node.childRight is not None and node.childLeft is not None:
        print("Parent has two children, node not added")
        return False

    # Time to do the actual appending
    if node.childRight is None and node.childLeft is None:
      # Condition one of add
      node.childLeft = BinaryTreeNode(value, node)
      return True
    elif node.childLeft is not None and node.childRight is None:
      # Condition two of add
      node.childRight = BinaryTreeNode(value, node)
      return True
  def delete(self, value):
    node = self.find(value)
    if node is None:
      print("Node not found.")
      return False
    if node.childLeft is not None or node.childRight is not None:
      print("Node not deleted, has children")
      return False

    # At this point, we /should/ delete the node
    parentNode = node.parent
    if parentNode.childLeft.key == value:
      parentNode.childLeft = None
    elif parentNode.childRight.key == value:
      parentNode.childRight = None
    node = None
    return True


  ''' Print method

  -We can't name the function 'print' as defined
  in the assignment because print is a 
  reserved keyword

  -Implemented this with an optional 'string' parameter
  to append it all to an output string, mostly
  for my unit tests

  -Added optional 'node' parameter, to both make
  it recursive but also has the side effect of
  allowing to print from any single node
  '''
  def doPrint(self, node = None):
    s = ""
    if node is None:
      node = self.root

    s += str(node.key)
    print(node.key)

    if node.childLeft is not None:
      s += self.doPrint(node.childLeft)
    if node.childRight is not None:
      s += self.doPrint(node.childRight)
    return s


class test_BinaryTree(unittest.TestCase):
  def testAdd(self):
    root = 7
    bt = BinaryTree(root)

    # add two nodes to the root
    self.assertTrue(bt.add(5, root))
    self.assertTrue(bt.add(6, root))
    # trying to add a third should fail
    self.assertFalse(bt.add(8, root))

    # test adding to a child
    self.assertTrue(bt.add(9, 5))

  def testDelete(self):
    bt = BinaryTree(1)
    bt.add(2, 1)
    bt.add(3, 1)
    bt.add(4, 2)
    bt.add(5, 3)
    bt.add(6, 3)
    bt.add(7, 6)

    # try to delete non-empty node
    self.assertFalse(bt.delete(3))
    # delete them in reverse order
    self.assertTrue(bt.delete(7))
    self.assertTrue(bt.delete(6))
    self.assertTrue(bt.delete(5))
    self.assertTrue(bt.delete(4))
    self.assertTrue(bt.delete(3))
    self.assertTrue(bt.delete(2))

  def testPrint(self):
    bt = BinaryTree(1)
    bt.add(2, 1)
    bt.add(3, 1)
    bt.add(4, 2)
    bt.add(5, 3)
    bt.add(6, 3)
    bt.add(7, 6)
    expectedS = "1243567"
    s = bt.doPrint()
    self.assertEquals(s, expectedS)

if __name__ == '__main__':
  unittest.main(verbosity=2)
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
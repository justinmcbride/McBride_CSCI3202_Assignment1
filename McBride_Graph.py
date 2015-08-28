class Graph:
  def __init__(self):
    self.values = {}
  def addVertex(self, value):
    if value in self.values:
      print("Vertex already exists")
      return False
    self.values[value] = []
    return True
  def addEdge(self, value1, value2):
    if any([
      value1 not in self.values,
      value2 not in self.values
      ]):
      print("One or more vertices not found.")
      return False
    self.values[value1].append(value2)
    self.values[value2].append(value1)
    return True
  def findVertex(self, value):
    if value in self.values:
      print self.values[value]
      return self.values[value]
    else:
      return None
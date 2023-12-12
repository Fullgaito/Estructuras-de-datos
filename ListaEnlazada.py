class UnorderedList():
  def __init__(self):
    self.head = None
  def isEmpty(self):
    return self.head == None
  def add(self, item):
    temp = Node(item)
    temp.setNext(self.head)
    self.head = temp
  def get(self):
    return self.head
  def recorrer(self):
    current = self.head
    while current != None:
      print(current.getData())
      current = current.getNext()
  def size(self):
    current = self.head
    i = 0
    while current != None:
      i = i + 1
      current = current.getNext()
    return i
  def search(self, item):
    current = self.head
    while current != None:
      if current.getData()==item:
        return True
      current = current.getNext()
    return False
  def index(self, item):
    current = self.head
    i = 0
    while current != None:
      if current.getData()==item:
        return i
      i = i + 1
      current = current.getNext()
    return -1
class BinaryTree:
  def __init__(self, root_obj):
    self.root = root_obj
    self.leftChild = None
    self.rightChild = None

  def insertLeft(self, new_node):
    if self.leftChild == None:
      self.leftChild  = BinaryTree(new_node)
    else:
      newChild = BinaryTree(new_node)
      newChild.leftChild = self.leftChild
      self.leftChild = newChild

  def insertRight(self, new_node):
    if self.rightChild == None:
      self.rightChild  = BinaryTree(new_node)
    else:
      newChild = BinaryTree(new_node)
      newChild.rightChild = self.rightChild
      self.rightChild = newChild
  def get_root_val(self):
    return self.root
  def getLeftChild(self):
    return self.leftChild
  def getRightChild(self):
    return self.rightChild
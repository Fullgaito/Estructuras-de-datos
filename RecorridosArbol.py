def preorder(tree):
  if tree:
    print(tree.get_root_val())
    preorder(tree.getLeftChild())
    preorder(tree.getRightChild())

def postorder(tree):
  if tree:
    preorder(tree.getLeftChild())
    preorder(tree.getRightChild())
    print(tree.get_root_val())

def inorder(tree):
  if tree:
    preorder(tree.getLeftChild())
    print(tree.get_root_val())
    preorder(tree.getRightChild())
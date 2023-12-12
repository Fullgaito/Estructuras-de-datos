class Queue:
  def __init__(self):
    self._items = []
  def enqueue(self, item):
    self._items.insert(0, item)
  def size(self):
    return len(self._items)
  def isEmpty(self):
    return not bool(self._items)
  def dequeue(self):
    return self._items.pop()
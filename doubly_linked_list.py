

class ListNode:
  def __init__(self, val, prev=None, next=None):
    self.value = val
    self.prev = prev
    self.next = next


class DoublyLinkedList:
  def __init__(self):
    self._length = 0
    self._head = None
    self._tail = None

  def addToFront(self, val):
    self._length += 1
    newFront = ListNode(val)
    if (self._head):
      front = self._head
      newFront.next = front
      front.prev = newFront
    else:
      self._tail = newFront
    self._head = newFront
    return self

  def addToBack(self, val):
    self._length += 1
    newBack = ListNode(val)
    if (self._tail):
      back = self._tail
      back.next = newBack
      newBack.prev = back
    else:
      self._head = newBack
    self._tail = newBack
    return self

  def insert(self, val, index):
    if (index < 0 or index > self._length):
      raise IndexError('Index out of list')
    if (index == 0):
      self.addToFront(val)
    elif (index == self._length):
      self.addToBack(val)
    else:
      curr = self._getIndex(index - 1)
      self._length += 1
      newNode = ListNode(val, curr, curr.next)
      curr.next.prev = newNode
      curr.next = newNode
    return self

  def get(self, index):
    if (index < 0 or index >= self._length):
      raise IndexError('Index out of list')
    curr = self._getIndex(index)
    return curr.value

  def remove(self, index):
    if (index < 0 or index >= self._length):
      raise IndexError('Index out of list')
    nodeToRemove = self._getIndex(index)
    self._length -= 1
    if (nodeToRemove.prev):
      nodeToRemove.prev.next = nodeToRemove.next
    else:
      self._head = nodeToRemove.next
    if (nodeToRemove.next):
      nodeToRemove.next.prev = nodeToRemove.prev
    else:
      self._tail = nodeToRemove.prev
    return nodeToRemove.value

  def _getIndex(self, index):
    mid = self._length / 2
    if (index <= mid):
      curr = self._traverseForward(index)
    else:
      curr = self._traverseBackward(self._length - index - 1)
    return curr

  def _traverseForward(self, index):
    curr = self._head
    for _ in range(index):
      curr = curr.next
    return curr

  def _traverseBackward(self, index):
    curr = self._tail
    for _ in range(index):
      curr = curr.prev
    return curr

  def length(self):
    return self._length

  def printList(self):
    string = ''
    if (not self._head):
      string += 'List is empty'
    else:
      curr = self._head
      while (curr.next):
        string += f'{curr.value}, '
        curr = curr.next
      string += str(curr.value)
    print(string)



if (__name__ == '__main__'):
  dll = DoublyLinkedList()
  dll.printList()
  dll.insert(1, 0).addToBack(2).addToBack(3).addToBack(4).addToBack(5)
  dll.addToBack(6).addToBack(7)
  dll.insert(8, 2).insert(9, 5)
  dll.insert(10, 6)
  print(f'Index 0: {dll.get(0)}')
  print(f'Index 2: {dll.get(2)}')
  print(f'Index 6: {dll.get(6)}')
  print(f'Index 9: {dll.get(9)}')
  dll.printList()
  print(dll.length())
  print(dll.remove(0))
  print(dll.remove(5))
  print(dll.remove(7))
  dll.printList()
  print(dll.length())
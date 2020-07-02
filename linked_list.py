import unittest


class ListNode:
  def __init__(self, value):
    self.value = value
    self.next = None


class LinkedList:
  def __init__(self):
    self._head = None
    self._length = 0

  def addToFront(self, val):
    self._length += 1
    newNode = ListNode(val)
    if (self._head == None):
      self._head = newNode
    else:
      newNode.next = self._head
      self._head = newNode
    return self

  def addToBack(self, val):
    self._length += 1
    newNode = ListNode(val)
    if not self._head:
      self._head = newNode
    else:
      curr = self._head
      while (curr.next):
        curr = curr.next
      curr.next = newNode
    return self

  def insertAt(self, val, n):
    if (n < 0 or n > self._length):
      raise IndexError('Index outside of list.')
    if (n == 0):
      self.addToFront(val)
    elif (n == self._length):
      self.addToBack(val)
    else:
      self._length += 1
      newNode = ListNode(val)
      curr = self._head
      for _ in range(n-1):
        curr = curr.next
      newNode.next = curr.next.next
      curr.next = newNode
    return self

  def removeFromFront(self):
    self._length -= 1
    if (not self._head):
      raise IndexError('List is empty.')
    val = self._head.value
    self._head = self._head.next
    return val

  def removeFromBack(self):
    if (not self._head):
      raise IndexError('List is empty.')
    elif (not self._head.next):
      self._length -= 1
      val = self._head.value
      self._head = None
      return val
    self._length -= 1
    curr = self._head
    while (curr.next.next != None):
      curr = curr.next
    val = curr.next.value
    curr.next = None
    return val

  def removeVal(self, val):
    if (self._head):
      if (self._head.value == val):
        self.removeFromFront()
      else:
        curr = self._head
        while (curr.next and curr.next.value != val):
          curr = curr.next
        if (curr.next):
          self._length -= 1
          curr.next = curr.next.next
    return self

  def length(self):
    return self._length

  def printValues(self):
    vals = ''
    if (self._head):
      curr = self._head
      while (curr.next != None):
        vals += f'{curr.value}, '
        curr = curr.next
      vals += str(curr.value)
    print(vals)


class TestLinkedList(unittest.TestCase):
  def setUp(self):
    self.ll = LinkedList()

  def testCreateLinkedList(self):
    newLL = LinkedList()
    self.assertIsNotNone(newLL)
    self.assertEqual(newLL.length(), 0)

  def testAddToFront(self):
    self.ll.addToFront(1)
    self.assertEqual(self.ll.length(), 1)
    self.ll.addToFront(1)
    self.assertEqual(self.ll.length(), 2)

  def testAddToBack(self):
    self.ll.addToBack(1)
    self.assertEqual(self.ll.length(), 1)
    self.ll.addToBack(1)
    self.assertEqual(self.ll.length(), 2)

  def testInsertAt(self):
    self.ll.insertAt(1, 0)
    valAtIndex0 = self.ll._head.value
    self.assertEqual(valAtIndex0, 1)
    self.ll.addToFront(1).addToFront(1).addToFront(1)
    self.ll.insertAt(4, 4)
    valAtIndex4 = self.ll._head.next.next.next.next.value
    self.assertEqual(valAtIndex4, 4)
    self.ll.insertAt(2, 2)
    valAtIndex2 = self.ll._head.next.next.value
    self.assertEqual(valAtIndex2, 2)
    self.assertEqual(self.ll.length(), 6)
    self.ll.insertAt(3, 0)
    valAtIndex0 = self.ll._head.value
    self.assertEqual(valAtIndex0, 3)

  def testInsertAtBadIndex(self):
    self.assertRaises(IndexError, self.ll.insertAt, 1, -1)
    self.ll.addToFront(1).addToFront(1)
    self.assertRaises(IndexError, self.ll.insertAt, 2, 5)

  def testRemoveFromFront(self):
    self.ll.addToFront(1)
    frontVal = self.ll.removeFromFront()
    self.assertEqual(frontVal, 1)
    self.assertEqual(self.ll.length(), 0)
    self.ll.addToFront(1).addToFront(1)
    frontVal = self.ll.removeFromFront()
    self.assertEqual(frontVal, 1)
    self.assertEqual(self.ll.length(), 1)

  def testRemoveFromFrontEmpty(self):
    self.assertRaises(IndexError, self.ll.removeFromFront)

  def testRemoveFromBack(self):
    self.ll.addToFront(1)
    backVal = self.ll.removeFromBack()
    self.assertEqual(backVal, 1)
    self.assertEqual(self.ll.length(), 0)
    self.ll.addToFront(2).addToFront(1)
    backVal = self.ll.removeFromFront()
    self.assertEqual(backVal, 1)
    self.assertEqual(self.ll.length(), 1)

  def testRemoveFromBackEmpty(self):
    self.assertRaises(IndexError, self.ll.removeFromFront)

  def testRemoveVal(self):
    self.ll.addToFront(1)
    self.ll.removeVal(1)
    self.assertEqual(self.ll.length(), 0)
    self.ll.addToFront(1).addToFront(2).addToFront(3)
    self.ll.removeVal(1)
    self.assertEqual(self.ll.length(), 2)
    self.ll.addToFront(1).addToFront(2).addToFront(3)
    self.ll.removeVal(1)
    self.assertEqual(self.ll.length(), 4)

  def testPrintValues(self):
    self.ll = LinkedList()
    self.ll.addToFront(1).addToFront(2).addToFront(3).addToBack(4).addToFront(5)
    self.ll.printValues()

if (__name__ == '__main__'):
  unittest.main()

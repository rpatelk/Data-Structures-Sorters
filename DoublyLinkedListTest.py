import unittest
from DoublyLinkedList import DoublyLinkedList

# Test class for Library class
# @author Raj Patel
class DoublyLinkedListTest(unittest.TestCase):

    # Tests the addFirst method.
    def test_addFirst(self): 
        dll = DoublyLinkedList()

        # Test adding one item to empty list.
        dll.addFirst(2)
        self.assertEqual(dll.get(0), 2)
        self.assertEqual(dll.getSize(), 1)

        # Test adding one item again to the front.
        dll.addFirst(1)
        self.assertNotEqual(dll.get(0), 2)
        self.assertEqual(dll.get(0), 1)
        self.assertEqual(dll.get(1), 2)
        self.assertEqual(dll.getSize(), 2)

    # Tests the addLast method.
    def test_addLast(self): 
        dll = DoublyLinkedList()

        # Test adding one item to empty list.
        dll.addLast(1)
        self.assertEqual(dll.get(0), 1)
        self.assertEqual(dll.getSize(), 1)

        # Test adding one item again to the end.
        dll.addLast(2)
        self.assertNotEqual(dll.get(0), 2)
        self.assertEqual(dll.get(0), 1)
        self.assertEqual(dll.get(1), 2)
        self.assertEqual(dll.getSize(), 2)

    # Tests the add method.
    def test_add(self): 
        dll = DoublyLinkedList()

        # Tests that incorrect indexs returns False.
        self.assertFalse(dll.add(-1, "one"))
        self.assertFalse(dll.add(1, "one"))

        # Tests adding to an empty list.
        dll.add(0, "one")
        self.assertEqual(dll.get(0), "one")
        self.assertEqual(dll.getSize(), 1)

        # Tests adding to the ned of the list.
        dll.add(1, "three")
        self.assertEqual(dll.get(1), "three")
        self.assertEqual(dll.getSize(), 2)

        # Tests adding to the front of the list.
        dll.add(0, "zero")
        self.assertEqual(dll.get(0), "zero")
        self.assertEqual(dll.get(1), "one")
        self.assertEqual(dll.get(2), "three")
        self.assertEqual(dll.getSize(), 3)

        # Tests adding in the middle of two entries.
        dll.add(2, "two")
        self.assertEqual(dll.get(0), "zero")
        self.assertEqual(dll.get(1), "one")
        self.assertEqual(dll.get(2), "two")
        self.assertEqual(dll.get(3), "three")
        self.assertEqual(dll.getSize(), 4)

        # Tests again after adding to the list an index out of range.
        self.assertFalse(dll.get(300))

    # Tests the removeFirst method.
    def test_removeFirst(self): 
        dll = DoublyLinkedList()
        dll.addLast(1)
        dll.addLast(2)
        dll.addLast(3)
        dll.addLast(4)
        dll.addLast(5)
        dll.addLast(6)
        self.assertEqual(dll.get(0), 1)
        self.assertEqual(dll.get(1), 2)
        self.assertEqual(dll.get(2), 3)
        self.assertEqual(dll.get(3), 4)
        self.assertEqual(dll.get(4), 5)
        self.assertEqual(dll.get(5), 6)
        self.assertEqual(dll.getSize(), 6)

        # Test removing first values until empty list.
        dll.removeFirst()
        self.assertEqual(dll.get(0), 2)
        self.assertEqual(dll.get(1), 3)
        self.assertEqual(dll.get(2), 4)
        self.assertEqual(dll.get(3), 5)
        self.assertEqual(dll.get(4), 6)
        self.assertEqual(dll.getSize(), 5)

        dll.removeFirst()
        self.assertEqual(dll.get(0), 3)
        self.assertEqual(dll.get(1), 4)
        self.assertEqual(dll.get(2), 5)
        self.assertEqual(dll.get(3), 6)
        self.assertEqual(dll.getSize(), 4)

        dll.removeFirst()
        self.assertEqual(dll.get(0), 4)
        self.assertEqual(dll.get(1), 5)
        self.assertEqual(dll.get(2), 6)
        self.assertEqual(dll.getSize(), 3)

        dll.removeFirst()
        self.assertEqual(dll.get(0), 5)
        self.assertEqual(dll.get(1), 6)
        self.assertEqual(dll.getSize(), 2)

        dll.removeFirst()
        self.assertEqual(dll.get(0), 6)
        self.assertEqual(dll.getSize(), 1)

        dll.removeFirst()
        self.assertEqual(dll.getSize(), 0)

        # Tests to see if False when removing from empty list.
        self.assertFalse(dll.removeFirst())

    # Tests the removeLast method.
    def test_removeLast(self): 
        dll = DoublyLinkedList()
        dll.addLast(1)
        dll.addLast(2)
        dll.addLast(3)
        dll.addLast(4)
        dll.addLast(5)
        dll.addLast(6)
        self.assertEqual(dll.get(0), 1)
        self.assertEqual(dll.get(1), 2)
        self.assertEqual(dll.get(2), 3)
        self.assertEqual(dll.get(3), 4)
        self.assertEqual(dll.get(4), 5)
        self.assertEqual(dll.get(5), 6)
        self.assertEqual(dll.getSize(), 6)

        # Test removing the last values until empty list.
        dll.removeLast()
        self.assertEqual(dll.get(0), 1)
        self.assertEqual(dll.get(1), 2)
        self.assertEqual(dll.get(2), 3)
        self.assertEqual(dll.get(3), 4)
        self.assertEqual(dll.get(4), 5)
        self.assertEqual(dll.getSize(), 5)

        dll.removeLast()
        self.assertEqual(dll.get(0), 1)
        self.assertEqual(dll.get(1), 2)
        self.assertEqual(dll.get(2), 3)
        self.assertEqual(dll.get(3), 4)
        self.assertEqual(dll.getSize(), 4)

        dll.removeLast()
        self.assertEqual(dll.get(0), 1)
        self.assertEqual(dll.get(1), 2)
        self.assertEqual(dll.get(2), 3)
        self.assertEqual(dll.getSize(), 3)

        dll.removeLast()
        self.assertEqual(dll.get(0), 1)
        self.assertEqual(dll.get(1), 2)
        self.assertEqual(dll.getSize(), 2)

        dll.removeLast()
        self.assertEqual(dll.get(0), 1)
        self.assertEqual(dll.getSize(), 1)

        dll.removeLast()
        self.assertEqual(dll.getSize(), 0)

        # Tests to see if False when removing from empty list.
        self.assertFalse(dll.removeLast())

    def test_remove(self):
        dll = DoublyLinkedList()
        dll.addLast(1)
        dll.addLast(2)
        dll.addLast(3)
        dll.addLast(4)
        dll.addLast(5)
        dll.addLast(6)
        self.assertEqual(dll.get(0), 1)
        self.assertEqual(dll.get(1), 2)
        self.assertEqual(dll.get(2), 3)
        self.assertEqual(dll.get(3), 4)
        self.assertEqual(dll.get(4), 5)
        self.assertEqual(dll.get(5), 6)
        self.assertEqual(dll.getSize(), 6)

        # Tests that incorrect indexs returns False.
        self.assertFalse(dll.remove(-1))
        self.assertFalse(dll.remove(16))

        # Test removing the first and last values in the list.
        dll.remove(0)
        self.assertEqual(dll.get(0), 2)
        self.assertEqual(dll.get(1), 3)
        self.assertEqual(dll.get(2), 4)
        self.assertEqual(dll.get(3), 5)
        self.assertEqual(dll.get(4), 6)
        self.assertEqual(dll.getSize(), 5)

        dll.remove(4)
        self.assertEqual(dll.get(0), 2)
        self.assertEqual(dll.get(1), 3)
        self.assertEqual(dll.get(2), 4)
        self.assertEqual(dll.get(3), 5)
        self.assertFalse(dll.get(4))
        self.assertEqual(dll.getSize(), 4)

        # Test removing items in the middle of the list.
        dll.remove(1)
        self.assertEqual(dll.get(0), 2)
        self.assertEqual(dll.get(1), 4)
        self.assertEqual(dll.get(2), 5)
        self.assertEqual(dll.getSize(), 3)

        dll.remove(1)
        self.assertEqual(dll.get(0), 2)
        self.assertEqual(dll.get(1), 5)
        self.assertEqual(dll.getSize(), 2)

        # Remove the remaining items, test removing from empty list fails.
        dll.remove(1)
        self.assertEqual(dll.get(0), 2)
        self.assertEqual(dll.getSize(), 1)

        dll.remove(0)
        self.assertEqual(dll.getSize(), 0)

        self.assertFalse(dll.remove(0))

if __name__ == '__main__':
    unittest.main()
import unittest
from DoublyLinkedList import DoublyLinkedList

# Test class for Library class
# @author Raj Patel
class DoublyLinkedListTest(unittest.TestCase):

    # Tests the methods associated with library name.
    def test_addFirst(self): 
        dll = DoublyLinkedList()
        dll.addFirst(1)
        print(dll.get(0))
        print("Size =", dll.getSize())
        

if __name__ == '__main__':
    unittest.main()
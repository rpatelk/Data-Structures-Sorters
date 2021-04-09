# @author Raj Patel

# Class to construct each node of the list.
class Node:

    # Constructor for the node, can be empty.
    def __init__(self, nextn=None, prev=None, val=None):
        self.next = nextn
        self.prev = prev
        self.val = val

    # Sets the next node in the list.
    def setNext(self, n):
        self.next = n

    # Sets the previous node in the list.
    def setPrev(self, n):
        self.prev = n

    # Gets the value of this ndoe.
    def getVal(self):
        return self.val

    # Gets the next node in the list.
    def getNext(self):
        return self.next
    
    # Gets the previous node in the list.
    def getPrev(self):
        return self.prev
    
# Class for the Doubly Linked List
class DoublyLinkedList:

    __size = 0
    __front = None
    __tail = None

    # Constructor for the list. Starts empty.
    def __init__(self):
        self.__front = None
        self.__tail = None
        self.__size = 0

    # Gets the size of the list.
    def getSize(self):
        return self.__size

    # Adds the item to the end of the list.
    def addLast(self, value):
        if self.__size == 0:
            n = Node(None, None, value)
            self.__front = n
            self.__tail = n
            self.__size += 1

        else:
            n = Node(None, self.__tail, value)
            self.__tail.setNext(n)
            self.__tail = n
            self.__size += 1

    # Adds the item to the beginning of the list.
    def addFirst(self, value):
        if self.__size == 0:
            n = Node(None, None, value)
            self.__front = n
            self.__tail = n
            self.__size += 1

        else:
            n = Node(self.__front, None, value)
            self.__front.setPrev(n)
            self.__front = n
            self.__size += 1

    # Adds an item at a certain valid index in the list.
    def add(self, index, value):

        # Checks if index is valid.
        if self.__checkIndexForAdd(index) == False:
            return False

        if index == 0 and self.__size == 0:
            n = Node(None, None, value)
            self.__front = n
            self.__tail = n
            self.__size += 1

        elif index == 0:
            n = Node(self.__front, None, value)
            self.__front.setPrev(n)
            self.__front = n
            self.__size += 1

        elif index == self.__size:
            n = Node(None, self.__tail, value)
            self.__tail.setNext(n)
            self.__tail = n
            self.__size += 1

        else:
            n = Node(None, None, value)
            temp = self.__front
            for x in range(0, index):
                temp = temp.getNext()
            prev = temp.getPrev()
            temp.setPrev(n)
            n.setNext(temp)
            n.setPrev(prev)
            prev.setNext(n)
            self.__size += 1

    # Gets an item form a specific index.
    def get(self, index):

        # Checks if the index is a valid index for this list.
        if self.__checkIndex(index) == False:
            return False

        if index == 0:
            return self.__front.getVal()

        elif index == self.__size - 1:
            return self.__tail.getVal()

        else:
            temp = self.__front
            for x in range(0, index):
                temp = temp.getNext()
            return temp.getVal()

    # Removes the first item in the list.
    def removeFirst(self):
        if self.__size == 0:
            return False

        elif self.__size == 1:
            self.__front = None
            self.__tail = None
            self.__size -= 1

        else:
            nextn = self.__front.getNext()
            nextn.setPrev(None)
            self.__front = nextn
            self.__size -= 1

    # Removes the last item in the list.
    def removeLast(self):
        if self.__size == 0:
            return False

        elif self.__size == 1:
            self.__front = None
            self.__tail = None
            self.__size -= 1

        else:
            prev = self.__tail.getPrev()
            prev.setNext(None)
            self.__tail = prev
            self.__size -= 1

    # Removes an item from the list at a certain index.
    def remove(self, index):
        if self.__checkIndex(index) == False:
            return False
        
        elif self.__size == 1:
            self.__front = None
            self.__tail = None
            self.__size -= 1

        elif index == 0:
            nextn = self.__front.getNext()
            nextn.setPrev(None)
            self.__front = nextn
            self.__size -= 1

        elif index == self.__size - 1:
            prev = self.__tail.getPrev()
            prev.setNext(None)
            self.__tail = prev
            self.__size -= 1

        else:
            temp = self.__front
            for x in range(0, index):
                temp = temp.getNext()
            nextn = temp.getNext()
            prev = temp.getPrev()

            nextn.setPrev(prev)
            prev.setNext(nextn)
            self.__size -= 1

    # Checks to see if the index is valid for the add method.
    def __checkIndexForAdd(self, index):
        if index < 0:
            return False
        
        elif index > self.__size:
            return False

        else:
            return True

    # Checks to see if the index is valid for anyother method than the add method.
    def __checkIndex(self, index):
        if index < 0:
            return False
        
        elif self.__size == 0:
            return False
        
        elif index > self.__size - 1:
            return False

        else:
            return True
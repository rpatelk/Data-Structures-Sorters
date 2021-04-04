class Node:

    def __init__(self, next=None, prev=None, val=None):
        self.next = next
        self.prev = prev
        self.val = val

    def setNext(self, n):
        self.next = n

    def setPrev(self, n):
        self.prev = n

    def getVal(self):
        return self.val

    def getNext(self):
        return self.next
    
    def getPrev(self):
        return self.prev
    

class DoublyLinkedList:

    __size = 0
    __front = None
    __tail = None

    def __init__(self):
        self.__front = None
        self.__tail = None
        self.__size = 0

    def getSize(self):
        return self.__size

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

    def add(self, index, value):
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

        elif index == self.__size - 1:
            n = Node(None, self.__tail, value)
            self.__tail.setNext(n)
            self.__tail = n
            self.__size += 1

        else:
            n = Node(None, None, value)
            temp = self.__front
            for x in range(0, index - 1):
                temp = temp.getNext()
            prev = temp.getPrev()
            temp.setPrev(n)
            n.setNext(temp)
            n.setPrev(prev)
            prev.setNext(n)
            self.__size += 1

    def get(self, index):
        if index == 0:
            return self.__front.getVal()

        elif index == self.__size - 1:
            return self.__tail.getVal()

        else:
            temp = self.__front
            for x in range(0, index - 1):
                temp = temp.getNext()
            return temp

    def removeFirst(self):
        if (self.__size == 0):
            return "fail"

        elif (self.__size == 1):
            self.__front = None
            self.__tail = None
            self.__size -= 1

        else:
            next = self.__front.getNext()
            next.setPrev(None)
            self.__front = next
            self.__size -= 1

    def removeLast(self):
        if (self.__size == 0):
            return "fail"

        elif (self.__size == 1):
            self.__front = None
            self.__tail = None
            self.__size -= 1

        else:
            prev = self.__tail.getPrev()
            prev.setNext(None)
            self.__tail = prev
            self.__size -= 1

    #def remove(index):
class Node:

    def __init__(self, next=None, prev=None, val=None):
        self.next = next
        self.prev = prev
        self.val = val

    def setNext(n):
        self.next = n

    def setPrev(n):
        self.prev = n

    def getVal():
        return self.val

    def getNext():
        return self.next
    
    def getPrev():
        return self.prev
    

class DoublyLinkedList:

    __size = 0
    __front = Node()
    __tail = Node()

    def __init__():
        self.__front = Node()
        self.__tail = Node()
        self.__size = 0

    def addLast(value):
        if self.__size == 0:
            n = Node(None, None, value)
            self.__front = n
            self.__tail = n
        else:
            n = Node(None, self.__tail, value)
            self.__tail.setNext(n)
            self.__tail = n

        self.__size += 1

    def addFirst(value):
        if self.__size == 0:
            n = Node(None, None, value)
            self.__front = n
            self.__tail = n
        else:
            n = Node(self.__front, None, value)
            self.__front.setPrev(n)
            self.__front = n
            self.__size += 1

    def get(index):
        if index == 0:
            return self.__front.getVal()
        elif index == self.__size - 1:
            return self.__tail.getVal()
        else:
            temp = self.__front
            for x in range(0, self.__size - 1):
                if (x == 0):
                    return temp
                else:
                    temp = temp.getNext()
        


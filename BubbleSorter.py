# Class to run bubble sorting algorithm.
# @author Raj Patel 
class BubbleSorter:

    # Data to be sorter.
    __data = []
    
    # Constructor for sorter.
    def __init__(self, data):
        self.setData(data)

    # Resets the data if necessary.
    def setData(self, data):
        self.__data = data

    # Compares 2 items.
    # Current implementation is for numbers, can be changed
    # to implement any type of comparator.
    # If x is less than y return 0 else return 1.
    def compare(self, x, y):
        if x < y:
            return 0
        else:
            return 1

    # Runs the bubble sorter by comparing two sets at a time
    # until the end of the list.
    def sort(self):
        r = True;
        while r:
            r = False
            for x in range(1, len(self.__data)):
                if (self.compare(self.__data[x], self.__data[x - 1]) == 0):
                    prev = self.__data[x - 1]
                    self.__data[x - 1] = self.__data[x]
                    self.__data[x] = prev
                    r = True
        return self.__data
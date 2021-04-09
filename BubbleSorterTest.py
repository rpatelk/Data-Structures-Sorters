import unittest
from BubbleSorter import BubbleSorter

# Test class for the BubbleSorter class.
# @author Raj Patel
class DoublyLinkedListTest(unittest.TestCase):

    # Tests the sorter.
    def test_sorter(self): 

        # Sorts Simple data set.
        data = [4,3,15,7,1,3,9,10,2,4]
        sorter = BubbleSorter(data)
        sortedData = sorter.sort()

        correctSort = [1,2,3,3,4,4,7,9,10,15]

        for x in range(0,len(data)):
            self.assertEqual(correctSort[x], sortedData[x])

        print(sortedData)

        # Sorts Big data set.
        data = [36,86,5,27,94,67,57,88,56,91,44,98,23,17,46,63,97,30,52,78,39,20,53,22,40,34,28,89,81,35,59,82,3,12,72,62,73,33,99,4,69,10,18,92,2,96,61,7,71,54,1,6,45,13,87,70,8,95,80,19,77,74,51,48,25,55,32,24,16,75,100,21,15,58,9,47,43,64,60,37,66,65,85,42,76,49,50,41,31,38,29,83,68,11,79,90,26,14,84,93]
        sorter.setData(data)
        sortedData = sorter.sort()

        correctSort = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]
        
        for x in range(0,len(data)):
            self.assertEqual(data[x], sortedData[x])

        print(sortedData)

if __name__ == '__main__':
    unittest.main()
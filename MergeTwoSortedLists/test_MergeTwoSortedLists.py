import MergeTwoSortedLists    # The code to test
import unittest   # The test framework

class Test_MergeTwoSortedLists(unittest.TestCase):
    def test_case1(self):
        input1 = [4,8,15,19]
        input2 = [7,9,10,16]
        output = [4,7,8,9,10,15,16,19]
        self.assertEqual(MergeTwoSortedLists.mergeSortedLists(input1, input2),output)

    def test_case2(self):
        input1 = [1,2,5,6]
        input2 = [3,4,7,8]
        output = [1,2,3,4,5,6,7,8]
        self.assertEqual(MergeTwoSortedLists.mergeSortedLists(input1, input2),output)

if __name__ == '__main__':
    unittest.main()
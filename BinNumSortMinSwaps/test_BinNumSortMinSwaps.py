import BinNumSortMinSwaps    # The code to test
import unittest   # The test framework

class Test_BinNumSortMinSwaps(unittest.TestCase):
    def test_case1(self):
        inpList = [0,0,1,0,1,0,1,1]
        self.assertEqual(BinNumSortMinSwaps.minSwaps(inpList),3)

    def test_case2(self):
        inpList = [1,1,1,1,0,0,0,0]       
        self.assertEqual(BinNumSortMinSwaps.minSwaps(inpList),0)

if __name__ == '__main__':
    unittest.main()
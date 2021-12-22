import MissingNumberInArray    # The code to test
import unittest   # The test framework

class Test_MissingNumberInArray(unittest.TestCase):
    def test_case1(self):
        input = [3,7,1,2,8,4,5]
        self.assertEqual(MissingNumberInArray.findMissingNumber(input),6)

    def test_case2(self):
        input = [1,8,6,5,4,3,7,9]
        self.assertEqual(MissingNumberInArray.findMissingNumber(input),2)
    
    def test_case3(self):
        input = [1,8,6,5,4,3,7,2]
        self.assertEqual(MissingNumberInArray.findMissingNumber(input),9)

if __name__ == '__main__':
    unittest.main()
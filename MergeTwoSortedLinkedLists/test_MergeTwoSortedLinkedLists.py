import SumOfTwoIntegers    # The code to test
import unittest   # The test framework

class Test_SumOfTwoIntegers(unittest.TestCase):
    def test_case1(self):
        input = [5,7,1,2,8,4,3]
        value = 10
        self.assertEqual(SumOfTwoIntegers.findSumOfTwoIntegers(input, value),True)

    def test_case2(self):
        input = [1,2,3,4,5,6]
        value = 7
        self.assertEqual(SumOfTwoIntegers.findSumOfTwoIntegers(input, value),True)
    
    def test_case3(self):
        input = [5,7,1,2,8,4,3]
        value = 19
        self.assertEqual(SumOfTwoIntegers.findSumOfTwoIntegers(input, value),False)

if __name__ == '__main__':
    unittest.main()
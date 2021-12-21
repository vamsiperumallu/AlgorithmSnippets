import FirstNonRepeatingChar    # The code to test
import unittest   # The test framework

class Test_FirstNonRepeatingChar(unittest.TestCase):
    def test_case1(self):
        input = "aaabcccdeeef"
        self.assertEqual(FirstNonRepeatingChar.getFirstNonRepeatingChar(input),'b')

    def test_case2(self):
        input = "abcbad"     
        self.assertEqual(FirstNonRepeatingChar.getFirstNonRepeatingChar(input),'c')
    
    def test_case3(self):
        input = "abcabcabc"
        self.assertEqual(FirstNonRepeatingChar.getFirstNonRepeatingChar(input),None)

if __name__ == '__main__':
    unittest.main()
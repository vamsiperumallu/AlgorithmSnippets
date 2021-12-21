import LongestSubstring    # The code to test
import unittest   # The test framework

class Test_LongestSubstring(unittest.TestCase):
    def test_case1(self):
        input = "abcabcbb"
        self.assertEqual(LongestSubstring.lengthOfLongestSubstring(input),3)

    def test_case2(self):
        input = "bbbb"     
        self.assertEqual(LongestSubstring.lengthOfLongestSubstring(input),1)
    
    def test_case3(self):
        input = "pwwkew"
        self.assertEqual(LongestSubstring.lengthOfLongestSubstring(input),3)

    def test_case4(self):
        input = "qwertyabcdaef"     
        self.assertEqual(LongestSubstring.lengthOfLongestSubstring(input),10)

if __name__ == '__main__':
    unittest.main()
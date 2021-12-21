import LongestPalindromicSubstring    # The code to test
import unittest   # The test framework

class Test_LongestPalindromicSubstring(unittest.TestCase):
    def test_case1(self):
        input = "babad"
        self.assertEqual(LongestPalindromicSubstring.longestPalindrome(input),'bab')

    def test_case2(self):
        input = "cbbd"     
        self.assertEqual(LongestPalindromicSubstring.longestPalindrome(input),'bb')
    
    def test_case3(self):
        input = "abcba"
        self.assertEqual(LongestPalindromicSubstring.longestPalindrome(input),'abcba')

    def test_case4(self):
        input = "abcdba"     
        self.assertEqual(LongestPalindromicSubstring.longestPalindrome(input),'a')

if __name__ == '__main__':
    unittest.main()
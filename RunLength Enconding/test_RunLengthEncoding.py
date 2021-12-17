import RunLengthEncoding    # The code to test
import unittest   # The test framework

class Test_RunLengthEncoding(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(RunLengthEncoding.generateEncoding("aaaabbcc"), "4a2b2c")

    def test_case2(self):
        self.assertEqual(RunLengthEncoding.generateEncoding("aaaabbcc"), "4a2b2")

if __name__ == '__main__':
    unittest.main()
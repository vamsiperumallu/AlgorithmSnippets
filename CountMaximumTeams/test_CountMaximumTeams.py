import CountMaximumTeams    # The code to test
import unittest   # The test framework

class Test_CountMaximumTeams(unittest.TestCase):
    def test_case1(self):
        skill =  [3,4,3,1,6,5]
        teamSize = 3
        maxDiff = 2
        self.assertEqual(CountMaximumTeams.countMaximumTeams(skill,teamSize,maxDiff), 2)

    def test_case2(self):
        skill =  [5,1,2,1,4,5]
        teamSize = 3
        maxDiff = 2        
        self.assertEqual(CountMaximumTeams.countMaximumTeams(skill,teamSize,maxDiff), 2)

    def test_case3(self):
        skill =  [9,3,5,7,1]
        teamSize = 2
        maxDiff = 1     
        self.assertEqual(CountMaximumTeams.countMaximumTeams(skill,teamSize,maxDiff), 0)
if __name__ == '__main__':
    unittest.main()
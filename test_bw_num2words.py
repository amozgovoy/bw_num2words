import unittest
from bw_num2words import solution

class TestIfnum2wordsIsCorrect(unittest.TestCase):
    def testNumber0(self):
        self.assertEqual(solution(0), "Zero")
    def testNumber1000(self):
        self.assertEqual(solution(1000), "One-Thousand")
    def testNumber12(self):
        self.assertEqual(solution(12), "Twelve")
    def testNumber119(self):
        self.assertEqual(solution(119), "One-Hundred Nineteen")
    def testNumber256(self):
        self.assertEqual(solution(256), "Two-Hundred Fifty Six")
    def testNumber692(self):
        self.assertEqual(solution(692), "Six-Hundred Ninety Two")
    def testNumber1100(self):
        self.assertEqual(solution(1100), "Error: the number is out of bounds")
    def testNumberMinus1(self):
        self.assertEqual(solution(-1), "Error: the number is out of bounds")        

if __name__ == '__main__':
    unittest.main()
import unittest
from stock_picker import picker

class StockPickerTestCases(unittest.TestCase):

    def test_case_1(self):
        output = picker([17,3,6,9,15,8,6,1,10])
        self.assertEqual(output, [1,4])

    def test_case_2(self):
        output = picker([3,17,6,9,18,15,6,1,10])
        self.assertEqual(output, [0,4])

    def test_case_3(self):
        output = picker([1,17,6,9,8,15,6,3,19])
        self.assertEqual(output, [0,8])
       
    def test_case_4(self):
        output = picker([19,17,6,9,8,15,6,3,1])
        self.assertEqual(output, [2,5])
    
    def test_case_5(self):
        output = picker([3, 3, 3, 3])
        self.assertEqual(output, [None, 3])

# print(picker([17,3,6,9,15,8,6,1,10]) == [1,4])
# print(picker([3,17,6,9,18,15,6,1,10]) == [0,4])
# print(picker([1,17,6,9,8,15,6,3,19]) == [0,8])
# print(picker([19,17,6,9,8,15,6,3,1]) == [2,5])

if __name__ == '__main__':
    unittest.main()

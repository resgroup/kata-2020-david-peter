import unittest
import kata
from parameterized import parameterized

class KataTests(unittest.TestCase):

    @parameterized.expand([
        ['O', 1],
        ['Y', 0]
    ])
    def test_first_row(self, expectedOutput, startRange):
        for seconds in range(startRange, 60, 2):
            self.assertEqual(expectedOutput, kata.first_row(seconds))

    @parameterized.expand([
        ['OOOO', 0, 5],
        ['ROOO', 5, 10],
        ['RROO', 10, 15],
        ['RRRO', 15, 20],
        ['RRRR', 20, 24],
    ])
    def test_second_row(self, expectedOutput, startRange, endRange):
        for hours in range(startRange, endRange):
            self.assertEqual(expectedOutput, kata.second_row(hours))

    @parameterized.expand([
        ['OOOO', 0],
        ['ROOO', 1],
        ['RROO', 2],
        ['RRRO', 3],
        ['RRRR', 4],
    ])
    def test_third_row(self, expectedOutput, startRange):
        for hours in range(startRange, 24, 5):
            self.assertEqual(expectedOutput, kata.third_row(hours))

    @parameterized.expand([
        ['OOOOOOOOOOO', 0, 5],
        ['YOOOOOOOOOO', 5, 5],
        ['YYOOOOOOOOO', 10, 5],
        ['YYYOOOOOOOO', 15, 5],
        ['YYYYOOOOOOO', 20, 5],
        ['YYYYYOOOOOO', 25, 5],
        ['YYYYYYOOOOO', 30, 5],
        ['YYYYYYYOOOO', 35, 5],
        ['YYYYYYYYOOO', 40, 5],
        ['YYYYYYYYYOO', 45, 5],
        ['YYYYYYYYYYO', 50, 5],
        ['YYYYYYYYYYY', 55, 5],
    ])
    def test_fourth_row(self, expectedOutput, startRange, rangeLength):
        for minutes in range(startRange, startRange + rangeLength):
            self.assertEqual(expectedOutput, kata.fourth_row(minutes))

    @parameterized.expand([
        ['OOOO', 0],
        ['YOOO', 1],
        ['YYOO', 2],
        ['YYYO', 3],
        ['YYYY', 4],
    ])
    def test_fifth_row(self, expectedOutput, startRange):
        for minutes in range(startRange, 60, 5):
            self.assertEqual(expectedOutput, kata.fifth_row(minutes))

    def test_berlin_clock(self):
        self.assertEqual('O\nRROO\nRROO\nYYYYYYYYYYY\nYOOO', kata.berlin_clock(12, 56, 1))

if __name__ == '__main__':
    unittest.main()
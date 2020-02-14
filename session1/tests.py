import unittest
import kata

class KataTests(unittest.TestCase):

    def test_first_row_even(self):
        for seconds in range(0, 60, 2):
            self.assertEqual('Y', kata.first_row(seconds))

    def test_first_row_odd(self):
        for seconds in range(1, 60, 2):
            self.assertEqual('O', kata.first_row(seconds))

    def test_second_row_less_than_5(self):
        for hours in range(0,5):
            self.assertEqual('OOOO', kata.second_row(hours))

    def test_second_row_between_5_and_9(self):
        for hours in range(5,10):
            self.assertEqual('ROOO', kata.second_row(hours))

    def test_second_row_between_10_and_14(self):
        for hours in range(10,15):
            self.assertEqual('RROO', kata.second_row(hours))

    def test_second_row_between_15_and_19(self):
        for hours in range(15,20):
            self.assertEqual('RRRO', kata.second_row(hours))

    def test_second_row_between_20_and_23(self):
        for hours in range(20,24):
            self.assertEqual('RRRR', kata.second_row(hours))

    def test_third_row_all_off(self):
        for hours in range(0, 24, 5):
            self.assertEqual('OOOO', kata.third_row(hours))

    def test_third_row_one_on(self):
        for hours in range(1, 24, 5):
            self.assertEqual('ROOO', kata.third_row(hours))

    def test_third_row_two_on(self):
        for hours in range(2, 24, 5):
            self.assertEqual('RROO', kata.third_row(hours))

    def test_third_row_three_on(self):
        for hours in range(3, 24, 5):
            self.assertEqual('RRRO', kata.third_row(hours))

    def test_third_row_all_on(self):
        for hours in range(4, 24, 5):
            self.assertEqual('RRRR', kata.third_row(hours))

if __name__ == '__main__':
    unittest.main()
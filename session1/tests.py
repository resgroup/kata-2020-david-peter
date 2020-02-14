import unittest
import kata

class KataTests(unittest.TestCase):

    def test_first_row_even(self):
        for seconds in range(0, 60, 2):
            self.assertEqual('Y', kata.first_row(seconds))

    def test_first_row_odd(self):
        for seconds in range(1, 60, 2):
            self.assertEqual('O', kata.first_row(seconds))

if __name__ == '__main__':
    unittest.main()
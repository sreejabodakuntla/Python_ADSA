
import unittest
from task import pairInSortedRotated

class TestAssignment(unittest.TestCase):

    def test1(self):
        self.assertEqual(pairInSortedRotated([11, 15, 6, 8, 9, 10], 16), True)

    def test2(self):
        self.assertEqual(pairInSortedRotated([11, 15, 6, 8, 9, 10], 21), True)

    def test3(self):
        self.assertEqual(pairInSortedRotated([11, 15, 6, 8, 9, 10], 20), True)

if __name__ == "__main__":
    unittest.main()
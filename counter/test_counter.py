"""Write a unit test to verify that Counter is a singleton.

   Also verify that all instances share the same count
   and that the count is not reset to 0 when you invoke
   count = Counter()
   after the first time.

   You can use pytest or unittest.
"""
import unittest
from counter import Counter


class TestCounter(unittest.TestCase):
    """Testcase from Readme"""
    def test_counter(self):
        """check that the counter won't return to zero,
        they are share the same count and can increase"""

        counter_1 = Counter()
        self.assertEqual(counter_1.count, 1)
        self.assertEqual(counter_1.count, 1)  # invoking count doesn't change anything
        self.assertEqual(counter_1.increment(), 2)  # add 1 and return the new count

        counter_2 = Counter()
        self.assertTrue(counter_2 is counter_1)
        self.assertEqual(counter_2.count, 2)  # shares the same count
        self.assertEqual(counter_2.increment(), 3)  # add 1 and return the new count
        self.assertEqual(counter_1.count, 3)
        self.assertEqual(counter_1.count, 3)  # counter_1 doesn't set to zero

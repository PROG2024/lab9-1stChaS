"""Write a unit test to verify that Counter is a singleton.

   Also verify that all instances share the same count
   and that the count is not reset to 0 when you invoke 
   count = Counter() 
   after the first time.

   You can use pytest or unittest.
"""
import unittest
import pytest
from circle import Circle


# Circle.add_area
class Test_Area(unittest.TestCase):
    """Testcase for add.area"""

    # question 1
    def test_radius_positive(self, other):
        self.circle = Circle
        if Circle.add_area() > 0 and other.radius > 0:
            self.assertTrue(self.circle)
            self.assertTrue(other.radius)
        raise ValueError("The radius should always be positive number.")

    # question 2
    def test_one_zero(self, other):
        if self.assertEqual(0, self.circle):
            self.assertNotEqual(0, self.circle)
        elif self.assertEqual(0, other.circle):
            self.assertNotEqual(0, other.circle)

    # question 3
    def raise_negative(self):
        with self.assertRaises(ValueError):
            self.circle.Circle()

        # # pytest
        # with pytest.raises(ValueError):
        #     self.radius.Circle()









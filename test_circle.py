"""Unit tests of the Circle class using unittest or pytest (your choice).

Write unit tests as described in README.md.

1. Unit test for add_area using typical values.
2. Unit test for add_area for an "edge case" where one circle has radius 0.
3. Unit test that circle constructor raises exception of radius is negative.

"""
import unittest
import math
from circle import Circle


# Circle.add_area
class Test_Area(unittest.TestCase):
    """Testcase for add.area"""

    # question 1
    def test_radius_positive(self):
        """Test `add_area` with two circles having positive radius values."""
        self.circle_1 = Circle(3)
        self.circle_2 = Circle(4)
        # the Euclidean norm
        total_area = self.circle_2.add_area(self.circle_1)
        self.assertEqual(total_area.get_radius(), 5)
        area = math.pi*(5**2)  # manual way
        self.assertEqual(total_area.get_area(), area)

    # question 2
    def test_one_zero(self):
        """Test `add_area` when one of the circles has radius 0,
        the other has non-zero radius."""
        self.circle_1 = Circle(16)
        self.circle_2 = Circle(0)  # radius 0 circle
        # check the radius of circle_2 == 0
        self.assertEqual(self.circle_2.get_radius(), 0)
        # the Euclidean norm
        total_area = self.circle_2.add_area(self.circle_1)
        area = math.pi * (16 ** 2)  # manual way
        self.assertEqual(total_area.get_area(), area)

    # question 3
    def test_raise_negative(self):
        """Circle constructor raises exception if the radius is negative."""
        with self.assertRaises(ValueError):
            self.circle = Circle(-5)

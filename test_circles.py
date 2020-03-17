"""
Unit tests for the Circles
"""

import circles
from math import pi


class TestCircle:
    def test_area(self):
        # Test areas when radius >= 0
        assert pi * (2 ** 2) == circles.circle_area(2)
        assert pi * (2.1 ** 2) == circles.circle_area(2.1)

    def test_value(self):
        # Make sure value errors are raised when necessary
        assert pi * ((-1) ** 2) == circles.circle_area(-1)

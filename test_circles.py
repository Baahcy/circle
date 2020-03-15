"""
Unit tests for the Circles
"""

import circles
from math import pi


class TestCircle:
    def test_area(self):
        # Test areas when radius >= 0
        # assert 12.566370614359172 == circles.circle_area(2)
        assert pi * (2 ** 2) == circles.circle_area(2)

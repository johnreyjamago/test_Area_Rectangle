# John-Rey Jamago
import unittest


def area_rect(l, w):
    if l < 0 or w < 0:
        raise ValueError("The Variable/s should be positive.")
    return l * w


class TestRectangleArea(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(area_rect(1, 29), 29.0)
        self.assertAlmostEqual(area_rect(12, 25), 300.0)
        self.assertAlmostEqual(area_rect(0, 0), 0.0)

    def test_values(self):
        self.assertRaises(ValueError, area_rect, -1, 1)


if __name__ == '__main__':
    unittest.main()

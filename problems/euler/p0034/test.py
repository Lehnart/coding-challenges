import unittest

from problems.euler.p0034.main import p0034


class TestP0034(unittest.TestCase):

    def test_p0034(self):
        self.assertEqual(p0034(), 40730)

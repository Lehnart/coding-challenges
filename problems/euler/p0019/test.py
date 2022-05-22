import unittest

from problems.euler.p0019.main import p0019


class TestP0019(unittest.TestCase):

    def test_p0019(self):
        self.assertEqual(p0019(), 171)

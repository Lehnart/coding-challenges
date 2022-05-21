import unittest

from problems.euler.p0020.main import p0020


class TestP0020(unittest.TestCase):

    def test_p0020(self):
        self.assertEqual(p0020(), 648)

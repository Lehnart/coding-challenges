import unittest

from problems.euler.p0024.main import p0024


class TestP0024(unittest.TestCase):

    def test_p0024(self):
        self.assertEqual(p0024(), 2783915460)

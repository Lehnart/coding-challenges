import unittest

from problems.euler.p0025.main import p0025


class TestP0025(unittest.TestCase):

    def test_p0025(self):
        self.assertEqual(p0025(), 4782)

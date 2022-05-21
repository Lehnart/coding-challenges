import unittest

from problems.euler.p0005.main import p0005


class TestP0005(unittest.TestCase):

    def test_p0005(self):
        self.assertEqual(p0005(), 232792560)

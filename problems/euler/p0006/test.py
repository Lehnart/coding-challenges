import unittest

from problems.euler.p0006.main import p0006


class TestP0006(unittest.TestCase):

    def test_p0006(self):
        self.assertEqual(p0006(), 25164150)

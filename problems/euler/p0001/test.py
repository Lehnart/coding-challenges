import unittest

from problems.euler.p0001.main import p0001


class TestP0001(unittest.TestCase):

    def test_p0001(self):
        self.assertEqual(p0001(), 233168)

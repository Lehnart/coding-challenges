import unittest

from problems.euler.p0004.main import p0004


class TestP0004(unittest.TestCase):

    def test_p0004(self):
        self.assertEqual(p0004(), 906609)

import unittest

from problems.euler.p0021.main import p0021


class TestP0021(unittest.TestCase):

    def test_p0021(self):
        self.assertEqual(p0021(), 31626)

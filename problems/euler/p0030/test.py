import unittest

from problems.euler.p0030.main import p0030


class TestP0030(unittest.TestCase):

    def test_p0030(self):
        self.assertEqual(p0030(), 443839)

import unittest

from problems.euler.p0719.main import p0719


class TestP0719(unittest.TestCase):

    def test_p0719_verif(self):
        self.assertEqual(p0719(10000), 41333)

    def test_p0719(self):
        self.assertEqual(p0719(1000000000000), 128088830547982)
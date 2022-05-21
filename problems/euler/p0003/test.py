import unittest

from problems.euler.p0003.main import p0003


class TestP0003(unittest.TestCase):

    def test_p0003(self):
        self.assertEqual(p0003(), 6857)

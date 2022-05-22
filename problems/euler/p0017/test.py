import unittest

from problems.euler.p0017.main import p0017


class TestP0017(unittest.TestCase):

    def test_p0017(self):
        self.assertEqual(p0017(), 21124)

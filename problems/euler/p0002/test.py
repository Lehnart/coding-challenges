import unittest

from problems.euler.p0002.main import p0002


class TestP0002(unittest.TestCase):

    def test_p0002(self):
        self.assertEqual(p0002(), 4613732)

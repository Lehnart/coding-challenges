import unittest

from problems.euler.p0012.main import p0012


class TestP0012(unittest.TestCase):

    def test_p0012(self):
        self.assertEqual(p0012(), 76576500)

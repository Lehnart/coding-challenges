import unittest

from problems.euler.p0028.main import p0028


class TestP0028(unittest.TestCase):

    def test_p0028(self):
        self.assertEqual(p0028(), 669171001)

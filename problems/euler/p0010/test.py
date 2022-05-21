import unittest

from problems.euler.p0010.main import p0010


class TestP0010(unittest.TestCase):

    def test_p0010(self):
        self.assertEqual(p0010(), 142913828922)

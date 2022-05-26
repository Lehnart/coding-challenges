import unittest

from problems.euler.p0700.main import p0700


class TestP0700(unittest.TestCase):

    def test_p0700(self):
        self.assertEqual(p0700(), 1517926517777556)

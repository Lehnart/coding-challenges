import unittest

from problems.euler.p0008.config import NUMBER
from problems.euler.p0008.main import p0008


class TestP0008(unittest.TestCase):

    def test_p0008(self):
        self.assertEqual(p0008(NUMBER), 23514624000)

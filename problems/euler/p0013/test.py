import unittest

from problems.euler.p0013.config import NUMBER
from problems.euler.p0013.main import p0013


class TestP0013(unittest.TestCase):

    def test_p0013(self):
        self.assertEqual(p0013(NUMBER), 5537376230)

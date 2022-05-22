import unittest

from problems.euler.p0018.config import triangle_str
from problems.euler.p0018.main import p0018


class TestP0018(unittest.TestCase):

    def test_p0018(self):
        self.assertEqual(p0018(triangle_str), 1074)

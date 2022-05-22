import os
import unittest

from problems.euler.p0022.main import p0022


class TestP0022(unittest.TestCase):

    def test_p0022(self):
        file_path_str = os.path.realpath(__file__)
        path_str = os.path.dirname(file_path_str)
        self.assertEqual(p0022(os.path.join(path_str, "names.txt")), 871198282)

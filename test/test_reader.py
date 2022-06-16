import unittest
from pyex.reader import Reader
class TestReader(unittest.TestCase):
    def test_read(self):
        reader = Reader("resources/Test.xlsx")
        reader.read()

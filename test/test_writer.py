import unittest
from pyex.writer import JSONWriter
from pyex.reader import Reader
class TestWriter(unittest.TestCase):
    def test_JSONWriter(self):
        writer = JSONWriter("resources/Test.json")
        reader = Reader("resources/Test.xlsx")
        writer.write(reader.read())


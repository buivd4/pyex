import unittest
from pyex.writer import StringWriter
from pyex.reader import Reader
class TestWriter(unittest.TestCase):
    def test_StringWriter(self):
        writer = StringWriter("resources/Test.json")
        reader = Reader("resources/Test.xlsx")
        output = writer.write(reader.read())
        assert output == """{
    "Sheet1": [
        {
            "Header1": "x",
            "Header2": "Value2B",
            "Header3": "Value2C",
            "Header4": "Value2D",
            "Header5": "Value2E",
            "Header6": "Value2F"
        },
        {
            "Header1": null,
            "Header2": "Value3B",
            "Header3": "Value3C",
            "Header4": "Value3D",
            "Header5": "Value3E",
            "Header6": "Value3F"
        },
        {
            "Header1": null,
            "Header2": "Value4B",
            "Header3": "Value4C",
            "Header4": "Value4D",
            "Header5": "Value4E",
            "Header6": "Value4F"
        },
        {
            "Header1": "yz",
            "Header2": "Value2B",
            "Header3": "Value2C",
            "Header4": "Value2D",
            "Header5": "Value2E",
            "Header6": "Value2F"
        },
        {
            "Header1": null,
            "Header2": "Value3B",
            "Header3": "Value3C",
            "Header4": "Value3D",
            "Header5": "Value3E",
            "Header6": "Value3F"
        },
        {
            "Header1": null,
            "Header2": "Value4B",
            "Header3": "Value4C",
            "Header4": "Value4D",
            "Header5": "Value4E",
            "Header6": "Value4F"
        }
    ],
    "Sheet2": [
        {
            "Header1": "xxx",
            "Header2": "Value2B",
            "Header3": "Value2C",
            "Header4": "Value2D",
            "Header5": "Value2E",
            "Header6": "Value2F"
        },
        {
            "Header1": null,
            "Header2": "Value3B",
            "Header3": "Value3C",
            "Header4": "Value3D",
            "Header5": "Value3E",
            "Header6": "Value3F"
        },
        {
            "Header1": null,
            "Header2": "Value4B",
            "Header3": "Value4C",
            "Header4": "Value4D",
            "Header5": "Value4E",
            "Header6": "Value4F"
        }
    ]
}"""


from pyex.data import Data
from pyex.processor import AbstractProcessor


class ChangeHeaderProcessor(AbstractProcessor):
    @staticmethod
    def normalize_header(header):
        return header.replace(" ","_").replace("(","_").replace(")","_").replace("/","_").lower()

    def execute(self, data: Data)-> Data:
        for sheet in data.sheets:
            sheet.header = [self.normalize_header(h) for h in sheet.header]
        return data
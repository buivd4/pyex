from pyex.data import Data
from pyex.processor import AbstractProcessor


class ChangeHeaderProcessor(AbstractProcessor):
    @staticmethod
    def normalize_header(header):
        new_header= header.replace(" ","_").replace("(","_").replace(")","_").replace("/","_").lower()
        if new_header in ("experience__months_","experience__months", "experience_months_"):
            return "experience_months"
        return new_header

    def execute(self, data: Data)-> Data:
        for sheet in data.sheets:
            sheet.header = [self.normalize_header(h) for h in sheet.header]
        return data

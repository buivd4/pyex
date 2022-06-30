import logging
import re

from openpyxl import load_workbook

from pyex.data import Data, Sheet
from pyex.constant import UNDEFINED

LOGGER = logging.getLogger("pyex")

class Reader:
    def __init__(self, filepath, with_header=True, default = None, exclude=None, ffill = []):
        self.filepath = filepath
        self.workbook = load_workbook(filepath,data_only=True)
        self.with_header = with_header
        self.default = default
        self.exclude = exclude
        self.ffill = ffill

    def read(self)->dict:
        LOGGER.info(f"Read file from {self.filepath}")
        data = Data()
        for sheet in self.workbook.worksheets:
            if self.exclude:
                if re.match(self.exclude, sheet.title):
                    LOGGER.debug(f"Exclude sheet: {sheet.title}")
                    continue
            LOGGER.debug(f"Reading sheet: {sheet.title}")
            data_sheet = Sheet(sheet.title)
            lc=0
            last_cell = None                    
            for i, row in enumerate(sheet.values):
                lc+=1
                if self.with_header and i==0:
                    header = list(row)
                    for j, h in enumerate(header):
                        if h is None or h==u"\u00A0":
                            header[j] = "_".join([UNDEFINED, str(j)])
                    LOGGER.debug(f"Header: {',  '.join(header)}")
                    data_sheet.set_header(header)
                else:
                    record = list(row)
                    for j, cell in enumerate(record):
                        if cell in (None,u"\u00A0") and j in self.ffill and last_cell is not None and len(last_cell)>j:
                            record[j] = last_cell[j]
                        elif cell in (None,u"\u00A0"):
                            record[j] = self.default
                    last_cell = record
                    data_sheet.add_record(record)
                if all([cell is None for cell in row]):
                    break
            LOGGER.debug(f"Line count: {lc}")
            data.add_sheet(data_sheet)
        return data

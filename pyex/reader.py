from openpyxl import load_workbook
from pyex.data import Data,Sheet
import re
import logging

LOGGER = logging.getLogger("pyex")

class Reader:
    def __init__(self, filepath):
        self.filepath = filepath
        self.workbook = load_workbook(filepath)

    def read(self, with_header=True, default = None, exclude=None, ffill = [])->dict:
        LOGGER.info(f"Read file from {self.filepath}")
        data = Data()
        for sheet in self.workbook.worksheets:
            if exclude:
                if re.match(exclude, sheet.title):
                    LOGGER.debug(f"Exclude sheet: {sheet.title}")
                    continue
            LOGGER.debug(f"Reading sheet: {sheet.title}")
            data_sheet = Sheet(sheet.title)
            lc=0
            last_cell = None                    
            for i, row in enumerate(sheet.values):
                lc+=1
                if with_header and i==0:
                    header = list(row)
                    for j, cell in enumerate(header):
                        if cell is None:
                            header[j] = str(j)
                    LOGGER.debug(f"Header: {',  '.join(header)}")
                    data_sheet.set_header(header)
                else:
                    record = list(row)
                    for j, cell in enumerate(record):
                        if cell is None and j in ffill and last_cell is not None and len(last_cell)>j:
                            record[j] = last_cell[j]
                        elif cell is None:
                            record[j] = default
                    last_cell = record
                    data_sheet.add_record(record)
                if all([cell is None for cell in row]):
                    break
            LOGGER.debug(f"Line count: {lc}")
            data.add_sheet(data_sheet)
        return data

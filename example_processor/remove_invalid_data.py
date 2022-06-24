import logging

from pyex.data import Data
from pyex.processor import AbstractProcessor
from pyex.constant import UNDEFINED

LOGGER = logging.getLogger("pyex")

class RemoveInvalidDataProcessor(AbstractProcessor):
    def execute(self, data: Data)-> Data:
        for s, sheet in enumerate(data.sheets):
            for j,header in enumerate(sheet.header):
                if header == "experience_months":
                    for r,rec in enumerate(sheet.data):
                        data.sheets[s].data[r][j]=data.sheets[s].data[r][j] if data.sheets[s].data[r][j]!="undefined" else 0
                if header.startswith(UNDEFINED) and all(record[j] in ("undefined", u"\u00A0") for record in sheet.data):
                    LOGGER.debug(f"Pop column '{header}' of {sheet.name}")
                    data.sheets[s].header.pop(j)
                    data.sheets[s].buck_delete(j)

        return data
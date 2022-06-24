import logging

from pyex.data import Data
from pyex.processor import AbstractProcessor
from pyex.constant import UNDEFINED

LOGGER = logging.getLogger("pyex")

class CleanProcessor(AbstractProcessor):
    def execute(self, data: Data)-> Data:
        data.get_sheet("13. Test Eng").header.pop(0)
        data.get_sheet("13. Test Eng").buck_delete(0)
        data.get_sheet("13. Test Eng").header[0]="items"
        return data

import logging

from pyex.data import Data
from pyex.processor_chain import ProcessorChain
from pyex.processor import AbstractProcessor
from pyex.constant import UNDEFINED

LOGGER = logging.getLogger("pyex")

class LazyProcessor(AbstractProcessor):
    def __init__(self):
        self.subchain = ProcessorChain()
        self.subchain.register(r".\example_processor\change_header.py:ChangeHeaderProcessor")
        self.subchain.register(r".\example_processor\remove_invalid_data.py:RemoveInvalidDataProcessor")
        self.subchain.register(r".\example_processor\clean_data.py:CleanProcessor")
        self.subchain.register(r".\example_processor\add_user_info.py:AddUserInfoProcessor")
        
        
    def execute(self, data:Data)->Data:
        return self.subchain.execute(data)

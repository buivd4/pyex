import logging

from pyex.data import Data
LOGGER = logging.getLogger("pyex")

class AbstractProcessor:
    def _execute(self, data: Data)->Data:
        LOGGER.info(f"Run processor {self.__class__.__name__}")
        return self.execute(data)
    
    def execute(self, data: Data)->Data:
        raise NotImplementedError()
    
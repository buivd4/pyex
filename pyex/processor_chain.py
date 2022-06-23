from pyex.data import Data
import importlib
import sys
import os
from pyex.processor import AbstractProcessor

def load_processor(module_as_str):
    #__import__ method used
    # to fetch module
    # module_as_str: <module_path>:<class_name>
    *module_str, class_name = module_as_str.split(":")
    module_str = ":".join(module_str)
    module_path = os.path.dirname(os.path.realpath(module_str))
    module_name = ".".join(os.path.basename(module_str).split(".")[:-1])
    sys.path.append(module_path)
    module = __import__(module_name)

    # getting attribute by
    # getattr() method
    clazz= getattr(module, class_name)
    if not issubclass(clazz, AbstractProcessor):
        raise TypeError("Processor class must be inherited from pyex.processor.AbstractProcessor")
    return clazz

class ProcessorChain:
    def __init__(self):
        self.chain = []

    def register(self, module_as_str):
        clazz = load_processor(module_as_str)
        self.chain.append(clazz())

    def execute(self, data: Data)->Data:
        output = data
        for processor in self.chain:
            output = processor._execute(output)
        return data


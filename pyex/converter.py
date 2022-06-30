import logging
from pyex.reader import Reader
from pyex.writer import JSONWriter

LOGGER = logging.getLogger("pyex")

class Converter:
    def __init__(self, fin, fout, processor_chain, configurations):
        self.fin = fin
        self.fout = fout
        self.processor_chain = processor_chain
        self.configurations = configurations
        self.grp_by_sheet = (not self.configurations.pop("flatten")) if "flatten" in self.configurations else True
        self.grp_by_sheet = False

    def convert(self):
        reader=Reader(filepath = self.fin, **self.configurations)
        writer=JSONWriter(filepath = self.fout, grp_by_sheet=self.grp_by_sheet)
        data = reader.read()
        data = self.processor_chain.execute(data)
        writer.write(data)
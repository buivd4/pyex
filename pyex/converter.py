import logging
LOGGER = logging.getLogger("pyex")

class Converter:
    def __init__(self, reader, processor_chain, writer):
        self.reader = reader
        self.processor_chain = processor_chain
        self.writer = writer

    def run(self):
        data = self.reader.read()
        data = self.processor_chain.execute(data)
        self.writer.write(data)


class BuckConverter:
    def __init__(self, readers, processor_chain, writers):
        assert type(readers)==list, "Argument readers of BuckReader must be a list"
        assert type(writers)==list, "Argument writers of BuckReader must be a list"

        self.readers = readers
        self.processor_chain = processor_chain
        self.writers = writers

    def run(self):
        for reader,writer in zip(self.readers,self.writers):
            LOGGER.info(f"Processing {reader.filepath}")
            data = reader.read()
            data = self.processor_chain.execute(data)
            writer.write(data)
        
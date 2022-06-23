class Converter:
    def __init__(self, reader, processor_chain, writer):
        self.reader = reader
        self.processor_chain = processor_chain
        self.writer = writer

    def run(self):
        data = self.reader.read()
        data = self.processor_chain.execute(data)
        self.writer.write(data)
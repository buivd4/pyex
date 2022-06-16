class Sheet:
    def __init__(self,name):
        self.name = name
        self.data = []
        self.header = []

    def set_header(self, header):
        self.header=header

    def add_record(self, record):
        self.data.append(record)

    def __str__(self):
        return f"<Sheet \"{self.name}\">"

class Data:
    def __init__(self):
        self.sheets = []

    def add_sheet(self,sheet):
        self.sheets.append(sheet)

    def add_record(self,sheet_name, record):
        for sheet in self.sheets:
            if sheet.name == sheet_name:
                sheet.add_record(record)
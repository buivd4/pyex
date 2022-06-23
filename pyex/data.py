class Sheet:
    def __init__(self,name):
        self.name = name
        self.data = []
        self.header = []

    def set_header(self, header):
        self.header=header

    def add_record(self, record):
        self.data.append(record)

    def get_record(self, ith):
        return self.data[ith]

    def buck_delete(self, ith):
        for i in range(len(self.data)):
            self.data[i].pop(ith)

    def buck_insert(self, data:dict):
        """
            Insert new data to every record
        """
        assert type(data)==dict, "Input of buck_insert must be dict"
        self.header.extend(list(data.keys()))
        for record in self.data:
            record.extend(data.values())

    def __str__(self):
        return f"<Sheet \"{self.name}\">"

class Data:
    def __init__(self):
        self.sheets = []

    def pop(self, sheet_name):
        for i, sheet in enumerate(self.sheets):
            if sheet.name == sheet_name:
                return self.sheets.pop(i)
        raise KeyError(f"Sheet name {sheet_name} not found")

    def get_sheet(self, sheet_name):
        for sheet in self.sheets:
            if sheet.name == sheet_name:
                return sheet
        raise KeyError(f"Sheet name {sheet_name} not found")

    def add_sheet(self,sheet):
        self.sheets.append(sheet)

    def add_record(self,sheet_name, record):
        for sheet in self.sheets:
            if sheet.name == sheet_name:
                sheet.add_record(record)
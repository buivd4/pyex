import json
import datetime
import logging

LOGGER = logging.getLogger("pyex")

class AbstractWriter:
    def __init__(self,filepath):
        self.filepath = filepath

    def _write(self, data):
        output = {}
        for sheet in data.sheets:
            dt_sheet = []
            for record in sheet.data:
                dt_sheet.append(dict(zip(sheet.header, record)))
            output.update({sheet.name:dt_sheet})
        return output

    def _save(self,data):
        raise NotImplementedError()

    def write(self,data):
        LOGGER.info(f"Write data to {self.filepath}")
        return self._save(self._write(data))

class JSONWriter(AbstractWriter):
    class DateTimeJSONEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, (datetime.date, datetime.datetime)):
                return obj.isoformat()

    def _save(self,data):
        with open(self.filepath,"w") as output:
            json.dump(data,output,indent=4,cls=self.DateTimeJSONEncoder)
            return data

class StringWriter(AbstractWriter):
    class DateTimeJSONEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, (datetime.date, datetime.datetime)):
                return obj.isoformat()

    def _save(self,data):
        output= json.dumps(data,indent=4 , cls=self.DateTimeJSONEncoder)
        return output
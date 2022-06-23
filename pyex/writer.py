import datetime
import json
import logging

LOGGER = logging.getLogger("pyex")


class AbstractWriter:
    def __init__(self, grp_by_sheet=True):
        self.grp_by_sheet=grp_by_sheet

    def _write(self, data):
        output = {} if self.grp_by_sheet else []
        for sheet in data.sheets:
            dt_sheet = []
            for record in sheet.data:
                dt_sheet.append(dict(zip(sheet.header, record)))
            if self.grp_by_sheet:
                output.update({sheet.name: dt_sheet})
            else:
                output.extend(dt_sheet)
        return output

    def _save(self, data):
        raise NotImplementedError()

    def write(self, data):
        return self._save(self._write(data))


class JSONWriter(AbstractWriter):
    class DateTimeJSONEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, (datetime.date, datetime.datetime)):
                return obj.isoformat()

    def __init__(self, filepath, grp_by_sheet=True):
        self.filepath = filepath
        super().__init__(grp_by_sheet)

    def _save(self, data):
        with open(self.filepath, "w") as output:
            LOGGER.info(f"Write data to {self.filepath}")
            json.dump(data, output, indent=4, cls=self.DateTimeJSONEncoder)
            return data


class RawWriter(AbstractWriter):
    class DateTimeJSONEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, (datetime.date, datetime.datetime)):
                return obj.isoformat()

    def _save(self, data):
        output = json.loads(json.dumps(data, indent=4, cls=self.DateTimeJSONEncoder))
        return output

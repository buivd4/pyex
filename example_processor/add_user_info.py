from pyex.data import Data
from pyex.processor import AbstractProcessor

class AddUserInfoProcessor(AbstractProcessor):
    def execute(self, data: Data)-> Data:
        try:
            # Get user information
            info_sheet_name="0. Background&Objectives"
            info_sheet = data.pop(info_sheet_name)
            user_data = {}
            user_data.update({"name": info_sheet.get_record(0)[1].split(":")[1].strip()})
            user_data.update({"id":info_sheet.get_record(0)[2].split(":")[1].strip()})
            user_data.update({"department":info_sheet.get_record(0)[3].split(":")[1].strip()})
            user_data.update({"university":info_sheet.get_record(1)[1].split(":")[1].strip()})
    #        user_data.update({"year_of_graduation":int(info_sheet.get_record(1)[2].split(":")[1].strip())})
            user_data.update({"major":info_sheet.get_record(1)[3].split(":")[1].strip()})

            for sheet in data.sheets:
                insert_data = {**user_data, **{"category":sheet.name}}
                sheet.buck_insert(insert_data)

            return data
        except Exception as e:
            print(e)
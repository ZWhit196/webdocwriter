# http://xlsxwriter.readthedocs.io/getting_started.html
# http://xlsxwriter.readthedocs.io/working_with_pandas.html
# http://pbpython.com/improve-pandas-excel-output.html <== Helpful stuff

import pandas as pd
import xlsxwriter

class ExcelBase:
    book_name = "Workbook"
    workbook = None
    sheets = []

    def __init__(self, fname=None, sname=None, username=None):
        if fname is not None:
            self.book_name = fname
        self.file_path = "./docs/{}/excel/".format(username)
        self.workbook = xlsxwriter.Workbook("{}.xlsx".format(self.book_name))
        self.Add_sheet(sname)

    def __repr__(self):
        return "<XLSX writer base>"

    def Workbook_name(self):
        return self.book_name

    def Add_sheet(self, sheet_name=None):
        if sheet_name is None:
            sheet_name = "Sheet{}".format(len(self.sheets))
        self.sheets.append(self.workbook.add_worksheet(sheet_name))

    def Finish(self):
        self.workbook.close()


class ExcelWriter(ExcelBase):
    json_content = None

    def _loadJson(self, json_name=None, raw=None):
        if raw is None:
            print(json_name)

    def Array_to_frame(self, data):
        print(data)
        cols = [x for x in range(len(data))]
        DF = pd.DataFrame(columns=cols, data=data)
        print(DF)
        # print(self.file_path,self.Workbook_name())
        # DF.to_excel(self.file_path+self.Workbook_name(),engine=pd.ExcelWriter(self.file_path+self.Workbook_name()))


# ==============================================
if __name__ == "__main__":
    eb = ExcelWriter("ATestBook", "first")

    json_stuff = {"ATestBook": [ {"first": [ [ "Content:", {'Nothing here': ['bold']} ] ]} ] }

    eb.Finish()  # Must use .Finish() or errors arise

import xlrd
import xlwt
import csv


class CSV:
    @staticmethod
    def get_data(file_name):
        with open(file_name) as f:
            try:
                data = csv.reader(f)
                hdr = next(data)
                col_num = len(hdr)

                arr = []
                for row in data:
                    kv = {}
                    for col in range(col_num):
                        kv[hdr[col]] = row[col]
                    arr.append(kv)
                return arr
            except Exception as e:
                print(e)
                return []

            
class ExcelWriter:
    def __init__(self, name):
        self.workbook = xlwt.Workbook()
        self.name = name
        self.sheet = self.workbook.add_sheet('sheet')

    def put_data(self, arr):
        for idx, key in enumerate(arr[0]):
            self.sheet.write(0, idx, key)
        for idx, item in enumerate(arr):
            for jdx, key in enumerate(item):
                self.sheet.write(idx + 1, jdx, item[key])
        self.workbook.save(self.name)


class ExcelReader:
    def __init__(self, name):
        self.workbook = xlrd.open_workbook(name)
        self.name = name
        self.sheet = self.workbook.sheet_by_index(0)

    def get_data(self):
        arr, keys = [], []
        for idx in range(self.sheet.ncols):
            keys.append(self.sheet.cell(0, idx).value)
        for idx in range(1, self.sheet.nrows):
            data = dict()
            for jdx in range(self.sheet.ncols):
                data[keys[jdx]] = self.sheet.cell(idx, jdx).value
            arr.append(data)
        return arr


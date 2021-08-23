import xlrd
import xlwt


class ExcelWriter:
    def __init__(self, name):
        self.workbook = xlwt.Workbook()
        self.name = name
        self.sheet = self.workbook.add_sheet(self.name)

    def put_data(self, arr):
        for idx, key in enumerate(arr[0]):
            self.sheet.write(0, idx, key)
        for idx, item in enumerate(arr):
            for jdx, key in enumerate(item):
                self.sheet.write(idx + 1, jdx, item[key])
        self.workbook.save(self.name)


class ExeclReader:
    def __init__(self, name):
        self.workbook = xlrd.open_workbook(name)
        self.name = name
        self.sheet = self.workbook.sheet_by_index(0)
        self.col_num = self.sheet.ncols
        self.row_num = self.sheet.nrows

    def get_data(self):
        arr, keys = [], []
        for idx in range(self.col_num):
            keys.append(self.sheet.cell(0, idx))
        for idx in range(1, self.row_num):
            data = dict()
            for jdx in range(self.col_num):
                data[keys[jdx]] = self.sheet.cell(idx, jdx)
            arr.append(data)
        return arr


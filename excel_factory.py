import os
import xlrd
import uuid
from logger import log


class ExcelFactory(object):
    """docstring for ExcelFactory"""

    _instance = {}

    def __new__(cls, *args, **kw):
        if not cls._instance.get(cls):
            cls._instance[cls] = super().__new__(cls)
        return cls._instance[cls]

    def __init__(self, files):
        self.excels = {}
        self.files = []

        for i, file in enumerate(files):
            # _ = str(uuid.uuid5(uuid.NAMESPACE_DNS, os.path.basename(i)))
            _ = os.path.basename(file)
            self.excels[_] = xlrd.open_workbook(file)
            self.files.append(_)

    # 检查文件是否存在
    def check_file_exist(self, files: list):
        for i, j in enumerate(files):
            if not os.path.exists(j):
                log.error(f"{j} not exists!")
                files.pop(i)

    def get_data(self, file_no, sheet_no, d_no, start=0, end=None, row=True):
        tb = self.excels[file_no].sheets()[sheet_no]
        data = tb.row_values(d_no) if row else tb.col_values(d_no)

        if end:
            return data[start: end]
        return data

    def get_row_data(self, file_no, sheet_no, row_no, start=0, end=None):
        return self.get_data(file_no, sheet_no, row_no, start, end, True)

    def get_col_data(self, file_no, sheet_no, col_no, start=0, end=None):
        return self.get_data(file_no, sheet_no, col_no, start, end, False)

    def sum(self, file):
        res = {}
        for sheet in self.excels[file].sheets():
            _ = {}
            for i in range(sheet.ncols):
                vals = sheet.col_values(i)
                k = vals.pop(0)
                v = [i if isinstance(i, (float, int)) else 0 for i in vals]
                _[k] = {
                    "total": sum(v),
                    "avf": sum(v)/len(v),
                    "min": min(v),
                    "max": max(v),
                }
            res[sheet.name] = _

        log.info(f"sum's data: {res}")
        return res

    def run(self):
        pass


def test(list_):
    pass


if __name__ == '__main__':
    pass

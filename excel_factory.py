import os
import xlrd
from logger import log


class ExcelFactory(object):
    """docstring for ExcelFactory"""

    def __init__(self, files: list):
        self.excels = dict()
        self.check_file_exist(files)

        for i, file in enumerate(files):
            self.excels[i] = xlrd.open_workbook(file)

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

    def run(self):
        pass


def test(list_):
    pass


if __name__ == '__main__':
    pass

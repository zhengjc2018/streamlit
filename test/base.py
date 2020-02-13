import os
import sys
import unittest

if not __package__:
    from pathlib import Path
    current_path = Path(__file__).resolve()
    lib_base = current_path.parents[1]
    print(lib_base)
    sys.path.append(str(lib_base))

from excel_factory import ExcelFactory
from logger import log


class TestCase(unittest.TestCase):

    def setUp(self):
        files = []
        names = ["test"]
        current_path = os.getcwd()

        for i in names:
            files.append(os.path.join(current_path, "%s.xlsx" % i))
        self.ex = ExcelFactory(files)

    def tearDown(self):
        pass

    def test_excel_function(self):
        col_data = self.ex.get_col_data(0, 1, 2)
        row_data = self.ex.get_row_data(0, 1, 2)

        assert col_data == ['成绩', 87.0, 89.0, 81.0, 90.0]
        assert row_data == ['bbbb', 13.0, 89.0, '跳啊']


if __name__ == '__main__':
    unittest.main()

from collections import Counter
from csv import DictReader
import numpy as np
import fxs

def toMat(input, output, rows_title, cols_title, val_title, none_val):
    def to_dict_with_i(set):
        """
        Convert set to dict with set values as keys and indexes as values.

        :param set: set with keys
        :return: dict with set values as keys and indexes as values
        """
        dct = dict()
        for i, id in enumerate(set):
            dct[id] = i
        return dct
    DELIMITER = ";"
    reader = DictReader(open(input, "rt"),delimiter=DELIMITER)

    row_names = set()
    col_names = set()

    cs = Counter()

    for row in reader:
        cs[row[cols_title]] += 1
        row_names.add(row[rows_title])
        col_names.add(row[cols_title])

    row_is = to_dict_with_i(row_names)
    col_is = to_dict_with_i(col_names)

    mat = [(len(col_is)+1) * [None] for _ in range(len(row_is))]

    # titles = [None] * len(row_names)
    # row_names = fxs.loadMovies()

    for row in DictReader(open(input, "rt"), delimiter=DELIMITER):
        row_name = row[rows_title]
        iCol = col_is[row[cols_title]]
        iRow = row_is[row_name]
        mat[iRow][iCol+1] = row[val_title]

    for row, i in row_is.items():
        mat[i][0] = row
    fxs.write(output,mat,none_val, [rows_title]+["izb" + str(i) for i in range(len(col_is))])

toMat("normalizirani_izbirci.csv","mat_sole_izbirci.csv","sola","izbirni_predmet", "odstotek_ucencev_iz_sole",0)
import xlrd
import xlwt
import os
import re

"""
pl5	    PL5(1)pl10(2)pl5(2)pl50(1)
pl10	PL5(1)pl15(3)pl5(2)pl20(2)pl10(1)
pl500	PL5(1)pl10(2)pl20(2)pl50(1)PL5(3)

"""
path = r'C:\Users\49942\Desktop\pl_test.xlsx'
readbook = xlrd.open_workbook(path)
print(readbook)
shell = readbook.sheet_by_index(0)
print(shell)
cell11 = shell.cell(0, 1)
print(cell11)
print(cell11.value)
cell_1 = shell.cell(1, 0).value
cell_2 = shell.cell(1, 1).value


def computes(cell_1, cell_2):
    sum_dic = {}
    print(cell_1)
    print(cell_2)
    cell_1 = cell_1.strip().lower()
    cell_2 = cell_2.strip()
    split_list = cell_2.split(')')
    for i in split_list:
        try:
            k, v = i.split('(')
        except ValueError:
            continue
        key = k.strip().lower()
        val = int(v.strip())

        try:
            sum_dic[key] = sum_dic[key] + val
        except KeyError:
            sum_dic[key] = val

    total = sum(sum_dic.values())
    print(cell_1, cell_2, sum_dic[cell_1])
    result = sum_dic[cell_1] / total

    print(total)
    print(result)
    return result


computes(cell_1,cell_2)



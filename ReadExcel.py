# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 08:27:35 2018

@author: 长风振林
"""

import xlrd


def read(file,sheet_index=0):
    workbook = xlrd.open_workbook("E:/皓首穷经/大四下/竞赛/京东/车辆智能调度-A榜/input_node.xlsx")
    # all_sheets_list = workbook.sheet_names()
    # print("本文件中所有的工作表名称:", all_sheets_list)
    # 按索引读取工作表
    sheet = workbook.sheet_by_index(sheet_index)
    print("工作表名称:", sheet.name)
    print("行数:", sheet.nrows)
    print("列数:", sheet.ncols)

    # 按工作表名称读取数据
    # second_sheet = workbook.sheet_by_name("b")
    # print("Second sheet Rows:", second_sheet.nrows)
    # print("Second sheet Cols:", second_sheet.ncols)
    # 获取单元格的数据
    # cell_value = sheet.cell(1, 0).value
    # print("获取第2行第1列的单元格数据:", cell_value)
    data = []
    for i in range(0, sheet.nrows):
        data.append(sheet.row_values(i))
    return data


if __name__ == '__main__':
    #read函数里面的东西暂时没用
    print(read('随便起个名.xlsx'))
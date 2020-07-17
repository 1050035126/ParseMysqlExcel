# -*- coding: utf-8 -*-
"""
@Software: PyCharm
@Author :张鹏
@Email  :1050035126@qq.com
@Date   :2020/07/08/0008 16:51
@Version:1.0
@Desc   :
解析excel mysql表的结构定义
 输出mysql的插创建数据表的sql语句

"""
import xlrd


def processTableFormat(excelPath):
    resultDic = {}
    tempTableName = ""
    tempTableExplain = ""
    tempColList = []
    # 读取excel中的表结构
    workbook = xlrd.open_workbook(excelPath)
    sheet = workbook.sheet_by_index(0)
    rowLen = sheet.nrows  # 总行数
    for i in range(rowLen):

        rowData = sheet.row_values(i)  # i行的list

        temp = rowData[0]
        if temp == "序号":
            continue
        if temp == "表名" or temp == "":
            if tempTableName != "":
                resultDic[tempTableName] = {
                    "tableExplain": tempTableExplain,
                    "colList": tempColList.copy()
                }

            tempTableName = rowData[1]
            tempTableExplain = rowData[3]
            tempColList.clear()
            continue

        colIndex = rowData[0]
        name = rowData[1]
        comment = rowData[2].replace(" ", "")
        dataType = rowData[3]
        dataLen = rowData[4]
        allowNullStr = rowData[5]

        if allowNullStr in ["", "√"]:
            allowNull = ""
        elif allowNullStr == "自动递增":
            allowNull = "自动递增"
        else:
            allowNull = "NOT NULL"

        tempColList.append([name, comment, dataType, dataLen, allowNull])

    if len(tempColList) != 0:
        resultDic[tempTableName] = {
            "tableExplain": tempTableExplain,
            "colList": tempColList.copy()
        }

    return resultDic


def outCreateTableSql(tableFormatDic):
    tableNameList = tableFormatDic.keys()

    for tableName in tableNameList:
        tableContent = tableFormatDic.get(tableName)
        colList = tableContent.get("colList")
        tableExplain = tableContent.get("tableExplain")

        print("\n")
        print(f"CREATE TABLE `{tableName}` (")
        # [name, comment, dataType, dataLen, allowNull]
        primaryKeySet = ""

        colSize = len(colList)
        tempSqlItemList = []
        for colIndex in range(colSize):
            col = colList[colIndex]

            name = col[0]
            comment = col[1]
            dataType = col[2]
            dataLen = col[3]
            allowNull = col[4]
            defaultNull = "DEFAULT NULL"
            if dataType == "datetime":
                dataLen = ""
            # 是否允许为空
            if allowNull:
                if allowNull == "自动递增":
                    allowNull = " NOT NULL AUTO_INCREMENT "
                else:
                    allowNull = f"{allowNull}"
            else:
                allowNull = ""
            # 添加数据长度定义
            if dataLen != "":
                dataLen = int(dataLen)
                dataLen = f"({dataLen})"

            if "主键" in comment:
                primaryKeySet = name

            # 对于主键和不允许空的 不设定默认值null
            if "主键" in comment or allowNull != "":
                defaultNull = ""

            tempSqlItemList.append(f"`{name}` {dataType}{dataLen} {allowNull} COMMENT '{comment}' {defaultNull} ")

        if primaryKeySet != "":
            tempSqlItemList.append(f"PRIMARY KEY (`{primaryKeySet}`)")

        print(",\n".join(tempSqlItemList))
        print(f") COMMENT='{tableExplain}' ENGINE=InnoDB DEFAULT CHARSET=utf8;")


if __name__ == '__main__':
    excelPath = r"excelMysql.xlsx"

    tableFormatDic = processTableFormat(excelPath)

    outCreateTableSql(tableFormatDic)

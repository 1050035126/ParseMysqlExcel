# ParseMysqlExcel
# 运行环境 
1. python3.6
2. 所需python库:  
   i. python-docx 

# 说明
解析word或excel中的mysql的表结构定义，输出sql语句  
包含两种方式  
1.在word中定义  
（需要表名和表格一一对应，第一行：表名：tableName   ；第二行：字段表格）  
  参考：[wordMysql.docx](wordMysql.docx)  
2.在excel中定义  
  参考： [excelMysql.xlsx](/excelMysql.xlsx)

# 1. word表定义mysql结构
## 格式：位于sheet1，竖排显示 
(1) 第一个表格声明表名以及对应的注释  
| 序号 | 表名 | 备注 |
| ---- | ------ | ------ |
| 1 |	test_table | 测试表1 |
| 2 |	test_table2 | 测试表2 |

(2) 表名：test_table_name  声明表名，以（表名：）起始  
(3) 表格声明，test_table_name对应的表结构

表名：test_table2
| 序号 | 字段名称 | 字段描述 | 字段类型 | 长度| 允许空 |
| ---- | ------ | ------ | ---- | ------ | ------ |
| 1 |	id | 主键 | varchar | 64 | 自动递增 |
| 2 |	file_type | 文件类型 | varchar | 10 | 必填 |
| 3 |	start_time | 开始时间 | datetime |   | √ |
| 4 |	end_time | 结束时间 | datetime |  |  |
| 5 |	interval | 时间间隔 | float |   |  |


## 输出示例
```
CREATE TABLE `test_table2` (
`id` varchar(64) NOT NULL AUTO_INCREMENT COMMENT '主键'  ,
`file_type` varchar(10) NOT NULL  COMMENT '文件类型' DEFAULT NULL ,
`start_time` datetime  COMMENT '开始时间' DEFAULT NULL ,
`end_time` datetime  COMMENT '结束时间' DEFAULT NULL ,
`interval` float  COMMENT '时间间隔' DEFAULT NULL ,
PRIMARY KEY (`id`)
) COMMENT='测试表2' ENGINE=InnoDB DEFAULT CHARSET=utf8;
```


# 2. excel表定义mysql结构
## 格式：位于sheet1，竖排显示

| 表名 | test_table22 | 表注释 | 测试表22 |   |  |
| ---- | ------ | ------ | ---- | ------ | ------ |
| 序号 | 字段名称 | 字段描述 | 字段类型 | 长度| 允许空 |
| 1 |	id | 主键 | varchar | 64 | 必填 |
| 2 |	file_type | 文件类型 | varchar | 10 |
| 3 |	start_time | 开始时间 | datetime |   |
| 4 |	end_time | 结束时间 | datetime |   |
| 5 |	interval | 时间间隔 | float |   |


## 输出示例
```
CREATE TABLE `test_table22` (
`id` varchar(64) NOT NULL COMMENT '主键'  ,
`file_type` varchar(10)  COMMENT '文件类型' DEFAULT NULL ,
`start_time` datetime  COMMENT '开始时间' DEFAULT NULL ,
`end_time` datetime  COMMENT '结束时间' DEFAULT NULL ,
`interval` float  COMMENT '时间间隔' DEFAULT NULL ,
PRIMARY KEY (`id`)
) COMMENT='测试表22' ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

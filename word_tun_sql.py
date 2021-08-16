from docx import Document  # 导入库

"""

编号	字段名	类型	字段意义	备注
1	id	int		
2	name	varchar(64)	管理用户名	唯一，不重复，不能更改
3	password	varchar(64)	管理用户口令	
4	last_time	datetime	登录时间	
5	last_ip	varchar(64)	登录ip	
6	times	int(11)	登录次数	
7	created_at	datetime	添加时间	时间
8	add_user	varchar(64)	操作人	同users中的name
9	updated_at	datetime	最后更新时间	
10				
备注	super(超级管理员用户信息数据表)

备注列为表名括号的内容为表的备注

请注意 里面的()都为英文字母下的 如果使用中文下的  会导致错误
"""


def generateSql(table):
    primary_key = ''
    table_remarks = ''
    sql = 'CREATE TABLE `<table_name>`('
    for i in range(1, len(table.rows)):  # 从表格第二行开始循环读取表格数据

        filed_name = table.cell(i, 1).text
        limit = table.cell(i, 2).text
        remarks = table.cell(i, 3).text

        if (filed_name == ""):
            continue
        # 如果是最后一行 最好一行是表名
        if (i == len(table.rows) - 1):
            split = str(filed_name).split('(')
            table_name = split[0]
            if (len(split) > 1):
                table_remarks = split[1].replace(')', '').replace('）', '')
            sql = sql.replace('<table_name>', table_name.replace(" ", ""))
            continue

        if (filed_name == 'id'):
            sql += "`{}` {} COMMENT '{}' AUTO_INCREMENT,".format(filed_name, limit, remarks)
            primary_key = filed_name

        else:
            sql += "`{}` {} COMMENT '{}' ,".format(filed_name, limit, remarks)

    sql += ' PRIMARY KEY (`{}` ))'.format(primary_key)
    if (table_remarks != ''):
        sql += "COMMENT='{}';".format(table_remarks)
    return sql


def getSql(path):
    sql_list = []
    document = Document(path)  # 读入文件
    tables = document.tables  # 获取文件中的表格集
    for table in tables:
        sql = generateSql(table)
        sql_list.append(sql)
        # table = tables[21]  # 获取文件中的第一个表格
        # sql = generateSql(table)
        # print(sql)
    return sql_list


sqls = getSql(path="Z:\\工作\\erp\\企业资源计划信息系统数据库设计文档.docx")
for sql in sqls:
    print(sql)

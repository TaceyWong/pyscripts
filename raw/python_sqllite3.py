__author__ = 'Administrator'
#coding:utf-8

#Step 1:导入Python SQLLITE模块
import sqlite3

print "导入sqllite3成功"

#Step 2:创建/打开数据库
cx = sqlite3.connect("test.db")
print "打开数据库"
# 创建在内存中
# con = sqlite3.connect(":memory")

#Step 3:数据库连接对象
"""
    打开数据库时返回的对象cx是一个数据库连接对象，他可以有以下操作
    ①commit()——事务提交
    ②rollback()——食事务回滚
    ③close()——关闭一个数据库连接
    ④cursor()——创建一个游标

    关于commit()，如果isolation_level隔离级别默认，那么每次对数据库的操作都余姚使用该命令
    若设置isolation_level = None,则成为自动提交模式

"""

#Step 4:使用游标查询数据库

cu = cx.cursor()

print "得到游标"
"""
    使用游标对象SQL语句查询数据库，获得查询对象
    游标对象有以下操作：
    ①execute()——执行SQL语句
    ②executemany()——执行多条语句
    ③close()关闭游标
    ④fetchone()——从结果中取一条记录，并将游标指向下一条记录
    ⑤fetchmany()——从结果中取多条记录
    ⑥fetchall()——从结果中取出所有记录
    ⑦scroll()——游标滚动
"""

# About 1:建表

cu.execute("create table catalog (id integer primary key,pid integer,name varchar(10) UNIQUE,nickname text NULL)")
print "创建表成功"

# About 2：插入数据
"""
    避免以下的写法（避免注入攻击）
    pid = 200
    cx.execute("...where pid = %s" %pid)
"""

for t in [(0,10,'abc','Yu'),(1,20,'cba','Wang')]:
    cx.execute("insert into catalog values(?,?,?,?)",t)

print "插入数据成功"

#注意默认状态需要提交
cx.commit()
print "提交成功"

# About 3:查询

cu.execute("select * from catalog")

print "查询成功"

#要提取查询到的数据，使用游标的fetch函数

print cu.fetchall()

print "提取查询到的数据成功"

# About 4:修改

cu.execute("update catalog set name = 'Boy' where id = 0")
cx.commit()
print "修改成功"

# About 5:删除

cu.execute("delete from catalog where id = 1")
cx.commit()
print "删除成功"

# About 6：使用中文

"""
    保证编辑器、保存、文内编码全部使用utf-8
    并且在中文前加 u
"""

#以下部分出现错误
x = u'王新勇'
cu.execute("update catalog set name = ? where id = 0",x)
cu.execute("select * from catalog")
cu.fetchall()
print "使用中文修改数据成功"
"""
    若要显示中文字体，要依次打印出每个字符串
    for item in cu.fetchall():
        for element in item:
            print element,
        print
"""

# About 7:Row 类型
"""
    Row提供了基于索引和基于名字大小写敏感的方式来访问列而几乎没有内存开销。
"""

""" 尚待完善"""



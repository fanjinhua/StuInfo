import sqlite3
from data_stu import list_stu

conn = sqlite3.connect('database.db')
cur = conn.cursor()
cur.execute('CREATE TABLE temp_stu_info(学号 VARCHAR(8), 姓名 VARCHAR(8), 性别 VARCHAR(8), 专业 VARCHAR(8), 院系 VARCHAR(8))')
#cur.execute('INSERT INTO stuinfo VALUES("2011212376", "麻才来", "男", "生物医学工程", "生物信息学院")')

for i in range(len(list_stu)):
    cur.execute('INSERT INTO temp_stu_info VALUES("%s", "%s", "%s", "%s", "%s")' % (list_stu[i].num,
                list_stu[i].name, list_stu[i].sex, list_stu[i].zy, list_stu[i].xy))

# delete duplicate
cur.execute('CREATE TABLE stu_info(学号 VARCHAR(8), 姓名 VARCHAR(8), 性别 VARCHAR(8), 专业 VARCHAR(8), 院系 VARCHAR(8))')
cur.execute('INSERT INTO stu_info SELECT DISTINCT * FROM temp_stu_info')
cur.execute('DROP TABLE temp_stu_info')

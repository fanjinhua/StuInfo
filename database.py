import sqlite3
from data_stu import list_stu

conn = sqlite3.connect('database.db')
cur = conn.cursor()
cur.execute('CREATE TABLE stu_info(学号 VARCHAR(8), 姓名 VARCHAR(8), 性别 VARCHAR(8), 专业 VARCHAR(8),'
            ' 院系 VARCHAR(8))')
#cur.execute('INSERT INTO stu_info VALUES("2011212376", "麻才来", "男", "生物医学工程", "生物信息学院")')

for i in range(len(list_stu)):
    cur.execute('INSERT INTO stu_info (学号, 姓名, 性别, 专业, 院系) VALUES (?, ?, ?, ?, ?)',
                (list_stu[i].num, list_stu[i].name, list_stu[i].sex, list_stu[i].zy, list_stu[i].xy))

# pic_url = 'http://jwzx.cqupt.edu.cn/showstuPic.php?xh='
# for i in range(len(list_stu)):
#     cur.execute('UPDATE stu_info SET 照片=? WHERE 学号=?',
#                 ( sqlite3.Binary(requests.get(pic_url + list_stu[i].num).content) ,
#                   list_stu[i].num))
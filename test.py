# class Stu:
#     def __init__(self, num, name, sex, zy, xy):
#         self.num = num
#         self.name = name
#         self.sex = sex
#         self.zy = zy
#         self.xy = xy
#
# list_stu = []
#
# stu = Stu('2015210177', '夏宇', '男', '通信与信息类', '通信与信息工程学院')
# list_stu.append(stu)
#
# stu2 = Stu('2015210178', '鲁森', '男', '通信与信息类', '通信与信息工程学院')
# list_stu.append(stu2)
#
#
# list_stu.append(Stu('2015210179', '方法森', '男', '通信与信息类', '通信与信息工程学院'))
# print(list_stu[0].num)
# print(list_stu[1].num)
# print(list_stu[2].num)

from urllib.request import urlopen
from bs4 import BeautifulSoup
from data_stu import class_links

url = 'http://jwzx.cqupt.edu.cn/'


html2 = urlopen(url + class_links[0])           # gb18030
print(class_links[0])
ins = BeautifulSoup(html2.read(), 'html.parser',
                      from_encoding="gb18030").find('tr', onmouseover="this.bgColor='#E3E3E3';")
print(ins)  # error

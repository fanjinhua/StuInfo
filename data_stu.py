#coding = utf-8
from urllib.request import urlopen
from bs4 import BeautifulSoup
import os.path as pt
import os
import html5lib

class_links = []
zyh = ['0601', '0602', '0604', '0605', '0611', '0101', '0102', '0104', '0114', '0115', '0190', '0191',
       '0192', '5101', '5102', '6101', '0401', '0402', '0403', '0405', '0406', '0412', '0491', '0492',
       '5301', '5302', '5303', '6401', '0801', '0802', '0803', '0805', '0806', '0812', '0818', '0890',
       '5201', '5202', '1201', '1202','1204', '1205', '1207', '1208', '1211', '1212', '1290']
url = 'http://jwzx.cqupt.edu.cn/'

for each_zyh in zyh:
    html = urlopen(url + 'pubBjStu.php?zyh=' + each_zyh)
    bsObj = BeautifulSoup(html.read(), 'html5lib')
    links = bsObj.find_all('a', target='_blank')

    for link in links:
        class_links.append(link['href'])

stu_info = []

for class_link in class_links:
    html2 = urlopen(url + class_link)           # gb18030
    infos = BeautifulSoup(html2.read(), 'html5lib',
                          from_encoding="gb18030").find_all('tr', onmouseover="this.bgColor='#E3E3E3';")

    for info in infos:
        stu_info.append(info.get_text())


class Stu:
    def __init__(self, num, name, sex, zy, xy):
        self.num = num
        self.name = name
        self.sex = sex
        self.zy = zy
        self.xy = xy

list_stu = []
dict_pic = {}

for each_info in stu_info:
    ls = each_info.split()
    # print(ls)
    for i in range(0, len(ls), 5):
        list_stu.append(Stu(ls[i], ls[i+1], ls[i+2], ls[i+3], ls[i+4]))

for i in range(len(list_stu)):
    file_name = list_stu[i].num + '.jpg'
    os.mkdir("pic")
    #os.chdir("pic")
    file_directory = "pic\\" + file_name
    file = open(file_directory, 'wb')
    file.write(urlopen('http://jwzx.cqupt.edu.cn/showstuPic.php?xh=' + list_stu[i].num).read())
    file.close()
    #dict_pic[list_stu[i].num] = 'http://jwzx.cqupt.edu.cn/showstuPic.php?xh=' + list_stu[i].num


print(len(list_stu))


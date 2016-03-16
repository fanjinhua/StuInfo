from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageTk
from database import *
from urllib.request import urlopen
import io
from data_stu import dict_pic

root = Tk()
root.geometry('300x280')
root.title('Database Modifier')

fra = Frame(root, height=6, width=280)
fra.pack()

#text = Text(fra, height=10, width=16)

label = Label(fra, height=10, width=16)

def change(url_pic):
    image_bytes = urlopen('http://jwzx.cqupt.edu.cn/showstuPic.php?xh=' + url_pic).read()
    data_stream = io.BytesIO(image_bytes)
    image = Image.open(data_stream)
    #缩放图片
    image.thumbnail((130, 150))
    pic = ImageTk.PhotoImage(image)
    label.configure(image=pic)

label.pack(side=LEFT)

# image = Image.open(data_stream)
#
# #缩放图片
# image.thumbnail((130, 150))
# pic = ImageTk.PhotoImage(image)
# text.insert(END, '\n')
# text.image_create(END, image=pic)
# text.pack(side=LEFT)

frame = Frame(fra, height=6, width=280)
frame.pack(side=RIGHT)

Label(frame, text="学号 ").grid(row=0)
Label(frame, text="姓名 ").grid(row=1)
Label(frame, text="性别 ").grid(row=2)
Label(frame, text="专业 ").grid(row=3)
Label(frame, text="院系 ").grid(row=4)

num = StringVar()
name = StringVar()
sex = StringVar()
zy = StringVar()
xy = StringVar()

e1 = Entry(frame, textvariable=num)
e2 = Entry(frame, textvariable=name)
e3 = Entry(frame, textvariable=sex)
e4 = Entry(frame, textvariable=zy)
e5 = Entry(frame, textvariable=xy)

e1.grid(row=0, column=2)
e2.grid(row=1, column=2)
e3.grid(row=2, column=2)
e4.grid(row=3, column=2)
e5.grid(row=4, column=2)

def insert():
    print(e1.get(), e2.get(), e3.get(), e4.get(), e5.get())
    try:
        with cur:
            cur.execute('INSERT INTO stu_info VALUES(?, ?, ?, ?, ?)',
                        (e1.get(), e2.get(), e3.get(), e4.get(), e5.get()))
    except sqlite3.IntegrityError:
        print("Couldn't add the same one twice!")

def delete():
    messagebox.showinfo("Warnning!", "Are you sure to delete this info?")
    cur.execute('DELETE FROM stu_info WHERE 学号=?', [e1.get()])

def find():
    cur.execute('SELECT * FROM stu_info WHERE 学号=?', [e1.get()])
    value = cur.fetchall()
    print(value)
    num.set(value[0][0])
    name.set(value[0][1])
    sex.set(value[0][2])
    zy.set(value[0][3])
    xy.set(value[0][4])

    change(value[0][0])

def clear():
    num.set('')
    name.set('')
    sex.set('')
    zy.set('')
    xy.set('')

def save():
    cur.execute('UPDATE stu_info SET 姓名=?, 性别=?, 专业=?, 院系=? WHERE 学号=?',
                [e2.get(), e3.get(), e4.get(), e5.get(), e1.get()])


insert_button = Button(root, text='Insert', activeforeground='white', activebackground='green', command=insert)
delete_button = Button(root, text='Delete', activeforeground='white', activebackground='red', fg='red', command=delete)
find_button = Button(root, text='Find', activeforeground='white', activebackground='green', command=find)
save_button = Button(root, text='Save', activeforeground='white', activebackground='green', command=save)
clear_button = Button(root, text='Clear', activeforeground='white', activebackground='green', command=clear)

insert_button.pack(fill=X, expand=True)
delete_button.pack(fill=X, expand=True)
find_button.pack(fill=X, expand=True)
save_button.pack(fill=X, expand=True)
clear_button.pack(fill=X, expand=True)

root.mainloop()

cur.close()
conn.commit()
conn.close()
from tkinter import *
from database import *

root = Tk()
root.geometry('300x250')
root.title('Database Modifier')

frame = Frame(root, height=6, width=280)
frame.pack()
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

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
e5.grid(row=4, column=1)

def insert():
    print(e1.get(), e2.get(), e3.get(), e4.get(), e5.get())
    cur.execute('INSERT INTO stu_info VALUES("%s", "%s", "%s", "%s", "%s"' %
                (e1.get(), e2.get(), e3.get(), e4.get(), e5.get()))

def delete():
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

def clear():
    num.set('')
    name.set('')
    sex.set('')
    zy.set('')
    xy.set('')

#def save():
 #   cur.execute('')

#text = Text(root, height=6, width=430)

#text.insert(INSERT, "每行分别键入学号，姓名，性别，专业，院系：")

#text.pack()

insert_button = Button(root, text='Insert', activeforeground='white', activebackground='green', command=insert)
delete_button = Button(root, text='Delete', activeforeground='white', activebackground='red', fg='red')
find_button = Button(root, text='Find', activeforeground='white', activebackground='green', command=find)
save_button = Button(root, text='Save', activeforeground='white', activebackground='green')
clear_button = Button(root, text='Clear', activeforeground='white', activebackground='green', command=clear)
#insert_button.bind("<Button-1>")
insert_button.pack(fill=X, expand=True)
delete_button.pack(fill=X, expand=True)
find_button.pack(fill=X, expand=True)
save_button.pack(fill=X, expand=True)
clear_button.pack(fill=X, expand=True)

mainloop()

cur.close()
conn.commit()
conn.close()
import tkinter as tk
from tkinter import ttk
import pymysql as mq
from tkinter import messagebox





root = tk.Tk()
root.geometry("1370x700")
root.title("Student Management System")

title_label=tk.Label(root,text='Student Management System', font=('Aerial',30,'bold'),border=12,relief=tk.GROOVE,foreground='black')
title_label.pack(side=tk.TOP,fill=tk.X)

detail_frame = tk.LabelFrame(root,text='Enter Details',font=('Aerial',25),fg='black',bd=12,relief=tk.GROOVE)
detail_frame.place(x=20,y=105,width=500,height=560)

data_frame =tk.LabelFrame(root,fg='black',relief=tk.GROOVE,border=12)
data_frame.place(x=530,y=110,width=800,height=560)

name_var = tk.StringVar()
roll_var = tk.StringVar()
father_var = tk.StringVar()
contact_var = tk.StringVar()
gender_var = tk.StringVar()
class_var = tk.StringVar()
search_var = tk.StringVar()

def fetch_data():
    conn = mq.connect(host="localhost",user= 'root',password='',database='student')
    curr = conn.cursor()
    curr.execute('select * from data')
    rows = curr.fetchall()
    if len(rows)!=0:
        student_table.delete(*student_table.get_children())
        for row in rows:
            student_table.insert('',tk.END,values=row)
        conn.commit()
    conn.close()


def add():
    if name_var.get()==""or roll_var.get()=="" or class_var.get()=="":
        messagebox.showerror("Error","Please fill alla the fields!")
    else:
        conn = mq.connect(host='localhost',user='root',password='',database='student')
        curr=conn.cursor()
        curr.execute("INSERT INTO data VALUES (%s,%s,%s,%s,%s,%s)",(name_var.get(),roll_var.get(),class_var.get(),gender_var.get(),contact_var.get(),father_var.get()))
        conn.commit()
        conn.close()
        fetch_data()
def get_cursor(event):
    cursor_row = student_table.focus()
    content=student_table.item(cursor_row)
    row = content['values']
    name_var.set(row[0])
    roll_var.set(row[1])
    father_var.set(row[5])
    contact_var.set(row[4])
    gender_var.set(row[3])
    class_var.set(row[2])

def clear():
    name_var.set("")
    roll_var.set("")
    father_var.set("")
    contact_var.set("")
    gender_var.set("")
    class_var.set("")

def update():
    conn = mq.connect(host="localhost",user='root',password='',database='student')
    curr = conn.cursor()
    curr.execute("update data set name=%s,class=%s,gender=%s,contact=%s,father_name=%s where roll_no=%s",(name_var.get(),class_var.get(),gender_var.get(),contact_var.get(),father_var.get(),roll_var.get()))
    conn.commit()
    fetch_data()
    conn.close()
    clear()

def delete():
    conn = mq.connect(host="localhost", user='root', password='', database='student')
    curr = conn.cursor()
    curr.execute("DELETE FROM data where roll_no=%s",roll_var.get())
    conn.commit()
    fetch_data()
    conn.close()
    clear()

name = tk.Label(detail_frame,text='Name',bd=7,font=('Aerial',17))
name.grid(row=0,column=0,padx=2,pady=4)
name_entry = tk.Entry(detail_frame,bd=7,font=('Aerial',17),textvariable=name_var)
name_entry.grid(row=0,column=1,padx=2,pady=4)

roll = tk.Label(detail_frame,text='Roll No',bd=7,font=('Aerial',17))
roll.grid(row=1,column=0,padx=2,pady=4)
roll_entry = tk.Entry(detail_frame,bd=7,font=('Aerial',17),textvariable=roll_var)
roll_entry.grid(row=1,column=1,padx=2,pady=4)

class_label = tk.Label(detail_frame,text='Class',bd=7,font=('Aerial',17))
class_label.grid(row=2,column=0,padx=2,pady=4)
class_entry = tk.Entry(detail_frame,bd=7,font=('Aerial',17),textvariable=class_var)
class_entry.grid(row=2,column=1,padx=2,pady=4)

gender = tk.Label(detail_frame,text='Gender',bd=7,font=('Aerial',17))
gender.grid(row=3,column=0,padx=2,pady=4)
gender_entry = tk.Entry(detail_frame,bd=7,font=('Aerial',17),textvariable=gender_var)
gender_entry.grid(row=3,column=1,padx=2,pady=4)

contact = tk.Label(detail_frame,text='Contact',bd=7,font=('Aerial',17))
contact.grid(row=4,column=0,padx=2,pady=4)
contact_entry = tk.Entry(detail_frame,bd=7,font=('Aerial',17),textvariable=contact_var)
contact_entry.grid(row=4,column=1,padx=2,pady=4)

father = tk.Label(detail_frame,text="Father's Name",bd=7,font=('Aerial',17))
father.grid(row=5,column=0,padx=2,pady=4)
father_entry = tk.Entry(detail_frame,bd=7,font=('Aerial',17),textvariable=father_var)
father_entry.grid(row=5,column=1,padx=2,pady=4)


crud_frame = tk.LabelFrame(detail_frame,relief=tk.GROOVE,border=12)
crud_frame.place(x=15,y=320,width=430,height=160)

add_button = tk.Button(crud_frame,text='Add',bd=7,font=('Aerial',12),width=18,command=add)
add_button.grid(row=0,column=0,padx=5,pady=5)

update_button = tk.Button(crud_frame,text='Update',bd=7,font=('Aerial',12),width=18,command=update)
update_button.grid(row=0,column=1,padx=5,pady=5)

delete_button = tk.Button(crud_frame,text='Delete',bd=7,font=('Aerial',12),width=18,command=delete)
delete_button.grid(row=1,column=0,padx=5,pady=5)

clear_button = tk.Button(crud_frame,text='Clear',bd=7,font=('Aerial',12),width=18,command=clear)
clear_button.grid(row=1,column=1,padx=5,pady=5)

search_frame = tk.LabelFrame(data_frame,bd=12,relief=tk.GROOVE)
search_frame.place(x=20,y=10,width=745,height=80)

search_label = tk.Label(search_frame,text='Search',font=('Aerial',17),fg='black')
search_label.grid(row=0,column=0,padx=2,pady=2)

search_in = ttk.Combobox(search_frame,font=("Aerial",12),state='readonly',textvariable=search_var)
search_in['values']=('Name','Roll No','Contact','Father Name','Class','Gender')
search_in.grid(row=0,column=1,padx=2,pady=2)

search_button = tk.Button(search_frame,text='Search',font=('Aerial',12),fg='black',width=10,bd=7)
search_button.grid(row=0,column=2,padx=20,pady=2)

showall_button = tk.Button(search_frame,text='Show All',font=('Aerial',12),fg='black',width=10,bd=7)
showall_button.grid(row=0,column=3,padx=20,pady=2)

database_frame = tk.LabelFrame(data_frame,font=('Aerial',17),fg='black',bd=12)
database_frame.place(x=15,y=100,width=745,height=420)

main_frame = tk.Frame(database_frame,bd=2,relief=tk.GROOVE)
main_frame.pack(fill=tk.BOTH,expand=True)

y_scroll = tk.Scrollbar(main_frame,orient=tk.VERTICAL)
x_scroll = tk.Scrollbar(main_frame,orient=tk.HORIZONTAL)

student_table = ttk.Treeview(main_frame,columns=('Name','Roll No','Class','Gender','Contact','Father Name'),yscrollcommand=x_scroll.set,xscrollcommand=y_scroll.set)
y_scroll.config(command=student_table.yview)
x_scroll.config(command=student_table.xview)

y_scroll.pack(side=tk.RIGHT,fill=tk.Y)
x_scroll.pack(side=tk.BOTTOM,fill=tk.X)

student_table.heading('Name',text='Name')
student_table.heading('Roll No',text='Roll No')
student_table.heading('Class',text='Class')
student_table.heading('Gender',text='Gender')
student_table.heading('Contact',text='Contact')
student_table.heading("Father Name",text='Father Name')
student_table.pack(fill=tk.BOTH,expand=True)



fetch_data()

student_table.bind("<ButtonRelease-1>",get_cursor)
root.mainloop()



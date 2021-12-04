from tkinter import *
root = Tk()
root.title("Gpa calculator")
p1=PhotoImage(file='images.png')
root.iconphoto(False,p1)
root.configure(bg='pink')
sub=StringVar()
cred=StringVar()
pt=StringVar()
subjects=[]
credits=[]
points=[]

def add():
    subject=sub.get()
    credit=cred.get()
    point=pt.get()
    subjects.append(subject)
    credits.append(int(credit))
    points.append(int(point))
    sub.set("")
    cred.set("")
    pt.set("")
    for x in range(len(subjects)):
        t=f"{subjects[x]}    {credits[x]}    {points[x]} "
        Label(root,text=t,bg='pink').grid(row=2+x,column=0)

def calcgpa():
    m=0
    s=0
    final_l=[]
    for i in range(len(credits)):
        m+=credits[i]
    for i in range(len(credits)):
        final_l.append(credits[i]*points[i])
    for i in final_l:
        s+=i
    Label(root,text="Gpa: %0.2f"%float(s/m),bg='pink',fg='indigo').grid(row=4,column=2)

Label(root,text="Subject",bg='pink',fg='green').grid(row=0,column=0)
Label(root,text="Credit",bg='pink',fg='green').grid(row=0,column=1)
Label(root,text="Point",bg='pink',fg='green').grid(row=0,column=2)
Entry(root,textvariable=sub).grid(row=1,column=0)
Entry(root,textvariable=cred).grid(row=1,column=1)
Entry(root,textvariable=pt).grid(row=1,column=2)
Button(root,text='Add Subject',command=add,fg='red').grid(row=1,column=3)

Button(root,text='Gpa',command=calcgpa,fg='red').grid(row=10,column=1)



root.mainloop()

from tkinter import *

root = Tk()
root.geometry("300x400")

#root.minsize(width=300,height=300)
#root.maxsize(width=300,height=300)

lable = Label(root, text="Name", fg="white", bg="black")
lable.grid(row=0, column=0,pady=10,sticky=W)

e1 = Entry(root)
e1.grid(row=0, column=1)

lable = Label(root, text="User name ", fg="white", bg="black")
lable.grid(row=1, column=0,pady=10,sticky=W)

e1 = Entry(root)
e1.grid(row=1, column=1)

lable = Label(root, text="Password", fg="white", bg="black")
lable.grid(row=2, column=0,pady=10,sticky=W)

e1 = Entry(root)
e1.grid(row=2, column=1)

chk = Checkbutton(root,text="remember me")
chk.grid(row=3,column=1)

btn = Button(root, text="Submit",width=10)
btn.grid(row=4,column=1,pady=20,sticky=W) #Another way
#btn.grid(row=3,column=0,columnspan=2)
root.mainloop()

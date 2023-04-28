from tkinter import *
root=Tk()

def msg():
    l1=Label(root,text="hello")
    l1.pack()

btn=Button(root,text="click",command=msg)
btn.pack()

root.mainloop()
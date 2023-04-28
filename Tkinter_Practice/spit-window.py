from tkinter import *

root=Tk()
root.title("HACKERS")
root.iconbitmap("hacker.ico")
root.geometry("400x300")


m1=PanedWindow(root,relief=SUNKEN,bd=4,bg="pink")
m1.pack(fill=BOTH,expand=1)

l1=Label(m1,text="lest side")
m1.add(l1)

m2=PanedWindow(m1,relief=SUNKEN,bd=4, bg="skyblue",orient=VERTICAL)
m1.add(m2)

l2=Label(m2, text="right top side")
m2.add(l2)
l3=Label(m2,text="right bottom side")
m2.add(l3)

root.mainloop()


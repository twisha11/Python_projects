from tkinter import *
from tkinter import scrolledtext

root = Tk()
root.title("Scrolledtext")
root.geometry("300x300")

s1=scrolledtext.ScrolledText(root,width=40, height=10)
s1.pack()




root.mainloop()

from tkinter import *

root=Tk()
root.geometry("400x400")

topframe = Frame(root)
topframe.pack()

bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM)

leftframe = Frame(root)
leftframe.pack(side=LEFT)

Rightframe = Frame(root)
Rightframe.pack(side=RIGHT)

e1 = Entry(Rightframe)
e1.pack()

e1=Label(topframe,text="top side")
e1.pack()

e1=Entry(leftframe)
e1.pack()

btn=Button(bottomframe, text="submit")
btn.pack()


root.mainloop()

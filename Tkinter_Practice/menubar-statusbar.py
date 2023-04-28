from tkinter import *

root=Tk()
root.geometry("500x400")

#main menu create
m1=Menu(root)
root.config(menu=m1)

#sub component create
sm1=Menu(m1,tearoff=0)
m1.add_cascade(label="File", menu=sm1)
sm1.add_command(label="Save")
sm1.add_command(label="Open")

sm2=Menu(m1,tearoff=0)
m1.add_cascade(label="Edit", menu=sm2)
sm2.add_command(label="Save as")
sm2.add_command(label="New")

sm3=Menu(m1,tearoff=0)
m1.add_cascade(label="view", menu=sm3)
sm3.add_command(label="Tool")
sm3.add_command(label="Windows")


sm4=Menu(m1,tearoff=0)
m1.add_cascade(label="Navigate",menu=sm4)
sm4.add_command(label="File")
sm4.add_command(label="symbol")

sm5=Menu(m1,tearoff=0)
m1.add_cascade(label="Code",menu=sm5)
sm5.add_command(label="Move")
sm5.add_command(label="Genrate")



#add sub menu
stautsbar=Label(root, text="Run", relief=SUNKEN, anchor=W)
   
stautsbar.pack(side=BOTTOM,fill=X)

root.mainloop()

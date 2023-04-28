#import tkinter
from tkinter import *
# Let's create the Tkinter window
window = Tk()
window.title("GUI")

# In order to display the image in a GUI, you will use the 'PhotoImage' method of Tkinter. It will an image from the directory (specified path) and store the image in a variable.
icon = PhotoImage(file = "C:/Users/abc/Desktop/tp/a.png")

# Finally, to display the image you will make use of the 'Label' method and pass the 'image' variriable as a parameter and use the pack() method to display inside the GUI.
label = Label(window, image = icon)
label.pack()

window.mainloop()
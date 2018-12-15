from tkinter import *

root=Tk()
w = root.winfo_screenwidth() 
h = root.winfo_screenheight() 
w = w//2 
h = h//2 
w = w - 700
h = h - 450
root.geometry('1366x768+{}+{}'.format(w, h))
root.resizable(FALSE,FALSE)


rootimg=PhotoImage(file="root.gif")

l = Label(image = rootimg)
l.pack()
  
root.mainloop()
#sanyasosatisaiaisa

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
rootimg=PhotoImage(file="GOTYLABEL.png")

l1=Label(bg='red')

def start(event):
    
    bstart.destroy()
    bsettings.destroy()
    bexit.destroy()
    l.destroy()
    
    #GAME    
    
    l1.pack()






l = Label(image = rootimg)
bstartimg=PhotoImage(file="start.png")
bstart = Button(root, image = bstartimg)
bsettingsimg=PhotoImage(file="settings.png")
bsettings = Button(root, image = bsettingsimg)
bexitimg=PhotoImage(file="exit.png")
bexit = Button(root, image = bexitimg)



def ext(event):
    exit()
    
bexit.bind('<Button-1>', ext)
bstart.bind('<Button-1>',start)
bstart.place(x=463, y=220)
bsettings.place(x=463, y=370)
bexit.place(x=463, y=520)
l.pack()
root.mainloop()

bstartimg=PhotoImage(file="start.png")
bstart = Button(root, image = bstartimg)
bsettingsimg=PhotoImage(file="settings.png")
bsettings = Button(root, image = bsettingsimg)
bexitimg=PhotoImage(file="exit.png")
bexit = Button(root, image = bexitimg)



def ext(event):
    exit()
    
bexit.bind('<Button-1>', ext)
bstart.bind('<Button-1>',start)
bstart.place(x=463, y=220)
bsettings.place(x=463, y=370)
bexit.place(x=463, y=520)
root.mainloop()

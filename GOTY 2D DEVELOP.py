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

l1=Label(bg='lightgreen',text='СУПЕР КРУТАЯ\nИСТОРИЯ',font='Courier 48 bold')
nextimg=PhotoImage(file='next.png')
bnext=Button(image=nextimg)
shopimg=PhotoImage(file='shop.png')
bshop=Button(image=shopimg)




def start(event):
    
    bstart.destroy()
    bsettings.destroy()
    bexit.destroy()
    l.destroy()
    l1.pack(expand=1,fill=BOTH)
    def nextt(event):
        l1.destroy()
        bnext.destroy()
        
        bshop.place(x=10,y=200)
    bnext.bind('<Button-1>',nextt)  
    bnext.place(x=1100,y=700)
    
    
    
def upgrade(event):
    print('sasa')




l = Label(image = rootimg)
l.pack()

bstartimg=PhotoImage(file="start.png")
bstart = Button(root, image = bstartimg)
bsettingsimg=PhotoImage(file="settings.png")
bsettings = Button(root, image = bsettingsimg)
bexitimg=PhotoImage(file="exit.png")
bexit = Button(root, image = bexitimg)



def ext(event):
    root.destroy()
    
bexit.bind('<Button-1>', ext)
bstart.bind('<Button-1>',start)
bstart.place(x=463, y=220)
bsettings.place(x=463, y=370)
bexit.place(x=463, y=520)
root.mainloop()


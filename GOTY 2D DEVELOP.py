from tkinter import *
import random as ran


weplist0=(' ', '1',10,0,10,'Меч Новичка'  ,  '2',5,15,10,'Кинжал Новичка')
 # nomer,+dmg,+crit%,cost,name
weplistlist=(weplist0,)
 
 
 
charweplvl=0

root=Tk()
w = root.winfo_screenwidth() 
h = root.winfo_screenheight() 
w = w//2 
h = h//2 
w = w - 700
h = h - 450
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight())) #1366x768
root.resizable(FALSE,FALSE)
root.overrideredirect(True)
rootimg=PhotoImage(file="GotyRoot.png")

l1=Label(bg='lightgreen',text='СУПЕР КРУТАЯ\nИСТОРИЯ',font='Courier 48 bold')
nextimg=PhotoImage(file='next.png')
bnext=Button(image=nextimg)



shopimg=PhotoImage(file='shop.png')
bshop=Button(image=shopimg)
charimg=PhotoImage(file='char.png')
bchar=Button(image=charimg)
whutimg=PhotoImage(file='whut.png')
bwhut=Button(image=whutimg)
nextbimg=PhotoImage(file='nextb.png')
bnextb=Button(image=nextbimg)

characterimg=PhotoImage(file='character.png')
lchar=Label(image=characterimg)




#wep1=((weplistlist[charweplvl])[ran.randint(1,( (len(weplistlist[charweplvl])-1)//5 ))])
#wep1img=PhotoImage(file= (weplistlist[charweplvl])[(''.join(weplistlist[charweplvl]).find(str(wep1)))+4] )#
# Разбирайся тут я не понел





def upgrade(event):
    l1.destroy()
    bnext.destroy()
    
    bchar.bind('<Button-1>',charup)
    bchar.place(x=10,y=50)
    bshop.place(x=10,y=180)
    bwhut.place(x=10,y=310)
    bnextb.place(x=10,y=615)

def charup(event):
    
    lchar.place(x=700,y=50)



def start(event):
    
    bstart.destroy()
    bsettings.destroy()
    bexit.destroy()
    l.destroy()
    l1.pack(expand=1,fill=BOTH)
    bnext.bind('<Button-1>',upgrade)  
    bnext.place(x=1100,y=700)
    
    



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

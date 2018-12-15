from tkinter import *

root=Tk()
root.title('Testbattle')
w = root.winfo_screenwidth() 
h = root.winfo_screenheight() 
w = w//2 
h = h//2 
w = w - 512
h = h - 300
root.geometry('1024x600+{}+{}'.format(w, h))
root.resizable(FALSE,FALSE)


start=Button(root,text='start')


def battle(event):
    start.destroy()
    def startmenu(event):
        
        dam.destroy()
        hpbar.destroy()
        endb.destroy()
        ehpbar.destroy()
        
        start=Button(root,text='start')
        start.bind('<Button-1>',battle)
        start.pack()
    
    
    hpbar=Label(root,width=40,height=2,bg='red')
    ehpbar=Label(root,width=40,height=2,bg='darkred')
    
    dam=Button(root,bg='gray',width=20,height=3,text='Attack')
    endb=Button(root,bg='darkblue',width=20,height=3)
    def att(event):
        ehpbar['width']=ehpbar['width']-10
        if ehpbar['width']==0:
            ehpbar.destroy()
    dam.bind('<Button-1>',att)
    endb.bind('<Button-1>',startmenu)
    
    hpbar.place(x=20,y=20)
    ehpbar.place(x=720,y=20)
    dam.place(x=20,y=526)
    endb.place(x=820,y=526)    
start.bind('<Button-1>',battle)

start.pack()
root.mainloop()

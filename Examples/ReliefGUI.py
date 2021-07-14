from tkinter import *
from random import *
App = Tk()
App.title('Lottery')
App.geometry('200x120')
App['background']= 'pink'

inp = Entry(App,background='grey',foreground='white',relief='sunken',borderwidth=5,width = 25)
inp.grid(row=0,column=0,columnspan=2,padx=25,pady=5)

def m_table():
    num = list(inp.get().split(','))
    s = 'Choice: '+str(choice(num))
    l = Label(App,text=s,font=('Courier',10),background='cyan',foreground='black',relief='raised',borderwidth=3,width=15)
    l.grid(row=2,column=0,columnspan=2,padx=40,pady=2)
    quit_b['state'] = NORMAL

B = Button(App, text='Generate',command=m_table,background='green',foreground='white',relief='groove',borderwidth=5)
B.grid(row=1,column=0,padx=5,pady=5)
quit_b = Button(App, text='Cancel',command=App.quit,state=DISABLED,background='red',foreground='white',relief='flat',borderwidth=5)
quit_b.grid(row=1,column=1,padx=5,pady=5)
App.mainloop()
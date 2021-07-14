from tkinter import *
from random import *
App = Tk()
App.title('Lottery')
App.geometry('250x150')
App['background']= 'pink'

inp = Entry(App,background='grey',foreground='white',relief='sunken',borderwidth=5,width = 25)
inp.grid(row=0,column=0,columnspan=2,padx=25,pady=5)

no_choice = IntVar()
rb1 = Radiobutton(App, text = '1',variable=no_choice,value=1)
rb2 = Radiobutton(App, text = '2',variable=no_choice,value=2)
rb1.grid(row=1,column=0,padx=25,pady=5)
rb2.grid(row=1,column=1,padx=25,pady=5)
rb1.select()
def m_table():
    num = list(inp.get().split(','))
    if(no_choice.get()==2):
        e = sample(num,2)
        s = 'Choice: '+str(e[0]+' '+e[1])
    else:
        s= 'Choice: '+str(choice(num))
    l = Label(App,text=s,font=('Courier',10),background='cyan',foreground='black',relief='raised',borderwidth=3,width=15)
    l.grid(row=3,column=0,columnspan=2,padx=40,pady=2)
    quit_b['state'] = NORMAL

B = Button(App, text='Generate',command=m_table,background='green',foreground='white',relief='groove',borderwidth=5)
B.grid(row=2,column=0,padx=5,pady=5)
quit_b = Button(App, text='Cancel',command=App.quit,state=DISABLED,background='red',foreground='white',relief='flat',borderwidth=5)
quit_b.grid(row=2,column=1,padx=5,pady=5)
App.mainloop()
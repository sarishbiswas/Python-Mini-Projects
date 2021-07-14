from tkinter import *

App = Tk()
App.title('Multiplication Table')
App.geometry('200x350')

inp = Entry(App,text='Enter a number')
inp.grid(row=0,column=0,columnspan=2,padx=25,pady=5)

def m_table():
    num = int(inp.get())
    for i in range(1,11):
        l = Label(App,text=str(num)+" x "+str(i)+" = "+str(num*i))
        l.grid(row=1+i,column=0,padx=25,pady=2)
    quit_b['state'] = NORMAL

B = Button(App, text='Generate',command=m_table)
B.grid(row=1,column=0,padx=5,pady=5)
quit_b = Button(App, text='Cancel',command=App.quit,state=DISABLED)
quit_b.grid(row=1,column=1,padx=5,pady=5)
App.mainloop()
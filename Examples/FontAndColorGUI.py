from tkinter import *

App = Tk()
App.title('Multiplication Table')
App.geometry('200x350')
App['background']= 'pink'

inp = Entry(App,background='grey',foreground='white')
inp.grid(row=0,column=0,columnspan=2,padx=25,pady=5)

def m_table():
    num = int(inp.get())
    for i in range(1,11):
        l = Label(App,text=str(num)+" x "+str(i)+" = "+str(num*i),font=('Courier',10),background='cyan',foreground='black')
        l.grid(row=1+i,column=0,columnspan=2,padx=40,pady=2)
    quit_b['state'] = NORMAL

B = Button(App, text='Generate',command=m_table,background='green',foreground='white')
B.grid(row=1,column=0,padx=5,pady=5)
quit_b = Button(App, text='Cancel',command=App.quit,state=DISABLED,background='red',foreground='white')
quit_b.grid(row=1,column=1,padx=5,pady=5)
App.mainloop()
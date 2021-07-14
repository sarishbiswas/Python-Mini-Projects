from tkinter import *
from datetime import *
bg = 'black'
fg = 'cyan'
App = Tk()
App.title('Age Calculator')
App.geometry('250x150')
App['background'] = bg

label = Label(App, text='Enter the Details Below: ', foreground=fg, background=bg)
label.grid(row=0, column=0, columnspan=3)

dayL = label = Label(App, text='Day: ', foreground=fg, background=bg)
dayE = Entry(App, width=2)
monL = label = Label(App, text=' Month: ', foreground=fg, background=bg)
monE = Entry(App, width=2)
yrL = label = Label(App, text=' Year: ', foreground=fg, background=bg)
yrE = Entry(App, width=4)

dayL.grid(row=1,column=0,pady=5)
dayE.grid(row=1,column=1,pady=5)
monL.grid(row=1,column=2,pady=5)
monE.grid(row=1,column=3,pady=5)
yrL.grid(row=1,column=4,pady=5)
yrE.grid(row=1,column=5,pady=5)


def time_diff():
    days = int(dayE.get())
    mons = int(monE.get())
    yrs= int(yrE.get())
    dob = datetime(day=days, month=mons, year=yrs)
    times_now = datetime.now()
    return times_now - dob
def calculate_days():
    v = time_diff().days
    l1 = Label(App, text='Your Age is '+str(v)+' days', foreground=fg, background=bg)
    l1.grid(row=3,column=0,columnspan=6)
def calculate_seconds():
    v1 = time_diff().total_seconds()
    l2 = Label(App, text='Your have lived '+str(v1)+' seconds', foreground=fg, background=bg)
    l2.grid(row=4,column=0,columnspan=6)

b1 = Button(App, text='Click me', command = calculate_days, foreground=fg, background=bg)
b1.grid(row=2,column=0,columnspan=2)
b2 = Button(App, text='Click me', command = calculate_seconds, foreground=fg, background=bg)
b2.grid(row=2,column=2,columnspan=2)

App.mainloop()

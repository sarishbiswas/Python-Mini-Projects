from tkinter import *

App = Tk()
App.title('Slider Example')
App.geometry('250x250')

sld_var = IntVar()
slider = Scale(App,from_=0,to=10,variable=sld_var,orient=HORIZONTAL)
slider.pack()

def show():
    l = Label(App,text=str(sld_var.get()))
    l.pack()
b = Button(App,text='show',command=show)
b.pack()
App.mainloop()
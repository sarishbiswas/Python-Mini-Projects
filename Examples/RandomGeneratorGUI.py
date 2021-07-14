from tkinter import *
from random import *

App = Tk()
App.title('Random Number Generator')
App.geometry('350x450')

def rand_gen():
    label = Label(App,text=randint(1,100))
    label.pack()
B = Button(App, text= 'Generate' , command=rand_gen)
B.pack()

App.mainloop()
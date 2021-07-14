from tkinter import *

App = Tk()
App.title('Dropdown Example')
App.geometry('250x250')

colours = ['red','green','blue','yellow','cyan','pink','white','black']
var = StringVar()
menu = OptionMenu(App,var,*colours)
menu.pack()

def change_bg():
    App['background'] = var.get()
b = Button(App,text='Change Colour',command=change_bg,background='red')
b.pack()

App.mainloop()
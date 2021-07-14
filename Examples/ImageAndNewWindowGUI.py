from tkinter import *
from PIL import Image,ImageTk
App = Tk()
App.title('Python App')
App.iconbitmap(r'Res/naruto_japanese_cuisine_japan_ramen_japanese_food_icon_190977.ico')
img = ImageTk.PhotoImage(Image.open(r'../Res/Naruto_Uzumaki.png'))
L = Label(App, image=img)
L.pack()
def click():
    top = Toplevel()
    top.title('Top Image')
    l = Label(top, text='abcd')
    l.pack()
b = Button(App,command=click,text='Click Me')
b.pack()
App.mainloop()
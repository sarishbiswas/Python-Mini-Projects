from tkinter import *
from tkinter import filedialog
from PIL import Image,ImageTk
App = Tk()
App.title('Python App')
App.iconbitmap(r'Res/naruto_japanese_cuisine_japan_ramen_japanese_food_icon_190977.ico')
def click():
    global img
    App.fname = filedialog.askopenfilename(initialdir='Res',
                                           title='Select an Image',
                                           filetypes=(('PNG Images','*.png'),
                                                      ('Jpeg Images','*.jpg'),
                                                      ('Icon Images','*.ico'),
                                                      ('All Files','*.*'))
                                           )
    b.destroy()
    img = ImageTk.PhotoImage(Image.open(App.fname))
    lbl = Label(App, image=img)
    lbl.pack()

b = Button(App,command=click,text='Click Me')
b.pack()
App.mainloop()
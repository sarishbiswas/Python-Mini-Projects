from tkinter import *

bg='cyan'
fg = 'black'
ft=('Times',18)
App = Tk()
App.title('Image to Icon Converter')
App.iconbitmap(r'../Res/resize.ico')
App.geometry('500x280')
App['background'] = 'pink'

def open_img():
    from tkinter import filedialog
    from PIL import Image
    global img
    file_dir = filedialog.askopenfilename(initialdir='C:/', title='Choose the image',filetypes=(('PNG Images','*.png'),('JPEG/JPG Images','*.jpg'),('All Files','*.*')))
    img = Image.open(file_dir)

def convert_img():
    from PIL import Image
    img.save(f'{ico_name.get()}.ico',format='ICO',sizes=[(ico_size.get(),ico_size.get())])

    success = Toplevel()
    success.title('Success')
    msg = Label(success,text='Image is Converted succesfully.',font=ft)
    msg.grid(row=0,column=0)
    success.mainloop()


def preview():
    prev = Toplevel()
    prev.title('Image Preview')
    prev.iconbitmap(f'{ico_name.get()}.ico')
    prev_label = Label(prev,text='Checkout your Icon!',font=ft)
    prev_label.grid(row=0,column=0)


fileL = Label(App,text='Choose Your Image: ',background=bg,foreground=fg,font=ft)
fileB = Button(App,text='Choose file',command=open_img,background=bg,foreground=fg,font=ft,width=10)
fileL.grid(row=0,column=0,padx=5,pady=10)
fileB.grid(row=0,column=1,padx=5,pady=10)

sizeL = Label(App,text="Choose the size(pixel): ",background=bg,foreground=fg,font=ft)
sizeL.grid(row=1,column=0,padx=5,pady=10)
ico_size=IntVar()
sizes=[16,32,48,64,128,256]
ico_size.set(32)
options = OptionMenu(App,ico_size,*sizes)
options.config(bg=bg,fg=fg,font=ft,width=10)
options.grid(row=1,column=1,padx=5,pady=10)


fnameL = Label(App,text='Enter the name of the file: ',background=bg,foreground=fg,font=ft)
fnameL.grid(row=2,column=0,padx=5,pady=10)
ico_name = Entry(App,background=bg,foreground=fg,font=ft,width=15)
ico_name.grid(row=2,column=1,padx=5,pady=10)

convertB = Button(App,text='Convert',command=convert_img,background=bg,foreground=fg,font=ft)
convertB.grid(row=3,column=0,padx=5,pady=10)

previewB = Button(App,text='Preview',command=preview,background=bg,foreground=fg,font=ft)
previewB.grid(row=3,column=1,padx=5,pady=10)
App.mainloop()
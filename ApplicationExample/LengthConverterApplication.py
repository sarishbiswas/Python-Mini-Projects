from tkinter import *
from PIL import Image,ImageTk
bg='cyan'
fg = 'black'
App = Tk()
App.title('Length Converter')
App.iconbitmap(r'../Res/resize.ico')
App.geometry('420x250')
App['background'] = 'yellow'
scales=['Meters','Inches','Foot']

label_from = Label(App, text='Convert From: ',background=bg,foreground=fg,font=('Times',18))
from_entry = Entry(App,width=15,background=bg,foreground=fg,font=('Times',18))
from_entry.insert(END,'0.0')
from_var= StringVar()
from_var.set('Select')
from_menu = OptionMenu(App,from_var,*scales)
from_menu.config(bg=bg,fg=fg,font=('Times',18))

label_to = Label(App, text='Convert To: ',background=bg,foreground=fg,font=('Times',18))
result_label = Label(App, text='0.0',width=15,background=bg,foreground=fg,font=('Times',18))
result_label.grid(row=1, column=1, padx=5, pady=5)
to_var= StringVar()
to_var.set('Select')
to_menu = OptionMenu(App,to_var,*scales)
to_menu.config(bg=bg,fg=fg,font=('Times',18))
def converter():
    from_=from_var.get()
    to_=to_var.get()
    if from_entry.get() == '0.0':
        result_label = Label(App, text='Enter a Number',width=15, background=bg, foreground=fg, font=('Times', 18))
        result_label.grid(row=1, column=1, padx=5, pady=5)
    else:
        num = int(from_entry.get())
        if from_ == 'Meters' and to_ == 'Inches':
            converted_num = num * 39.37
        elif from_ == 'Meters' and to_ == 'Foot':
            converted_num = num * 3.28
        elif from_ == 'Inches' and to_ == 'Meters':
            converted_num = num / 39.37
        elif from_ == 'Inches' and to_ == 'Foot':
            converted_num = num / 12
        elif from_ == 'Foot' and to_ == 'Meters':
            converted_num = num / 3.28
        elif from_ == 'Foot' and to_ == 'Inches':
            converted_num = num * 12
        else:
            converted_num = num
        result_label = Label(App,text=str(round(converted_num,2)),background=bg,foreground=fg,font=('Times',18),width=15)
        result_label.grid(row=1,column=1,padx=5,pady=5)

label_from.grid(row=0,column=0,padx=5,pady=5)
label_to.grid(row=0,column=1,padx=5,pady=5)
from_entry.grid(row=1,column=0,padx=5,pady=5)
from_menu.grid(row=2,column=0,padx=5,pady=5)
to_menu.grid(row=2,column=1,padx=5,pady=5)

b = Button(App, text = 'Convert',command=converter,background=bg,foreground=fg,font=('Times',18))
b.grid(row=3,column=0,columnspan=2,padx=5,pady=5)
App.mainloop()
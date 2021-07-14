from tkinter import *

app = Tk()
app.title('Dice Roller')

dice = {0: '🎲', 1: '⚀', 2: '⚁', 3: '⚂', 4: '⚃', 5: '⚄', 6: '⚅'}
initial_label = Label(app,text=dice[0],foreground='black',font=('Times',200),background='cyan',width=2)
initial_label.grid(row=0,column=0)
def roll():
    from random import randint
    i = randint(1,6)
    label = Label(app,text=dice[i],foreground='black',font=('Times',200),background='cyan',width=2)
    label.grid(row=0,column=0)
b= Button(app, text= 'Roll', command= roll, foreground= 'black', font= ('Times', 10), background= 'yellow', width= 10)
b.grid(row=1,column=0)
app.mainloop()
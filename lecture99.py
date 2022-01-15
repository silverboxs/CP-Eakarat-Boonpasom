from cgitb import text
import math
from tkinter import *

def BMIcal(event):
    result = float(textboxWeigth.get()) / math.pow(float(textboxHeight.get())/100,2)
    print(result)
    labelResult.configure(result)
    #labelResult.configure(result)
    #print(float(textboxWeigth.get()) / math.pow(float(textboxHeight.get())/100,2))

MainWindow = Tk()
labelHeight = Label(MainWindow,text="ส่วนสูง (cm.)", font=("Tahoma",14))
labelHeight.grid(row=0,column=0)
textboxHeight = Entry(MainWindow, font=("Tahoma",14))
textboxHeight.grid(row=0,column=1)
labelWeigth = Label(MainWindow,text="น้ำหนัก (KG.)", font=("Tahoma",14))
labelWeigth.grid(row=1,column=0)
textboxWeigth = Entry(MainWindow, font=("Tahoma",14))
textboxWeigth.grid(row=1,column=1)
button = Button(MainWindow, text="คำนวณ", font=("Tahoma",14), fg="blue")
button.grid(row=2,column=0)
button.bind('<Button-1>', BMIcal)
labelResult = Label(MainWindow)
labelResult.grid(row=2, column=1)
MainWindow.mainloop()
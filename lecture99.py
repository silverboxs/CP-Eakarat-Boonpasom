from tkinter import *
import math

def BMIcal(event):
    result = float(textboxWeigth.get()) / math.pow(float(textboxHeight.get())/100,2)
    #print(result)
def testLabel(e):
    #Result.configure("TEST TEXT")
    #result = float(textboxWeigth.get()) / math.pow(float(textboxHeight.get())/100,2)
    print(textboxHeight.get())
    labelResult.configure(textboxHeight.get())

MainWindow = Tk()
labelHeight = Label(MainWindow,text="ความสูง(cm.)")
labelHeight.grid(row=0,column=0)
textboxHeight = Entry(MainWindow)
textboxHeight.grid(row=0,column=1)
labelWeigth = Label(MainWindow,text="น้ำหนัก (KG.)")
labelWeigth.grid(row=1, column=0)
textboxWeigth = Entry(MainWindow)
textboxWeigth.grid(row=1, column=1)
button = Button(MainWindow,text="คำนวณ")
button.bind('<Button-1>',testLabel)
button.grid(row=2,column=0)
labelResult = Label(MainWindow, text="")
labelResult.grid(row=2, column=1)


MainWindow.mainloop()

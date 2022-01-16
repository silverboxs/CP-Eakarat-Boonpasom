from tkinter import *
import math

def BMIcal(event):
    result = float(textboxWeigth.get()) / math.pow(float(textboxHeight.get())/100,2)

    if result <= 18.5:
        resultText2 = "ผอมเกินไป"
    elif result <= 22.9:
        resultText2 = "น้ำหนักปกติ"
    elif result <= 24.9:
        resultText2 = "น้ำหนักเกินปกติ"
    elif result <= 29.9:
        resultText2 = "อ้วน"
    else:
        resultText2 = "อ้วนมาก"

    resultText = "{:.2f}".format(result)
    labelResult.configure(text=float(resultText))
    labelResult2.configure(text=resultText2)


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
button.bind('<Button-1>',BMIcal)
button.grid(row=2,column=0)
labelResult = Label(MainWindow, text="")
labelResult.grid(row=2, column=1)
labelResult2 = Label(MainWindow, text="")
labelResult2.grid(row=3, column=1)


MainWindow.mainloop()
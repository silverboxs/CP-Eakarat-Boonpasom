from msilib.schema import ComboBox
from tkinter import *
from tkinter import ttk
from datetime import datetime
from tracemalloc import start
from forex_python.converter import CurrencyRates
from forex_python.bitcoin import BtcConverter
from idna import check_initial_combiner

btc = BtcConverter()

def dayList():
    dayList = list()
    for x in range(31):
        dayList.append(x+1)    

    return dayList

def YearList():
    y = list()
    year = 2022
    while year >= 2016:
        y.append(year)
        year -= 1

    return y

def timeSet(e):
    month = {
        'January':1, 
        'February':2,
        'March':3,
        'April':4,
        'May':5,
        'June':6,
        'July':7,
        'August':8,
        'September':9,
        'October':10,
        'November':11,
        'December':12
    }

    return datetime(int(value_year.get()),month[value_month.get()],int(value_day.get()),10,0,0,151012)    

def convert_to_BTC(e):
    conver_btc2016 = btc.convert_to_btc_on(1000,'THB',timeSet(e))
    decimalFormat = '{:.4f}'
    print(decimalFormat.format(conver_btc2016))


Main = Tk()
Main.geometry("500x500")
Main.configure(background="#333333")
Main.title("Bitcoin พารวย")

text_display_1 = Label(Main, text='ถ้าคุณซื้อ Bitcoin ไว้ในปี',font=('Tahoma',14,'bold'),bg='#333333',fg='white')
text_display_1.place(relx= 0.5, rely= 0.05, anchor='center')
#date Label Text...
text_day = Label(Main, text="DAY", font=('Tahoma',16,'bold'), bg='#333333', fg='white')
text_day.place(relx= 0.28, rely=0.15, anchor='center')
text_month = Label(Main, text="MONTH", font=('Tahoma',16,'bold'), bg='#333333', fg='white')
text_month.place(relx= 0.48, rely=0.15, anchor='center')
text_year = Label(Main, text="YEAR", font=('Tahoma',16,'bold'), bg='#333333', fg='white')
text_year.place(relx= 0.68, rely=0.15, anchor='center')

#Date combobox
value_day = ttk.Combobox(Main , width= 3 ,
                                values= (dayList()),
                                font=('Tahoma',10,'bold'))
value_day.place(relx=0.24, rely=0.2)
value_month = ttk.Combobox(Main, width=10,
                                values=('January', 
                                        'February',
                                        'March',
                                        'April',
                                        'May',
                                        'June',
                                        'July',
                                        'August',
                                        'September',
                                        'October',
                                        'November',
                                        'December'))
value_month.place(relx=0.40, rely=0.2)   
value_year = ttk.Combobox(Main, width=10,values=(YearList()))
value_year.place(relx=0.62,rely=0.2)

#Amount THB--
txt_amount = Label(Main, text="จำนวนเงินที่ซื้อ:",font=('Tahoma',16,'bold'), bg='#333333', fg='white')
txt_amount.place(relx=0.05,rely=0.3)
value_amount = Entry(Main,width=20)
value_amount.place(relx=0.4, rely=0.3)

button_submit = Button(Main, text="TEST", width=30,height=1)
button_submit.bind('<Button-1>',convert_to_BTC)
button_submit.place(relx=0.3, rely=0.4)
Main.mainloop()                            

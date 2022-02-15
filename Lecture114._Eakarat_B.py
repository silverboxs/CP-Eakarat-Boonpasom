from msilib.schema import ComboBox
from tkinter import *
from tkinter import ttk
from datetime import datetime
from forex_python.bitcoin import BtcConverter

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
    conver_btc2016 = btc.convert_to_btc_on(int(value_amount.get()),'THB',timeSet(e))
    conver_btc_last = btc.convert_btc_to_cur(conver_btc2016,'THB',)
    #Text Format....
    decimalFormat = '{:.4f}'
    THB_Format = '{:,.2f}'
    txt_date = value_day.get()+'-'+value_month.get()+'-'+value_year.get()+'\n'
    textResult = "จำนวน Bitcoin ที่คุณได้ : = "+decimalFormat.format(conver_btc2016)+" BTC"
    #Label Result Buy
    txt_btc_result = Label(Main, text=str(txt_date+textResult), font=('Tahoma',16,'bold'))
    txt_btc_result.place(relx=0.15, rely=0.5)
    #Text Format.....Now
    text_result_now = "ปัจจุบัน Bitcoin ของคุณจะมีมูลค่า\n"+THB_Format.format(conver_btc_last)+".-บาท"
    #Label Result Now
    txt_btc_last = Label(Main,text=text_result_now, font=('Tahoma',16,'bold'))
    txt_btc_last.place(relx=0.15,rely=0.7,width=400)

Main = Tk()
Main.geometry("500x500")
Main.configure(background="#333333")
Main.title("Bitcoin พารวย")

text_display_1 = Label(Main, text='>> ถ้าคุณซื้อ Bitcoin ในวันที่ <<',font=('Tahoma',14,'bold'),bg='#333333',fg='white')
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
value_amount = Entry(Main)
value_amount.place(relx=0.4, rely=0.3, width=200, height=30)

button_submit = Button(Main, text="คำนวณ", width=30,height=1)
button_submit.bind('<Button-1>',convert_to_BTC)
button_submit.place(relx=0.3, rely=0.4)
Main.mainloop()  

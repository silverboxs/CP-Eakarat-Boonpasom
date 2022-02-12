from tkinter import *
from tkinter import ttk
from datetime import datetime
from forex_python.converter import CurrencyRates
from forex_python.bitcoin import BtcConverter

Main = Tk()
Main.geometry("500x500")
Main.configure(background="#333333")
Main.title("Bitcoin พารวย")

text_display_1 = Label(Main, text='ถ้าคุณซื้อ Bitcoin ไว้จะรวยขนาดไหน',font=('Tahoma',14,'bold'),bg='#333333',fg='white')
text_display_1.place(relx= 0.5,
                     rely= 0.05,
                     anchor='center')
text_day = Label(Main, text="DAY", font=('Tahoma',16,'bold'), bg='#333333', fg='white')
text_day.place(relx= 0.28, rely=0.15, anchor='center')
text_month = Label(Main, text="MONTH", font=('Tahoma',16,'bold'), bg='#333333', fg='white')
text_month.place(relx= 0.48, rely=0.15, anchor='center')
text_year = Label(Main, text="YEAR", font=('Tahoma',16,'bold'), bg='#333333', fg='white')
text_year.place(relx= 0.68, rely=0.15, anchor='center')
Main.mainloop()
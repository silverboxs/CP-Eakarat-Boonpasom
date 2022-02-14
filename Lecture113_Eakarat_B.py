from forex_python.converter import CurrencyRates
from forex_python.bitcoin import BtcConverter
import datetime

c = CurrencyRates()
btc = BtcConverter()
time_now = datetime.datetime.now()
time_2016 = datetime.datetime(2016,2,14,10,10,10,151012)


buy_btc_2016 = int(input("ซื้อ BTC (2016) :"))
cover_btc2016 = btc.convert_to_btc_on(buy_btc_2016,'THB',time_2016)
print("Your BTC on 2016 :","{:.4f}".format(cover_btc2016))

cover_btc_now = btc.convert_btc_to_cur(cover_btc2016,'THB')
print("Your BTC/THB Now:","{:,.2f}".format(cover_btc_now))

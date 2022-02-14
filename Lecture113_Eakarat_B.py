from forex_python.converter import CurrencyRates
from forex_python.bitcoin import BtcConverter
import datetime

c = CurrencyRates()
btc = BtcConverter()
time_now = datetime.datetime.now()
time_2016 = datetime.datetime(2016,2,14,10,10,10,151012)
'''
usd_price_now = c.get_rate('USD','THB',star_time)
usd_price_2016 = c.get_rate('USD','THB',star_last)
btc_price_now = btc.get_latest_price('THB')
btc_price_2016 = btc.get_previous_price('THB',star_last)
btc_profit = btc_price_now-btc_price_2016

print("USD-2016:\t","{:.2f}".format(usd_price_2016))
print("USD-NOW:\t","{:.2f}".format(usd_price_now))
print("\n")
print("BTC/USD 2016:","{:,.0f}".format(btc_price_2016))
print("BTC/USD NOW:","{:,.0f}".format(btc_price_now))
print("Profit / BTC:","{:,.0f}".format(btc_profit))
print("Time:\t",star_time-star_last)
'''
buy_btc_2016 = int(input("ซื้อ BTC (2016) :"))
cover_btc2016 = btc.convert_to_btc_on(buy_btc_2016,'THB',time_2016)
print("Your BTC on 2016 :","{:.4f}".format(cover_btc2016))

cover_btc_now = btc.convert_btc_to_cur(cover_btc2016,'THB')
print("Your BTC/THB Now:","{:,.2f}".format(cover_btc_now))

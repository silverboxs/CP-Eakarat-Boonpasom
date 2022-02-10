from forex_python.converter import CurrencyRates
from forex_python.bitcoin import BtcConverter
import datetime

c = CurrencyRates()
btc = BtcConverter()
star_time = datetime.datetime.now()
star_last = datetime.datetime(2016,2,14,10,10,10,151012)

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
# -*- coding: utf-8 -*-
"""
Spyder Editor

This code shows how to make a dataframe containing adj. close prices 
using yahoofinancials library (which gives json output)
"""
import pandas as pd
import datetime as dt
from yahoofinancials import YahooFinancials

all_tickers = ["TATASTEEL.NS", "SBIN.NS", "UPL.NS"]

#extracting stock data for the tickers, one by one

close_prices = pd.DataFrame() #creating an emply dataframe
end_date = dt.datetime.today().strftime('%Y-%m-%d') #converting date into YYYY-MM-DD format
beg_date = (dt.datetime.today()-dt.timedelta(365)).strftime('%Y-%m-%d')

for ticker in all_tickers: 
    yahoo_financials=YahooFinancials(ticker) #creating an object called yahoo_financials
    json_obj= yahoo_financials.get_historical_price_data(beg_date, end_date, "daily") 
    ohlv= json_obj[ticker]["prices"] #ohlv is a dataframe containing ohlv data of this particular ticker
    temp=pd.DataFrame(ohlv)[["formatted_date", "adjclose"]] #gives a df with 2 columns
    temp.set_index("formatted_date", inplace=True) #sets the dates as the first columns (index)
    temp.dropna(inplace=True) #drops na values
    close_prices[ticker] = temp["adjclose"]
   
    
    

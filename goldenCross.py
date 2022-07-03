import yfinance as yf
import pandas as pd
from pandas_datareader import data
#from datetime import datetime
import datetime
import talib
import numpy as np
yf.pdr_override() #以pandasreader常用的格式覆寫

target_stock = '2454.TW'  #股票代號變數

today = datetime.datetime.today()
yy = today.year
mm = today.month
dd = today.day

start_date = datetime.datetime(2010, 1, 1)
end_date = datetime.datetime(yy, mm, dd) #設定資料起訖日期

df = data.get_data_yahoo([target_stock], start_date, end_date) #將資料放到Dataframe裡面
df['5MA'] = talib.SMA(df['Close'],timeperiod=5)
df['10MA'] = talib.SMA(df['Close'],timeperiod=10)
df['20MA'] = talib.SMA(df['Close'],timeperiod=20)
df['60MA'] = talib.SMA(df['Close'],timeperiod=60)
df['120MA'] = talib.SMA(df['Close'],timeperiod=120)
df['240MA'] = talib.SMA(df['Close'],timeperiod=240)

#print(df)
stock_without_nan = df
# # 去除NaN值
stock_without_nan = df[239:]
# #stock_without_nan = stock_without_nan.reset_index(drop=True)
# stock_without_nan.head()


# 目前快線慢線的相對位置
stock_without_nan['positions'] = np.where(stock_without_nan['5MA'] > stock_without_nan['10MA'], 1, -1)

print(stock_without_nan)

# --------- Write into Excel---------

# Specify the name of the excel file
file_name = 'goldenCross.xlsx'
print(stock_without_nan.info())

 
#df['Date']= pd.to_datetime(df['Date'])

# saving the excelsheet
stock_without_nan.to_excel(file_name)
print('Sales record successfully exported into Excel File')

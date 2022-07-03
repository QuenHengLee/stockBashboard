import yfinance as yf
import pandas as pd
from pandas_datareader import data
#from datetime import datetime
import datetime
yf.pdr_override() #以pandasreader常用的格式覆寫

target_stock = '2454.TW'  #股票代號變數

today = datetime.datetime.today()
yy = today.year
mm = today.month
dd = today.day

start_date = datetime.datetime(2010, 1, 1)
end_date = datetime.datetime(yy, mm, dd) #設定資料起訖日期

df = data.get_data_yahoo([target_stock], start_date, end_date) #將資料放到Dataframe裡面
 
#print(df)

# Specify the name of the excel file
file_name = 'stock_Output.xlsx'
print(df.info())

 
#df['Date']= pd.to_datetime(df['Date'])

# saving the excelsheet
df.to_excel(file_name)
print('Sales record successfully exported into Excel File')

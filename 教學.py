import twstock
import pandas

# 更新
twstock.__update_codes()

# 查看交易所商品清單
tickers = twstock.twse
df_tickers = pandas.DataFrame(tickers).T

# 判斷股票是否在清單裡面
'2330' in tickers

# 取得證交所股票data
stock = twstock.Stock('2330')
symbol = stock.sid # 回傳股票代號
date = stock.date # 時間
open = stock.open # 開
high = stock.high # 高
low = stock.low # 低
close = stock.price # 收


# 轉成DataFrame
data = {'Symbol': symbol,
        'Open': open, 
        'High': high, 
        'Low': low, 
        'Close': close}

df = pandas.DataFrame(data, index=date)

# 取得其他期間歷史資料
stock.fetch(2015, 7)  # 獲取 2015 年 7 月之股票資料
stock.fetch(2010, 5)  # 獲取 2010 年 5 月之股票資料
stock.fetch_31()      # 獲取近 31 日開盤之股票資料
stock.fetch_from(2000, 10)  # 獲取 2000 年 10 月至今日之股票資料(小心使用可能會被連線拒絕)
close = stock.price

# 取得即時資料
stock = twstock.realtime.get('2330')
print(stock['success']) # 確認是否回報有誤

# 取得多檔即時資料
stocks = twstock.realtime.get(['2330', '2317', '3008'])
df_realtime = pandas.DataFrame(stocks)

# 內建的買賣點分析 BestFourPoint(分析4大買賣點)
'''
o 量大收紅 / 量大收黑
o 量縮價不跌 / 量縮價跌
o 三日均價由下往上 / 三日均價由上往下
o 三日均價大於六日均價 / 三日均價小於六日均價
'''
stock = twstock.Stock('2330')
bfp = twstock.BestFourPoint(stock)
bfp.best_four_point_to_buy()   # 判斷是否為四大買點
bfp.best_four_point_to_sell()  # 判斷是否為四大賣點
bfp.best_four_point()          # 綜合判斷
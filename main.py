df_new = df_new.astype(‘float’) # 確認價量資料表 df 的值都是 float 格式
ta_list = [‘MACD’,‘RSI’] # 準備一份你想要計算並且併入 df 的技術指標清單
ta_list = talib.get_functions() # 這裡示範全部 158 種技術指標
for x in ta_list:
    try:
        # x 為技術指標的代碼，透過迴圈填入，再透過 eval 計算出 output
        output = eval('abstract.'+x+'(df_new)')
        # 如果輸出是一維資料，幫這個指標取名為 x 本身；多維資料則不需命名
        output.name = x.lower() if type(output) == pd.core.series.Series else None
        # 透過 merge 把輸出結果併入 df DataFrame
        df_new = pd.merge(df_new, pd.DataFrame(output), left_on = df_new.index, right_on = output.index)
        df_new = df_new.set_index('key_0')
    except:
        print(x)

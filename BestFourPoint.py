from twstock import Stock
from twstock import BestFourPoint
import pandas as pd

stock = Stock('2454')
bfp = BestFourPoint(stock)

# result = bfp.best_four_point_to_buy()    # 判斷是否為四大買點
# print(result)
# result = bfp.best_four_point_to_sell()   # 判斷是否為四大賣點
# print(result)

result = bfp.best_four_point() 
 
print(result[0])
print(result[1])



df = pd.DataFrame(columns = ["signal", "reason"]) #建立一個空的dataframe
#df.loc[0]=[ 'Mango', 4 ]

if(result[0] == "True"):
    df.loc[0]=[ '買入', result[1] ]
else:
    df.loc[0]=[ '賣出', result[1] ]

print(df)
 




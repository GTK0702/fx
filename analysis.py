import mplfinance as mpf
from pandas_datareader import data
import warnings
warnings.simplefilter("ignore")
import talib as ta

start="2021-01-01"
end="2021-03-07"

df=data.DataReader("JPY=X","yahoo",start,end)

#調整済終値が引数。短期起動平均/長期移動平均/MACDシグナルで成り立つ
df["macd"],df["macdsignal"],df["macdhist"]=ta.MACD(df["Adj Close"],fastperiod=12,slowperiod=26,signalperiod=9)

df.tail()

apds=[mpf.make_addplot(df["upper"],color="g"),
      mpf.make_addplot(df["middle"],color="b"),
      mpf.make_addplot(df["lower"],color="r"),
      mpf.make_addplot(df["macdhist"],type="bar",color="gray",
                       width=1.0,panel=1,alpha=0.5,ylabel="MACD")]
#type="bar":棒グラフ.width:棒グラフの幅.alpha:透明度.

mpf.plot(df,type="candle",figsize=(30,15),style="yahoo",addplot=apds)

mpf.plot(df,type="candle",figsize=(30,15),style="yahoo",addplot=apds,savefig="technical.png")
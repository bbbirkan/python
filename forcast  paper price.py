import pandas_datareader as pd
from fbprophet import Prophet
from matplotlib import pyplot
import datetime as dt
import warnings
warnings.simplefilter(action="ignore",category=FutureWarning)

end=dt.datetime.now()
start=dt.datetime(end.year - 20, end.month,end.day)
# print(start)
df = pd.get_data_yahoo('NVDA',start,end)

print(df.head())
# print(df.describe())
df=df.reset_index()
df[['ds', 'y']]=df[["Date","Adj Close"]]
# print(df.dtypes)

m = Prophet(interval_width=0.95, daily_seasonality=True)
model = m.fit(df)
future = m.make_future_dataframe(periods=365)
forecast = m.predict(future)
plot1 = m.plot(forecast)
plt2 = m.plot_components(forecast)
df.plot()
pyplot.show()

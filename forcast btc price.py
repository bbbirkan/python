import pandas as pd
from fbprophet import Prophet
from matplotlib import pyplot

df = pd.read_csv('market-price.csv')
df.describe()


# test data cvs
colum1="2021-01-30 00:00:00,34314.26"
print(colum1[8:10])

# print(df.describe())
# print(df.dtypes)
df['Year'] = df['Timestamp'].apply(lambda x: str(x)[0:4])
df['Month'] = df['Timestamp'].apply(lambda x: str(x)[5:7])
df['Day'] = df['Timestamp'].apply(lambda x: str(x)[8:10])
df['ds'] = pd.DatetimeIndex(df['Year']+'-'+df['Month']+'-'+df['Day'])

print(df.dtypes)
print(df.head())

df.drop(['Timestamp','Year', 'Month', 'Day'], axis=1, inplace=True)
df.columns = ['y', 'ds']
# df.columns = ['ds', 'y']# y=Volume ds=time

print(df.head())

m = Prophet(interval_width=0.95, daily_seasonality=True)
model = m.fit(df)

future = m.make_future_dataframe(periods=365,freq='D')
forecast = m.predict(future)
plot1 = m.plot(forecast)
plt2 = m.plot_components(forecast)

df.plot()
pyplot.show()

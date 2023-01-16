import yfinance as yf
import pandas as pd
import seaborn as sns
from yahooquery import Ticker
import matplotlib.pyplot as plt
from datetime import date,datetime,timedelta
from dateutil.relativedelta import relativedelta
import plotly.subplots as sp
import plotly.graph_objs as go

weeks_input=100
months_input=1
today= datetime.now().strftime("%Y-%m-%d")
months_ago = (datetime.now() - relativedelta(months=months_input)).strftime("%Y-%m-%d")
weeks_ago = (datetime.now()- timedelta(weeks_input)).strftime("%Y-%m-%d")
items= ['AAPL', 'MSFT', 'BRK-A']
print(months_ago)
print(weeks_ago)
data_heatmap = {}
data_ploty={}
for i in items:
    ticker = i
    check = Ticker(ticker)
    short_name = check.quote_type[ticker]['shortName']
    try:
        all_data = check.all_modules
        country = all_data[ticker]['summaryProfile']["country"]
        sector = all_data[ticker]['summaryProfile']["sector"]
        industry = all_data[ticker]['summaryProfile']["industry"]
        print(f'\n{short_name}: {industry} - {sector} - {country}\n')

    except:
        pass
    data_heatmap[short_name] = yf.download(ticker, start=months_ago, end=today)
    data_heatmap[short_name] = data_heatmap[short_name]['Adj Close']
# print(data_heatmap)
df = pd.concat(data_heatmap, axis=1)
df.columns = data_heatmap.keys()
corr = df.corr()

sns.heatmap(corr, annot=True)
plt.show(block=False)


###############------ploty-----################

data_ploty = {}
for i in items:
    ticker = i
    data_ploty[i] = yf.download(ticker, start=months_ago, end=today)
# Create a subplot layout
fig = sp.make_subplots(rows=len(data_ploty), cols=1)
for j, (ticker, df) in enumerate(data_ploty.items()):

    check = Ticker(ticker)
    short_name = check.quote_type[ticker]['shortName']
    print(short_name)
    fig.add_trace(go.Scatter(x=df.index, y=df['Adj Close'], name=ticker), row=j + 1, col=1)
fig.update_layout(title='Adjusted Close Prices of stocks', xaxis_title='', yaxis_title='Price')
fig.show()

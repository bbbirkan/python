import yfinance as yf
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Retrieve historical data for Nasdaq Composite, Russell 2000, and S&P 500
nasdaq = yf.download('^IXIC', start='2010-01-01', end='2023-01-10')
russell = yf.download('^RUT', start='2010-01-01', end='2023-01-10')
sp500 = yf.download('^GSPC', start='2010-01-01', end='2023-01-10')

# Convert data to pandas DataFrame
nasdaq_df = pd.DataFrame(nasdaq['Close'])
russell_df = pd.DataFrame(russell['Close'])
sp500_df = pd.DataFrame(sp500['Close'])

# Create dataframe for correlation
df = pd.concat([nasdaq_df, russell_df, sp500_df], axis=1)
df.columns = ['Nasdaq Composite', 'Russell 2000', 'S&P 500']
corr = df.corr()

# Visualize the correlation matrix
sns.heatmap(corr,annot=True)
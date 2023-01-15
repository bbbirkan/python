import pandas as pd
# Read the data from the website
df = pd.read_html("https://money.cnn.com/data/hotstocks/")[1]
print(df.head())
df['Ticker'] = df['Company'].str.split().str[0]
print(df['Ticker'])



"""                          Company   Price  Change % Change
0            WFC Wells Fargo & Co   44.22    1.39   +3.25%
1  SWK Stanley Black & Decker Inc   88.91    2.64   +3.06%
2                 TGT Target Corp  164.60    4.85   +3.04%
3        LVS Las Vegas Sands Corp   54.97    1.47   +2.75%
4         JPM JPMorgan Chase & Co  143.01    3.52   +2.52%
0    WFC
1    SWK
2    TGT
3    LVS
4    JPM
5    CLX
6    CCL
7    BAC
8    AIZ
9    OGN

"""

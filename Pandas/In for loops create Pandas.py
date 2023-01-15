from yahooquery import Ticker
import pandas as pd
ticker ="aapl"
check = Ticker(ticker)
valuation_measures = check.valuation_measures
data_frame_valuation_measures = pd.DataFrame()
count = len(valuation_measures)
for i in valuation_measures:
    for j in range(count):
        data_frame_valuation_measures.at[j, i] = valuation_measures[i][j]

# for i in valuation_measures:
#     df.at[0, i] = valuation_measures[i][0]
#     df.at[1, i] = valuation_measures[i][1]
#     df.at[2, i] = valuation_measures[i][2]
#     df.at[3, i] = valuation_measures[i][3]#.....

print(data_frame_valuation_measures.head())
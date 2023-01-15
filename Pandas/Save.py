import pandas as pd
import io,requests
# #-------------------------Ready  DATABASE Just USE ---------------------
link = requests.get("www.example.com")
dataframe = pd.read_excel(io.BytesIO(link.content))

# #---------------OPTIONAL - SAVE AS FILE DATABASE AND READ LATER---------------------
dataframe = pd.read_excel('tmp/sentiment.xls')
print(dataframe.head())

with open('tmp/sentiment.xls', 'wb') as output:
      output.write(link.content)

dataframe = pd.read_excel('tmp/sentiment.xls')

df=dataframe
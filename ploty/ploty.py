import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# plotly
# import plotly.plotly as py
from plotly.offline import init_notebook_mode, iplot, plot
import plotly as py

import plotly.graph_objs as go

# word cloud library
from wordcloud import WordCloud

# matplotlib
import matplotlib.pyplot as plt
# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory

import os
print(os.listdir("../ploty/world-university-rankings"))
timesData = pd.read_csv("../ploty/world-university-rankings/timesData.csv")
print(timesData.info())
print(timesData.head(10))
# Any results you write to the current directory are saved as output.

# prepare data frame
df = timesData.iloc[:100,:]

# import graph objects as "go"
import plotly.graph_objs as go

# Creating trace1
trace1 = go.Scatter(
                    x = df.world_rank,
                    y = df.citations,
                    mode = "lines",
                    name = "citations",
                    marker = dict(color = 'rgba(16, 112, 2, 0.8)'),
                    text= df.university_name)
# Creating trace2
trace2 = go.Scatter(
                    x = df.world_rank,
                    y = df.teaching,
                    mode = "lines+markers",
                    name = "teaching",
                    marker = dict(color = 'rgba(80, 26, 80, 0.8)'),
                    text= df.university_name)
data = [trace1, trace2]
layout = dict(title = 'Citation and Teaching vs World Rank of Top 100 Universities',
              xaxis= dict(title= 'World Rank',ticklen= 5,zeroline= False)
             )


print(df.world_rank)
import plotly
fig = dict(data = data, layout = layout)
plotly.offline.plot(fig, filename='TEST.html')



#show new version
# fig = go.Figure()
# fig.add_trace(trace1)
# fig.add_trace(trace2)
# fig.show()

#save like  image
# import os
# if not os.path.exists("images"):
#     os.mkdir("images")
# fig.write_image("images/fig1.png")
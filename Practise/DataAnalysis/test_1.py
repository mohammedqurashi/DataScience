import pandas as pd
import datetime
import pandas.io.data as web
import matplotlib.pyplot as plt
from matplotlib import style


style.use('ggplot')

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2016, 1, 1)

df = web.DataReader("KuchBhi", 'google', start, end)

#This is the real URL for API.
# www.google.com/finance/historical?q=XOM&startdate=Jan+01%2C+2010&enddate=Jan+01%2C+2016&output=csv

print (df.head())

#df['Adj Close'].plot()
df['Volume'].plot()
plt.show()

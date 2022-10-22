import imp
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas_ta as ta
import numpy as np


# Request historic pricing data via finance.yahoo.com API
df = yf.Ticker('TSLA').history(period='1y')[['Close', 'Open', 'High', 'Volume']]
# View our data
#print(df)


# # Calculate MACD values using the pandas_ta library
# df.ta.macd(close='close', fast=12, slow=26, signal=9, append=True)
# Get the 26-day EMA of the closing price
k = df['Close'].ewm(span=12, adjust=False, min_periods=12).mean()
# Get the 12-day EMA of the closing price
d = df['Close'].ewm(span=26, adjust=False, min_periods=26).mean()
# Subtract the 26-day EMA from the 12-Day EMA to get the MACD
macd = k - d
# Get the 9-Day EMA of the MACD for the Trigger line
macd_s = macd.ewm(span=9, adjust=False, min_periods=9).mean()
# Calculate the difference between the MACD - Trigger for the Convergence/Divergence value
macd_h = macd - macd_s
# Add all of our new values for the MACD to the dataframe
df['macd'] = df.index.map(macd)
df['macd_h'] = df.index.map(macd_h)
df['macd_s'] = df.index.map(macd_s)
# View our data
pd.set_option("display.max_columns", None)


df['trading_signal']  = [0] * len(df.index)


for index, row in df.iterrows():
    #print(row['macd_h'])
    
    if(df.index.get_loc(index) >= 1):
        if(df.iloc[df.index.get_loc(index)-1]['macd_h'] < 0 and row['macd_h'] > 0):
            print(row['macd_h'])
            df.iloc[df.index.get_loc(index), df.columns.get_loc('trading_signal')] = 1
            print(df.iloc[df.index.get_loc(index)]['trading_signal'])
        if(df.iloc[df.index.get_loc(index)-1]['macd_h'] > 0 and row['macd_h'] < 0):
            print(row['macd_h'])
            df.iloc[df.index.get_loc(index), df.columns.get_loc('trading_signal')] = -1
            print(df.iloc[df.index.get_loc(index)]['trading_signal'])




print(df)

df.index = df.index.tz_localize(None)

df.to_csv("MACD trading signal.csv", sep='\t')
df.to_excel(r'MACD trading signal.xlsx', index = True)


# get ticker data
df = yf.Ticker('TSLA').history(period='1y')[map(str.title, ['open', 'close', 'low', 'high', 'volume'])]
# calculate MACD values
df.ta.macd(close='close', fast=12, slow=26, append=True)
# Force lowercase (optional)
df.columns = [x.lower() for x in df.columns]
# Construct a 2 x 1 Plotly figure
fig = make_subplots(rows=2, cols=1)
# price Line
fig.append_trace(
    go.Scatter(
        x=df.index,
        y=df['open'],
        line=dict(color='#ff9900', width=1),
        name='open',
        # showlegend=False,
        legendgroup='1',
    ), row=1, col=1
)
# Candlestick chart for pricing
fig.append_trace(
    go.Candlestick(
        x=df.index,
        open=df['open'],
        high=df['high'],
        low=df['low'],
        close=df['close'],
        increasing_line_color='#ff9900',
        decreasing_line_color='black',
        showlegend=False
    ), row=1, col=1
)
# Fast Signal (%k)
fig.append_trace(
    go.Scatter(
        x=df.index,
        y=df['macd_12_26_9'],
        line=dict(color='#ff9900', width=2),
        name='macd',
        # showlegend=False,
        legendgroup='2',
    ), row=2, col=1
)
# Slow signal (%d)
fig.append_trace(
    go.Scatter(
        x=df.index,
        y=df['macds_12_26_9'],
        line=dict(color='#000000', width=2),
        # showlegend=False,
        legendgroup='2',
        name='signal'
    ), row=2, col=1
)
# Colorize the histogram values
colors = np.where(df['macdh_12_26_9'] < 0, '#000', '#ff9900')
# Plot the histogram
fig.append_trace(
    go.Bar(
        x=df.index,
        y=df['macdh_12_26_9'],
        name='histogram',
        marker_color=colors,
    ), row=2, col=1
)
# Make it pretty
layout = go.Layout(
    plot_bgcolor='#efefef',
    # Font Families
    font_family='Monospace',
    font_color='#000000',
    font_size=20,
    xaxis=dict(
        rangeslider=dict(
            visible=False
        )
    )
)
# Update options and show plot
fig.update_layout(layout)
fig.show()



#reference of MACD calculation from: https://www.alpharithms.com/calculate-macd-python-272222/
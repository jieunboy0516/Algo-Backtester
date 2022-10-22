# Algo Backtester

A backtester for quantitave trading strategies made for learning purpose.

Author: Samsam @ Imperial College London

## MACD Strategy generator

Python is used to generate trade signals using the MACD strategy. 

## Back testing framework

C++ is used to benchmark the result of the trading strategy, providing result of the profitability.


## Result of Backtesting MACD Strategy

Suppose every time the MACD line cross over the Signal line, 1 share of the taget stock is bought, and every time the MACD line cross below the Signal line, 1 share of target stock is sold. This backtester is able to calculate the networth percentage change in the past year.

I am using TSLA as an example due to its volatility.

Note: the result is not accurate due to many factors such as biased fiannce data and commission fee.


![TSLA](/imgs/tsla%20plot.png)


Result:
```

bought 1 shares. Total cash spent: 355.6666564941406. Current cash: 0. Networth: 355.6666564941406

sold 1 shares. Total cash spent: 355.6666564941406. Current cash: 343.85333251953125. Networth: 343.85333251953125

bought 1 shares. Total cash spent: 663. Current cash: 343.85333251953125. Networth: 651.1866760253906

sold 1 shares. Total cash spent: 663. Current cash: 635.7733459472656. Networth: 635.7733459472656

bought 1 shares. Total cash spent: 970.4766540527344. Current cash: 635.7733459472656. Networth: 943.25

sold 1 shares. Total cash spent: 970.4766540527344. Current cash: 909.6166687011719. Networth: 909.6166687011719

bought 1 shares. Total cash spent: 1258.5999755859375. Current cash: 909.6166687011719. Networth: 1197.739990234375

sold 1 shares. Total cash spent: 1258.5999755859375. Current cash: 1165.0733337402344. Networth: 1165.0733337402344

bought 1 shares. Total cash spent: 1538.6766357421875. Current cash: 1165.0733337402344. Networth: 1445.1499938964844

sold 1 shares. Total cash spent: 1538.6766357421875. Current cash: 1506.9033203125. Networth: 1506.9033203125

bought 1 shares. Total cash spent: 1791.8866424560547. Current cash: 1506.9033203125. Networth: 1760.1133270263672

sold 1 shares. Total cash spent: 1791.8866424560547. Current cash: 1793.5333251953125. Networth: 1793.5333251953125

bought 1 shares. Total cash spent: 2101.2066497802734. Current cash: 1793.5333251953125. Networth: 2102.8533325195312

sold 1 shares. Total cash spent: 2101.2066497802734. Current cash: 2096.4033203125. Networth: 2096.4033203125

bought 1 shares. Total cash spent: 2405.626663208008. Current cash: 2096.4033203125. Networth: 2400.8233337402344

sold 1 shares. Total cash spent: 2405.626663208008. Current cash: 2384.9933166503906. Networth: 2384.9933166503906

Final report

Cash spent: 2405.626663208008

Final networth: 2384.9933166503906

Percentage change: -0.8577119165324566%

```







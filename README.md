## Stock Alert

The stock alert app creates alerts on your  screen whenever stocks reflect your technical analysis conditionality. It is created using [chartink](https://chartink.com) which is used to create technical tools for Indian stock market. This web app provides free screeners for weekly, monthly trades. Also, the app creates alerts only if the stock belongs to nifty50 list to avoid unecessary alerts of countless stocks.

The app.py file is the main file to run the app. The app runs using [selenium's Firefox webdriver (geckodriver v0.26)](https://github.com/mozilla/geckodriver/releases/tag/v0.26.0).

|File|Description|
|----|-----------|
|app.py|Main file that runs the entire app|
|get_nifty50.py|Used to get data of nifty 50 stocks from [nseindia](https://www1.nseindia.com/products/content/derivatives/equities/fo_underlying_home.htm) and store the data in nse_nifty50.txt and nifty50tickers.pickle |
|requirements.txt| All external libraries to be downloaded|

#### Screenshot of Alert
<img src="https://github.com/AshishOhri/stock-alert/blob/master/capture.JPG" width="400px">

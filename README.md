## Stock Alert

The stock alert app is created using [chartink](https://chartink.com) which is used to create technical tools for Indian stock market. This app provides screeners for free as long as realtime data is not required. In other words, the alert focuses on weekly, monthly trades giving alerts on your screen. Also, the app is creates alerts if the stock belongs to nifty50 list to avoid unecessary alerts of countless stocks.

The app.py file is the main file to run the app. The app runs using [selenium's Firefox webdriver (geckodriver v0.26)](https://github.com/mozilla/geckodriver/releases/tag/v0.26.0).

|File|Description|
|----|-----------|
|app.py|Main file to run the file.|
|get_nifty50.py|Used to get data of nifty 50 stocks from [nseindia](https://www1.nseindia.com/products/content/derivatives/equities/fo_underlying_home.htm) and store the data in nse_nifty50.txt and nifty50tickers.pickle |
|requirements.txt| All external libraries to be downloaded|

#### Screenshot of Alert
<img src="https://github.com/AshishOhri/stock-alert/blob/master/capture.JPG" width="400px">

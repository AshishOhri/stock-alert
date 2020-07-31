from selenium import webdriver
import time
import pickle
import bs4 as bs

def get_nse_nifty50(): 
    browser=webdriver.Firefox(executable_path=r'.\geckodriver-v0.26.0-win64\geckodriver.exe')
    browser.get('https://www1.nseindia.com/products/content/derivatives/equities/fo_underlying_home.htm')
    time.sleep(15)
    html=browser.page_source
    browser.close()
    with open('nse_nifty50.txt','w') as f:
        f.write(html)

def get_nifty50_tickers():
    with open('nse_nifty50.txt','r') as f:
        html=f.read()
    soup=bs.BeautifulSoup(html,'lxml')
    table=soup.find('tbody')
    tickers=[]
    temp,fl=0,0
    for row in table.findAll('td',{'class':'normalText'}):
        text=row.get_text()
        if fl:
            if temp&1:
                tickers.append(text[:-1])
            temp=(temp+1)%2
        elif text=='Derivatives on Individual Securities':
            fl=1
    with open("nifty50tickers.pickle","wb") as f:
        pickle.dump(tickers,f)
if __name__=='__main__':
    get_nse_nifty50()
    get_nifty50_tickers()

import tkinter as tk

from selenium import webdriver
import time
import bs4 as bs
import pickle


def alert_popup(title,message,path):
    root=tk.Tk()
    root.title(title)

    w=400
    h=200

    sw=root.winfo_screenwidth()
    sh=root.winfo_screenheight()

    x=(sw-w)-10
    y=(sh-h)-80

    root.geometry('%dx%d+%d+%d'%(w,h,x,y))

    m=message
    m+='\n'
    m+=path
    w=tk.Label(root,text=m,width=120,height=10)
    w.pack()
##    b=tk.Button(root,text="Close",command=root.destroy,width=10)
##    b.pack()
    root.lift()
    tk.mainloop()

with open('nifty50tickers.pickle','rb') as f:
    tickers=pickle.load(f)
tickers=set(tickers)

browser=webdriver.Firefox(executable_path=r'.\geckodriver-v0.26.0-win64\geckodriver.exe')
browser.get('https://chartink.com/screener/52-week-breakout-1')
prev_display_text=''
prev=set()
try:
    while True:
        time.sleep(10)
        new_prev=set()
        display_text=''
        while True:
            html=browser.page_source
            soup=bs.BeautifulSoup(html,'html.parser')
            table=soup.findAll('tbody')[1]
            data=table.findAll('tr')

            for table_data in data:
                row=table_data.findAll('td')
                if row[2].text in tickers:
                    if row[2].text not in prev:
                        print(row[1].text,row[2].text)
                        display_text+=row[1].text+'  '+row[2].text+'\n'
                    new_prev.add(row[2].text)
            if 'disabled' in soup.find('li',{'class':'next'})['class']:
                break
            browser.execute_script("document.getElementsByClassName('next')[0].click();")
            time.sleep(1)
##        print(display_text)
        if prev_display_text!=display_text:
            alert_popup("ALERT",display_text,"")
            prev_display_text=display_text
        prev=new_prev
        time.sleep(10)
        browser.execute_script("document.getElementsByClassName('run_scan_button')[0].click()")
finally:
    browser.close()



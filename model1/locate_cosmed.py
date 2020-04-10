import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from lxml import html
from time import sleep
import time,datetime
import json
from Crawler_log import model_log

def store_info():
    driver = webdriver.Chrome()
    url = 'https://www.cosmed.com.tw/api/getStore.aspx?t=store&c=&d=&s='
    driver.get(url)

    model_list = []
    data = driver.find_elements_by_xpath("//pre")

    a = json.loads(data[0].text)
    for i in range(0,len(a['data'])):
        name = a['data'][i]['StoreNM']
        address = a['data'][i]['Address']
        tel = a['data'][i]['Tel']

        Data = [name,address,tel]
        model_list.append(Data)

    print(model_list)
    driver.close()

    ISOTIMEFORMAT = '%Y'+'%m'
    theTime = datetime.datetime.now().strftime(ISOTIMEFORMAT)
    theTime = theTime[2:]
    print('抓資料當日的西元年末兩位和月份:'+ theTime)

    cosmed_Dic = model_list
    columns = ["店名","地址","電話"]
    cosmed_Dic_df = pd.DataFrame(cosmed_Dic , columns=columns)
    cosmed_Dic_df.to_csv(str(theTime)+"COSMED.csv",encoding="utf-8-sig",index=False)

try:
    store_info()
    model_log(__file__,1)
except:
    model_log(__file__,0)
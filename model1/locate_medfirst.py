import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from lxml import html
from time import sleep
import time,datetime
from Crawler_log import model_log

def store_info():
    driver = webdriver.Chrome()
    url = 'https://event.medfirst.com.tw/StoreMap/Storelist.aspx'
    driver.get(url)
    model_list = []

    name = driver.find_elements_by_xpath("//div[@id='list']/div[@class='store_area shop display_store']/div[@class='row']/div[@class='col-xs-10 col-sm-11 col-md-10']/h1")
    adress = driver.find_elements_by_xpath("//div[@id='list']/div[@class='store_area shop display_store']/div[@class='row']/div[@class='col-xs-10 col-sm-11 col-md-10']/table[@class='store_info']/tbody/tr[1]/td/a")
    phone = driver.find_elements_by_xpath("//div[@id='list']/div[@class='store_area shop display_store']/div[@class='row']/div[@class='col-xs-10 col-sm-11 col-md-10']/table[@class='store_info']/tbody/tr[2]/td/a")
    print(len(name))
    print(len(adress))
    print(len(phone))
    for i in range(0,len(name)):
        Data = [name[i].text,adress[i].text,phone[i].text]
        model_list.append(Data)

    print(model_list)

    driver.close()

    ISOTIMEFORMAT = '%Y'+'%m'
    theTime = datetime.datetime.now().strftime(ISOTIMEFORMAT)
    theTime = theTime[2:]
    print('抓資料當日的西元年末兩位和月份:'+ theTime)

    medfirst_Dic = model_list
    columns = ["店名","地址","電話"]
    medfirst_df = pd.DataFrame(medfirst_Dic , columns=columns)
    medfirst_df.to_csv(str(theTime)+"杏一醫療用品.csv",encoding="utf-8-sig",index=False)

try:
    store_info()
    model_log(__file__,1)
except:
    model_log(__file__,0))
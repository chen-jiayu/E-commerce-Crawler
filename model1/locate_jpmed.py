import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from lxml import html
from time import sleep
import time,datetime
from Crawler_log import model_log

def store_info():
    driver = webdriver.Chrome()
    url = 'https://www.jpmed.com.tw/zh-TW/store'
    driver.get(url)
    model_list = []

    name = driver.find_elements_by_xpath("//form[@method='post']/div[@class='contentWrap']/div[@class='dtWrap']/div[@class='dtWrap']/div[@class='mainContent']/div[@class='right_content']/div[@class='right_item']/div[@class='storeList']/div[@class='storeBox']/p[@class='storeBox_name']")
    adress = driver.find_elements_by_xpath("//form[@method='post']/div[@class='contentWrap']/div[@class='dtWrap']/div[@class='dtWrap']/div[@class='mainContent']/div[@class='right_content']/div[@class='right_item']/div[@class='storeList']/div[@class='storeBox']/p[@class='storeBox_addr']/span/a")
    phone = driver.find_elements_by_xpath("//form[@method='post']/div[@class='contentWrap']/div[@class='dtWrap']/div[@class='dtWrap']/div[@class='mainContent']/div[@class='right_content']/div[@class='right_item']/div[@class='storeList']/div[@class='storeBox']/p[@class='storeBox_tel']/a")

    for i in range(0,len(name)):
        Data = [name[i].text,adress[i].text,phone[i*2].text]
        model_list.append(Data)

    print(model_list)

    driver.close()
    ISOTIMEFORMAT = '%Y'+'%m'
    theTime = datetime.datetime.now().strftime(ISOTIMEFORMAT)
    theTime = theTime[2:]
    print('抓資料當日的西元年末兩位和月份:'+ theTime)

    jpmed_Dic = model_list
    columns = ["店名","地址","電話"]
    jpmed_df = pd.DataFrame(jpmed_Dic , columns=columns)
    jpmed_df.to_csv(str(theTime)+"locate_Jpmed.csv",encoding="utf-8-sig",index=False)

try:
    store_info()
    model_log(__file__,1)
except:
    model_log(__file__,0)
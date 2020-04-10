import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from lxml import html
from time import sleep
import time,datetime
from Crawler_log import model_log

def store_info():
    driver = webdriver.Chrome()
    url = 'http://www.helthin99.com/about.asp?in=253'
    driver.get(url)
    model_list = []
    name_list=[]
    list = driver.find_elements_by_xpath("//div[@id='page']/article[@id='main_content']/article[@id='Right_blocks']/div[@class='right_content']/div[@class='right_mainpages']/div[@class='editorPages']/div[@align='center']/div[@align='center']/table[@align='center']/tbody/tr")
    count = 1
    for i in range(0,len(list)):
        try:
            if len(list[i].text)<=4:
                continue
            if i == 0:
                continue
            if i == 23:
                str1 = list[i].text
                arr = str1.split( )
                # print(str1)
                data = [arr[0]+arr[1],arr[2],arr[3]]
                # print(arr)
            else:
                str1 = list[i].text
                arr = str1.split( )
                data = [arr[0],arr[2],arr[1]]
                model_list.append(data)
                print(data)
        except Exception as e:
            continue
    driver.close()

    ISOTIMEFORMAT = '%Y'+'%m'
    theTime = datetime.datetime.now().strftime(ISOTIMEFORMAT)
    theTime = theTime[2:]
    print('抓資料當日的西元年末兩位和月份:'+ theTime)

    helthin_Dic = model_list
    columns = ["店名","地址","電話"]
    helthin_df = pd.DataFrame(helthin_Dic , columns=columns)
    helthin_df.to_csv(str(theTime)+"美的適生活藥妝.csv",encoding="utf-8-sig",index=False)
try:
    # helthin_df.to_csv("../output/美的適生活藥妝.csv",encoding="utf-8-sig",index=False)
    store_info()
    model_log(__file__,1)
except:
    model_log(__file__,0)
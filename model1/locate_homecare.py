import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from lxml import html
from time import sleep
import time,datetime
from Crawler_log import model_log

def store_info():
    driver = webdriver.Chrome()
    url_list= ['%A5x%A4j%AA%F9%A5%AB','%B0%EA%AE%F5%AA%F9%A5%AB','%B8p%AE%E7%AA%F9%A5%AB','%AAL%A4f%AA%F9%A5%AB','%A4%A4%B0%EA%AA%F9%A5%AB','%AA%E1%BD%AC%AA%F9%A5%AB','%B7%A3%B1%EA%AA%F9%A5%AB','%B0%AA%B6%AF%AA%F9%A5%AB']
    url = 'http://www.homecare.com.tw/ec/s1_map_01.asp?name='

    model_list = []
    for i in range(0,len(url_list)):
        try:
            driver.get(url+str(url_list[i]))

            name = driver.find_elements_by_xpath("//div[@align='center']/table/tbody/tr[@valign='top']/td[2]/table/tbody/tr[2]/td[2]/div[@style='width:650px']/div[@style='border:1px solid #66DD00']/div[@style='margin: auto 10px']/p/table/tbody/tr/td/table/tbody/tr/td/table[@bgcolor='#e1e1e1']/tbody/tr[1]/td[@bgcolor='#ffffff']/div[@style='background:#FFFFFF']")
            address = driver.find_elements_by_xpath("//div[@align='center']/table/tbody/tr[@valign='top']/td[2]/table/tbody/tr[2]/td[2]/div[@style='width:650px']/div[@style='border:1px solid #66DD00']/div[@style='margin: auto 10px']/p/table/tbody/tr/td/table/tbody/tr/td/table[@bgcolor='#e1e1e1']/tbody/tr[2]/td[2]")
            tel = driver.find_elements_by_xpath("//div[@align='center']/table/tbody/tr[@valign='top']/td[2]/table/tbody/tr[2]/td[2]/div[@style='width:650px']/div[@style='border:1px solid #66DD00']/div[@style='margin: auto 10px']/p/table/tbody/tr/td/table/tbody/tr/td/table[@bgcolor='#e1e1e1']/tbody/tr[3]/td[2]")

            a = name[0].text
            b = address[0].text
            c = tel[0].text
            Data = [a,b,c]
            model_list.append(Data)
            sleep(1)
        except IndexError as error:
            driver.refresh()


    print(model_list)
    driver.close()

    ISOTIMEFORMAT = '%Y'+'%m'
    theTime = datetime.datetime.now().strftime(ISOTIMEFORMAT)
    theTime = theTime[2:]
    print('抓資料當日的西元年末兩位和月份:'+ theTime)

    homeCare_Dic = model_list
    columns = ["店名","地址","電話"]
    homeCare_df = pd.DataFrame(homeCare_Dic , columns=columns)
    homeCare_df.to_csv(str(theTime)+"HOMECARE.csv",encoding="utf-8-sig",index=False)

try:
    store_info()
    model_log(__file__,1)
except:
    model_log(__file__,0)

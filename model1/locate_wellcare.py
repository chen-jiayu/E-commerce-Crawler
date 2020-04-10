import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from lxml import html
from time import sleep
import time,datetime
from Crawler_log import model_log

def store_info():
    driver = webdriver.Chrome()
    url = 'http://www.wellcare.com.tw/wellindex/03map_old.htm'
    driver.get(url)
    model_list = []
    city=['基隆','台北','桃園','新北','宜蘭','新竹','苗栗','台中','花蓮','南投','彰化','雲林','嘉義','台東','高雄','屏東']

    map = driver.find_elements_by_xpath("//map[@name='Map6']/area")
    for i in range(0,len(map)):
        driver.get(url)
        map = driver.find_elements_by_xpath("//map[@name='Map6']/area")
        detailHref = map[i].get_attribute('href')
        sleep(1)
        driver.get(detailHref)
        model = driver.find_elements_by_xpath("//table/tbody/tr[2]/td/table[@width='245']/tbody/tr/td[@class='style7']/a")
        for j in range(0,len(model)):
            try:
                Href = ''
                Href = model[j].get_attribute('href')
                # print(model[j].get_attribute('href'))
                driver.get(Href)
                name = driver.find_elements_by_xpath("//table/tbody/tr[13]/td[2]/table/tbody/tr[2]/td/span")
                address = driver.find_elements_by_xpath("//table/tbody/tr[13]/td[2]/table/tbody/tr[3]/td/table/tbody/tr/td[2]/table/tbody/tr[1]")
                tel = driver.find_elements_by_xpath("//table/tbody/tr[13]/td[2]/table/tbody/tr[3]/td/table/tbody/tr/td[2]/table/tbody/tr[2]")
                if city[i] in tel[0].text :
                    Data = [name[0].text,tel[0].text,address[0].text]
                    model_list.append(Data)
                else:
                    driver.get(detailHref)
                    model = driver.find_elements_by_xpath("//table/tbody/tr[2]/td/table[@width='245']/tbody/tr/td[@class='style7']/a")
                    continue
                    
                driver.get(detailHref)
                model = driver.find_elements_by_xpath("//table/tbody/tr[2]/td/table[@width='245']/tbody/tr/td[@class='style7']/a")
            except Exception as e:
                driver.refresh()
                continue

    driver.close()

    ISOTIMEFORMAT = '%Y'+'%m'
    theTime = datetime.datetime.now().strftime(ISOTIMEFORMAT)
    theTime = theTime[2:]
    print('抓資料當日的西元年末兩位和月份:'+ theTime)

    wellcare = model_list
    columns = ["店名","地址","電話"]
    wellcare_df = pd.DataFrame(wellcare , columns=columns)
    wellcare_df.to_csv("維康醫療用品.csv",encoding="utf-8-sig",index=False)
    wellcare_df.to_csv(str(theTime)+"wellcare維康醫療用品.csv",encoding="utf-8-sig",index=False)

try:
    store_info()
    model_log(__file__,1)
except:
    model_log(__file__,0)

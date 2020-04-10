import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from lxml import html
from time import sleep
import time
# from Crawler_log import model_log

driver = webdriver.Chrome()
url = 'http://www.tomods.com.tw/stores'
driver.get(url)

model_list=[]

locate_href = driver.find_elements_by_xpath("//div[@class='site_wrapper']/div[@class='content_wrapper m-b-100']/div[@class='container']/div[@class='row']/div[@class='col-md-9 my-account']/div[@class='tab-content']/div[@role='tabpanel']/div/div/table[@class='table table-striped']/tbody/tr/td[1]/a")
lenHref = len(locate_href)
# a = locate_href[0].get_attribute('href') 
for i in range(0,lenHref):
    locate_href = driver.find_elements_by_xpath("//div[@class='site_wrapper']/div[@class='content_wrapper m-b-100']/div[@class='container']/div[@class='row']/div[@class='col-md-9 my-account']/div[@class='tab-content']/div[@role='tabpanel']/div/div/table[@class='table table-striped']/tbody/tr/td[1]/a")
    a = locate_href[i].get_attribute('href') 
    driver.get(a)
    name = driver.find_element_by_xpath("//div[@class='site_wrapper']/div[@class='content_wrapper m-b-100']/div[@class='container']/div[@class='row']/div[@class='col-md-9 my-account']/div[@class='tab-content']/div[@role='tabpanel']/div/h3").text
    address = driver.find_element_by_xpath("//div[@class='site_wrapper']/div[@class='content_wrapper m-b-100']/div[@class='container']/div[@class='row']/div[@class='col-md-9 my-account']/div[@class='tab-content']/div[@role='tabpanel']/div/div[@class='store_content_info'][2]/span[@class='info_content']").text
    phone = driver.find_element_by_xpath("//div[@class='site_wrapper']/div[@class='content_wrapper m-b-100']/div[@class='container']/div[@class='row']/div[@class='col-md-9 my-account']/div[@class='tab-content']/div[@role='tabpanel']/div/div[@class='store_content_info'][3]/span[@class='info_block']").text
    Data = [name,address,phone]
    model_list.append(Data)
    driver.get('http://www.tomods.com.tw/stores')
    sleep(0.5)
print(model_list)

# driver.close()

# tomod_Dic = model_list
# columns = ["店名","地址","電話"]
# tomod_df = pd.DataFrame(tomod_Dic , columns=columns)
# tomod_df.to_csv("../output/locate_Tomod.csv",encoding="utf-8-sig",index=False)
# tomod_df.to_csv("locate_Tomod.csv",encoding="utf-8-sig",index=False)

# try:
#     tomod_df.to_csv("../output/Tomod三友藥妝.csv",encoding="utf-8-sig",index=False)
#     model_log(__file__,1)
# except:
#     model_log(__file__,0)
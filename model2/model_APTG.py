import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from lxml import html
from time import sleep
import time
# from create_folder import *

# store_path = check_folder()
driver = webdriver.Chrome()
idList=[150,170,240,300,360,390]
model_list=[]
url = 'https://eshop.aptg.com.tw/selectCat?tagId='
more_button=[]

for k in range(0,len(idList)):
    driver.get(url+str(idList[k]))
    sleep(5)
# 載入更多
    a=0
    while(a==0):
        more_button = driver.find_elements_by_xpath("//div[@class='gt-wrapper']/div[@class='gt gt-hp']/div[@class='gt-wrapper']/div[@class='gt-contents']/div[@class='container']/div[@class='text-center page-bottom-action']/a[@class='btn']")
        if len(more_button)>0:
            more_button[0].click()
        else:
            a=1
            break
    sleep(2)

    Model_href_name = driver.find_elements_by_xpath("//div[@class='gt-wrapper']/div[@class='gt gt-hp']/div[@class='gt-wrapper']/div[@class='gt-contents']/div[@class='container']/div[@class='plist-frame']/ul[@class='product-list']/li[@class='item price-t1']/div[@class='item-frame']/div[@class='text-area']/h5/span[@class='main-title']")
    Model_href_price = driver.find_elements_by_xpath("//div[@class='gt-wrapper']/div[@class='gt gt-hp']/div[@class='gt-wrapper']/div[@class='gt-contents']/div[@class='container']/div[@class='plist-frame']/ul[@class='product-list']/li[@class='item price-t1']/div[@class='item-frame']/div[@class='text-area']/h6/span[@class='price-text']")

    if len(Model_href_name) == len(Model_href_price):
        for i in range(0,len(Model_href_name)):
            name = Model_href_name[i].text
            price = Model_href_price[i].text
            a = ' '
            b = ' '
            Data = [name,a,b,price]
            model_list.append(Data)
            print("單購"+str(i))
    else:
        print('false')

    sleep(2)
    # 換搭門號
    element = driver.find_element_by_xpath("//input[@id='rc01']")
    driver.execute_script("arguments[0].click();", element)

    # 載入更多
    sleep(2)
    a=0
    while(a==0):
        more_button = driver.find_elements_by_xpath("//div[@class='gt-wrapper']/div[@class='gt gt-hp']/div[@class='gt-wrapper']/div[@class='gt-contents']/div[@class='container']/div[@class='text-center page-bottom-action']/a[@class='btn']")
        if len(more_button)>0:
            more_button[0].click()
        else:
            a=1
            break

    # 搭門號
    Model_href_name1 = driver.find_elements_by_xpath("//div[@class='gt-wrapper']/div[@class='gt gt-hp']/div[@class='gt-wrapper']/div[@class='gt-contents']/div[@class='container']/div[@class='plist-frame']/ul[@class='product-list']/li[@class='item ']/div[@class='item-frame']/div[@class='text-area']/h5/span[@class='main-title']")
    Model_href_price1 = driver.find_elements_by_xpath("//div[@class='gt-wrapper']/div[@class='gt gt-hp']/div[@class='gt-wrapper']/div[@class='gt-contents']/div[@class='container']/div[@class='plist-frame']/ul[@class='product-list']/li[@class='item ']/div[@class='item-frame']/div[@class='text-area']/h6/span[@class='price-text']")
    Model_href_price2 = driver.find_elements_by_xpath("//div[@class='gt-wrapper']/div[@class='gt gt-hp']/div[@class='gt-wrapper']/div[@class='gt-contents']/div[@class='container']/div[@class='plist-frame']/ul[@class='product-list']/li[@class='item ']/div[@class='item-frame']/div[@class='text-area']/p/span[@class='xs-brick']")
    Model_href_price3 = driver.find_elements_by_xpath("//div[@class='gt-wrapper']/div[@class='gt gt-hp']/div[@class='gt-wrapper']/div[@class='gt-contents']/div[@class='container']/div[@class='plist-frame']/ul[@class='product-list']/li[@class='item ']/div[@class='item-frame']/div[@class='text-area']/p/span[@class='price-text color-red']")
    sleep(2)
    if len(Model_href_name1) == len(Model_href_price3):
        for i in range(0,len(Model_href_name1)):
            name = Model_href_name1[i].text
            price1 = Model_href_price1[i].text
            price2 = str(Model_href_price2[i].text)[2:-1]
            price3 = Model_href_price3[i].text
            Data = [name,price2,price3,price1]
            model_list.append(Data)
            print("搭門號"+str(i))
    else:
        print('false')
    
    print(model_list) 
driver.close()

aptg_Dic = model_list
columns = ["Model","資費","專案費","建議售價"]
aptg_df = pd.DataFrame(aptg_Dic , columns=columns)
aptg_df.to_csv("APTG.csv",encoding="utf-8-sig" ,index = False)
# aptg_df.to_csv(store_path+"APTG.csv",encoding="utf-8-sig" ,index = False)


import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from lxml import html
from time import sleep
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
# from create_folder import *

# store_path = check_folder()

driver = webdriver.Chrome()
url = 'https://www.sinya.com.tw/show/'
url_list=['18','67','19','7','12','93','27','73','23','1']
url_name=['筆記型電腦及週邊','Apple旗艦店','桌上型電腦','顯示器','周邊館','家電館','手機/平板/穿戴型裝置','數位週邊','相機攝影機','電腦零組件']
model_list = []

for k in range(0,len(url_list)):
    driver.get(url+url_list[k])
    select_page = driver.find_elements_by_xpath("//div[@class='container main show']/div[@class='row prodRow']/div[@class='col-md-3 col-xs-12 prodSidebar']/div[@class='moreSearchBox']/div[@class='moreSearchArea']/div[@class='selectArea']/select[@id='sub_category']/option")
    select_len=len(select_page)
    star = 0
    # apple 不需周邊
    if k == 1:
        select_len = 4
    # 家電館第一類到第二類有bug
    if k == 5:
        star = 1
    for j in range(star,select_len):
        number = j
        try:
            select_page = driver.find_elements_by_xpath("//div[@class='container main show']/div[@class='row prodRow']/div[@class='col-md-3 col-xs-12 prodSidebar']/div[@class='moreSearchBox']/div[@class='moreSearchArea']/div[@class='selectArea']/select[@id='sub_category']/option")
            while(len(select_page)==0):
                driver.back()
                select_page = driver.find_elements_by_xpath("//div[@class='container main show']/div[@class='row prodRow']/div[@class='col-md-3 col-xs-12 prodSidebar']/div[@class='moreSearchBox']/div[@class='moreSearchArea']/div[@class='selectArea']/select[@id='sub_category']/option")
            category_name = select_page[j].text
            select_page[j].click()
        except Exception as e:
            continue
        x=1
        a=0
        page_count1 = driver.find_elements_by_xpath("//div[@class='container main show']/div[@class='row prodRow']/div[@class='col-md-9 col-xs-12']/div[@class='row']/div[@class='col-md-12']/nav/ul[@class='pagination']/li")
        page_count = len(page_count1) - 2
        while(a==0):
            try:
                model_detail_name = driver.find_elements_by_xpath("//div[@class='container main show']/div[@class='row prodRow']/div[@id='prodMainArea']/div[@class='showProdArea']/div[@id='search_list_item']/div[@class='col-md-3 col-xs-6 item_box']/div[@class='showProdBox']/a/div[@class='showProdInfo']/div[@class='showProdName']")
                model_detail_price = driver.find_elements_by_xpath("//div[@class='container main show']/div[@class='row prodRow']/div[@id='prodMainArea']/div[@class='showProdArea']/div[@id='search_list_item']/div[@class='col-md-3 col-xs-6 item_box']/div[@class='showProdBox']/a/div[@class='showProdInfo']/div[@class='showProdPriceArea']/span")
                for i in range(0,len(model_detail_name)):
                    Data = [url_name[k],category_name,model_detail_name[i].text,model_detail_price[i].text]
                    model_list.append(Data)       
                print(url_name[k],j,x,page_count)
                next_page = driver.find_element_by_xpath("//div[@class='container main show']/div[@class='row prodRow']/div[@class='col-md-9 col-xs-12']/div[@class='showInfo']/div[@class='showIconArea']/button[@class='btn']/span[@class='iconMoon icon-chevron-right']")
                if x == page_count :
                    break
                # x = x+1
                while(next_page == ''):
                    next_page = driver.find_element_by_xpath("//div[@class='container main show']/div[@class='row prodRow']/div[@class='col-md-9 col-xs-12']/div[@class='showInfo']/div[@class='showIconArea']/button[@class='btn']/span[@class='iconMoon icon-chevron-right']")
                x = x+1
                next_page.click()
                # time.sleep(1)
            except ElementClickInterceptedException as e:
                print(j,'error')
                driver.refresh()
                # print('qqq')
                time.sleep(0.5)
                # next_page = driver.find_element_by_xpath("//div[@class='container main show']/div[@class='row prodRow']/div[@class='col-md-9 col-xs-12']/div[@class='showInfo']/div[@class='showIconArea']/button[@class='btn']/span[@class='iconMoon icon-chevron-right']")
                # next_page.click()
                continue
            except NoSuchElementException as e:
                driver.back()
                print('end page')
                a=1
        time.sleep(1)
    time.sleep(1)
    
print(model_list)
driver.close()

sinya_Dic = model_list
columns = ["category1","category2","product","price"]
sinya_df = pd.DataFrame(sinya_Dic , columns=columns)
sinya_df.to_csv("SINYA.csv",encoding="utf-8-sig",index = False)
# sinya_df.to_csv(store_path+"SINYA.csv",encoding="utf-8-sig",index = False)
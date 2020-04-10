import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from lxml import html
from time import sleep
import time
from create_folder import *

store_path = check_folder()
driver = webdriver.Chrome()
idList=['2500500059/Mc','2700400006/吸塵器掃地機','2701000007/吹風機護髮吹風機','2701000002/鼻毛刀刮鬍刀','2701000006/電動音波牙刷沖牙機','2700400007/空氣清淨機',
'2700400008/除濕機','2700900003/電鍋電子鍋','2700900008/咖啡機調理機果汁機','2700900004/烤箱烤麵包機',
'2700900002/微波爐氣炸鍋','2700900010/濾飲水淨水設備','2700900009/熱水瓶快煮壺開飲機','2500500000/APPLE','2600100000/手機','2600400000/相機','2600600000/單眼相機鏡頭'
]
model_list=[]
url = 'https://www.momomall.com.tw/s/category/'
driver.get(url+idList[0])
count = 0
a=0
while(a==0):
    if count == len(idList):
        break
    try:
        name = driver.find_elements_by_xpath("//div[@class='categoriesHome']/div[@class='searchResults']/div[@class='w1220Area']/div[@id='bt_2_layout_Content']/div[@id='bt_2_layout_b2']/div[@class='prdListArea']/ul[@class='list']/li/a/p[2]")
        price = driver.find_elements_by_xpath("//div[@class='categoriesHome']/div[@class='searchResults']/div[@class='w1220Area']/div[@id='bt_2_layout_Content']/div[@id='bt_2_layout_b2']/div[@class='prdListArea']/ul[@class='list']/li/a/p[3]/b")
        for i in range(0,len(name)):
            Data = [name[i].text,price[i].text]
            model_list.append(Data)
        # print(model_list)
        next_page = driver.find_element_by_xpath("//div[@class='categoriesHome']/div[@class='searchResults']/div[@class='w1220Area']/div[@id='bt_2_layout_Content']/div[@id='bt_2_layout_b2']/div[@class='pageArea topPageArea']/dl/dd[@id='next_page_str2']/a")
        next_page.click()
    except Exception as e:
        if count == len(idList)-1:
            break
        count = count+1
        driver.get(url+idList[count])

print(model_list)
driver.close()

momo_Dic = model_list
columns = ["model","price"]
momo_df = pd.DataFrame(momo_Dic , columns=columns)
momo_df.to_csv("Momo.csv",encoding="utf-8-sig",index = False)
momo_df.to_csv(store_path+"Momo.csv",encoding="utf-8-sig",index = False)


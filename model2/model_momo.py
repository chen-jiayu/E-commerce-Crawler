import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from lxml import html
from time import sleep
import time
# from create_folder import *

# store_path = check_folder()
driver = webdriver.Chrome()
threec =['1912900000','1905200000','1908900000','1902200000','4200100000','4200200000','4200300000','4200500000']
applince = ['2902000000&FTOOTH=29&Area=tooth&mdiv=1099600000-bt_0_996_11-&ctype=B','2904900000&mdiv=1099600000-bt_0_996_11-&ctype=B','2903100000&FTOOTH=29&Area=tooth&mdiv=1099600000-bt_0_996_11-&ctype=B','2901400000&FTOOTH=29&Area=tooth&mdiv=1099600000-bt_0_996_11-&ctype=B','2900500000&FTOOTH=29&Area=tooth&mdiv=1099600000-bt_0_996_11-&ctype=B','2902300000&FTOOTH=29&Area=tooth&mdiv=1099600000-bt_0_996_11-&ctype=B','2905700000&mdiv=1099600000-bt_0_996_11-&ctype=B','2903200000&FTOOTH=29&Area=tooth&mdiv=1099600000-bt_0_996_11-&ctype=B','2906500000&mdiv=1099600000-bt_0_996_11-&ctype=B','2900400000&FTOOTH=29&Area=tooth&mdiv=1099600000-bt_0_996_11-&ctype=B','2901700000&FTOOTH=29&Area=tooth&mdiv=1099600000-bt_0_996_11-&ctype=B','2900200000&FTOOTH=29&Area=tooth&mdiv=1099600000-bt_0_996_11-&ctype=B','2904500000&FTOOTH=29&Area=tooth&mdiv=1099600000-bt_0_996_11-&ctype=B','2901600000&FTOOTH=29&Area=tooth&mdiv=1099600000-bt_0_996_11-&ctype=B']
model_list=[]
model = ['智慧型手機','iPhone','iPad','一般手機','微單眼','單眼相機','數位相機','單眼鏡頭','清淨機','除濕機','電鍋/電子鍋','冷/熱食物調理','咖啡機','烤箱/微波爐','快煮壺/熱水瓶','飲水設備','淨水設備','吹風機/造型美髮','美容電器','潔牙/電動牙刷','刮鬍刀']
url = 'https://www.momoshop.com.tw/category/LgrpCategory.jsp?l_code='
# len(threec)+len(applince)
for k in range(19,21):
    if k >= len(threec):
        driver.get(url+applince[k-len(threec)])
    if k < len(threec):
        driver.get(url+threec[k]+'&mdiv=1099600000-bt_0_996_10-&ctype=B')
    sleep(3)
    select1 = driver.find_elements_by_xpath("//div[@id='BodyBase']/div[3]/div[@class='bt_2_layout_Left']/div[@id='bt_2_layout_G']/div[@id='attributesBrandsArea']/div/ul/li[@class='cateS']/input")
    more = driver.find_elements_by_xpath("//div[@id='BodyBase']/div[3]/div[@class='bt_2_layout_Left']/div[@id='bt_2_layout_G']/div[@id='attributesBrandsArea']/div/ul/li[@class='More']/a")
    select2 = driver.find_elements_by_xpath("//div[@id='BodyBase']/div[3]/div[@class='bt_2_layout_Left']/div[@id='bt_2_layout_G']/div[@id='attributesBrandsArea']/div/ul/li[@class='cateS hide']/input")
    sleep(2)
    if len(more)>0:
        more[0].click()
    sleep(2)
    # print(len(select1))
    try:
        for i in range(0,len(select1)):
            select1[i].click()
            sleep(0.5)
    except Exception as e:
        continue
    if len(select2)>0:
        for j in range(0,len(select2)):
            select2[j].click()
            sleep(0.5)   
    a=1
    detail_href=[]
    b = 0
    while(a!=0):
        try:
            href1 = driver.find_elements_by_xpath("//div[@id='BodyBase']/div[3]/div[@class='bt_2_layout_Content']/div[@id='goodsAttrRoot']/div[@class='prdListArea bt770class']/ul/li/a")
            for j in range(0,len(href1)):
                ahref = href1[j].get_attribute('href')
                detail_href.append(ahref)
            element = driver.find_element_by_link_text("下一頁")
            driver.execute_script("arguments[0].click();", element)
            b = b+1
            sleep(2)
            if b==2:
                break
        except Exception as e:
            print('end page')
            break
        print(len(href1))
    for i in range(0,len(detail_href)):
        driver.get(detail_href[i])
        # sleep(1)
        name = driver.find_elements_by_xpath("//div[@id='BodyBase']/div[3]/div[@class='bt_2_layout_Content']/form[@id='productForm']/div[@class='prdwarp']/div[@class='prdnoteArea']/h1")
        price = driver.find_elements_by_xpath("//div[@id='BodyBase']/div[3]/div[@class='bt_2_layout_Content']/form[@id='productForm']/div[@class='prdwarp']/div[@class='prdnoteArea']/ul[@class='prdPrice']/li[@class='special']/span")
        area1 = driver.find_elements_by_xpath("//div[@id='BodyBase']/div[3]/div[@class='bt_2_layout_Content']/form[@id='productForm']/div[@class='prdwarp']/div[@class='prdnoteArea']/ul[@class='ineventArea']/li[1]")
        area2 = driver.find_elements_by_xpath("//div[@id='BodyBase']/div[3]/div[@class='bt_2_layout_Content']/form[@id='productForm']/div[@class='prdwarp']/div[@class='prdnoteArea']/ul[@class='ineventArea']/li[2]")
        if len(name) < 0:
            name = driver.find_elements_by_xpath("//div[@id='BodyBase']/div[3]/div[@class='bt_2_layout_Content']/form[@id='productForm']/div[@class='prdwarp']/div[@class='prdnoteArea']/p/h1")
        if len(area1) > 0 :
            area11 = area1[0].text
        if len(area2) > 0 :
            area21 = area2[0].text
        else :
            area11 = ' '
            area21 = ' '
        try:
            name1 = name[0].text
            price1 = price[0].text
            Data = [model[k],name1,price1,area11,area21]
            model_list.append(Data)
            sleep(1)
        except Exception as e:
            print(e)
            print(i)
            continue
        
driver.close()
print(model_list)

momo_Dic = model_list
columns = ["model","name","price","remark1","remark2"]
momo_df = pd.DataFrame(momo_Dic , columns=columns)
momo_df.to_csv("Momo.csv",encoding="utf-8-sig",index = False)
# momo_df.to_csv(store_path+"Momo.csv",encoding="utf-8-sig",index = False)


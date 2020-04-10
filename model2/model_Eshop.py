import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from lxml import html
from time import sleep
from selenium.common import exceptions  
# from create_folder import *

# store_path = check_folder()
driver = webdriver.Chrome()
url = 'https://eshop.fayaque.com.tw/product/'
driver.get(url)
model_list=[]

model_class = driver.find_elements_by_xpath("//div[@class='top-bar']/div[@class='menu']/div[@class='menu-wrapper']/div[@class='menu-wrapper-top']/div[@class='top-content']/ul[@class='main-menu']/li[@class='menu-item']/a")
sleep(1)
print(len(model_class))
for k in range(0,len(model_class)):
    a=k
    model_class_name = model_class[k].get_attribute('text')
    print(model_class_name)
    sleep(2)
    model_class[k].click()
    # print(len(model_class))
    real = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        sleep(2)
        now = driver.execute_script("return document.body.scrollHeight")
        if now == real :
            break
        real = now

    product_name = driver.find_elements_by_xpath("//div[@class='sub-wrapper product-page']/div[@class='content-bottom']/div[@class='sub-grid']/div[@id='grid']/div/div[@class='mask mask_table_list']/div[@class='btn-groups']/p[@class='description']/a")
    product_price = driver.find_elements_by_xpath("//div[@class='sub-wrapper product-page']/div[@class='content-bottom']/div[@class='sub-grid']/div[@id='grid']/div/div[@class='mask mask_table_list']/div[@class='btn-groups']/span[@class='money']")

    # print(len(product_name))
    # print(len(product_price))
    if len(product_name) == len(product_price):
        for i in range(0,len(product_name)):
            try:
                name = product_name[i].text
                price = product_price[i].text
                Data = [model_class_name,name,price]
                # print(i)
                sleep(0.01)
                model_list.append(Data)
            except Exception as e:
                print(e)
                print(i)
                pass
    else:
        k=a


    sleep(2)
    driver.back()
    sleep(1)
    model_class = driver.find_elements_by_xpath("//div[@class='top-bar']/div[@class='menu']/div[@class='menu-wrapper']/div[@class='menu-wrapper-top']/div[@class='top-content']/ul[@class='main-menu']/li[@class='menu-item']/a")

print(model_list)
driver.close()

eshop_Dic = model_list
columns = ["分類","商品名稱","價格"]
eshop_df = pd.DataFrame(eshop_Dic , columns=columns)
eshop_df.to_csv("Eshop.csv",encoding="utf-8-sig",index = False)

# eshop_df.to_csv(store_path+"Eshop.csv",encoding="utf-8-sig",index = False)


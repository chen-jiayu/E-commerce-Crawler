import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from lxml import html
from time import sleep
import time
# from create_folder import *

# store_path = check_folder()
driver = webdriver.Chrome()
url = 'https://www.vivatv.com.tw/mcategory.go'
driver.get(url)
model_href = driver.find_elements_by_xpath("//div[@id='wrapper-top']/div[@class='category-list']/table/tbody/tr/td/a")
model_name = driver.find_elements_by_xpath("//div[@id='wrapper-top']/div[@class='category-list']/table/tbody/tr/td/a/table[@class='category-individual']/tbody/tr/td[2]")
# print(model_name[1].text)
lenModel = len(model_href)
model_list=[]
model_href[0].click()
a = 0
for k in range(0,lenModel):
    driver.get(url)
    model_href = driver.find_elements_by_xpath("//div[@id='wrapper-top']/div[@class='category-list']/table/tbody/tr/td/a")
    model_name = driver.find_elements_by_xpath("//div[@id='wrapper-top']/div[@class='category-list']/table/tbody/tr/td/a/table[@class='category-individual']/tbody/tr/td[2]")
    name = model_name[k].text
    model_href[k].click()
    while(a==0):
        title = driver.find_elements_by_xpath("//div[@id='wrapper-top']/div[@class='product-list']/div[@class='product-individual']/div[@class='product-info float-l']/a/h5[@class='name']")
        price = driver.find_elements_by_xpath("//div[@id='wrapper-top']/div[@class='product-list']/div[@class='product-individual']/div[@class='product-info float-l']/a/h5[@class='price']")
        for i in range(0,len(price)):
            Data = [name,title[i].text,price[i].text]
            model_list.append(Data)
        next_page = driver.find_element_by_xpath("//div[@id='wrapper-top']/div[@class='button_pages']/a")
        href = next_page.get_attribute('href')
        text = next_page.get_attribute('text')
        if(text == '下一頁'):
            driver.get(href)
            sleep(1)

        if(text == '上一頁'):
            break

print(model_list)
driver.close()

vivata_Dic = model_list
columns = ["category1","modelname1","ViVa售價"]
vivata_df = pd.DataFrame(vivata_Dic , columns=columns)
# vivata_df.to_csv(store_path+"VIVATA.csv",encoding="utf-8-sig",index = False)
vivata_df.to_csv("VIVATA.csv",encoding="utf-8-sig",index = False)
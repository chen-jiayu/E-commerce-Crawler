import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from lxml import html
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
# from create_folder import *

# store_path = check_folder()

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get('https://eshop.cht.com.tw/home/consumer/mobservice/device/smart-home')

final_list = []
# model 網址
model_list = []
Model_href = driver.find_elements_by_xpath("//div[@class='tab-container']/div[@class='tab-wrap owl-center-tab']/a")
for i in range(0,len(Model_href)):
    modelHref = Model_href[i].get_attribute('href')
    model_list.append(modelHref)

# detail 內容
detail_list = []
for i in range(0,len(model_list)):
    print('第'+str(i)+'個model')
    driver.get(model_list[i])
    detail_href = driver.find_elements_by_xpath("//div[@class='nekos grid-4 filter-section']/div[@class='neko']/div[@class='card-wrapper']/div[@class='card product']/a[@class='hash card-text content-center']")
    detail_href_hide = driver.find_elements_by_xpath("//div[@class='nekos grid-4 filter-section']/div[@class='neko']/div[@class='card-wrapper hide']/div[@class='card product']/a[@class='hash card-text content-center']")

    detailHref = ' '
    for j in range(0,len(detail_href)+len(detail_href_hide)):
        if j < len(detail_href):
            detailHref = detail_href[j].get_attribute('href')
            detail_list.append(detailHref)
        if j > len(detail_href)-1:
            detailHref = detail_href_hide[j-len(detail_href)].get_attribute('href')
            detail_list.append(detailHref)
        
    print(len(detail_href)+len(detail_href_hide))

for i in range(0,len(detail_list)):
    driver.get(detail_list[i])
    detailName = driver.find_element_by_xpath("//section[@class='device-detail']/div[@class='container without-padding']/div[@class='nekos']/div[@class='is-5 neko-center']/div[@class='card-wrapper']/div[@class='card']/div[@class='card-text']/h1[@id='h1_ProductName']").text
    detailPrice = driver.find_element_by_xpath("//section[@class='device-detail']/div[@class='container without-padding']/div[@class='nekos']/div[@class='is-5 neko-center']/div[@class='card-wrapper']/div[@class='card']/div[@class='card-text']/div[@class='product-price']/div[@class='h4']/span[@class='h2 is-orange']").text
    detailHighPrice = driver.find_element_by_xpath("//section[@class='device-detail']/div[@class='container without-padding']/div[@class='nekos']/div[@class='is-5 neko-center']/div[@class='card-wrapper']/div[@class='card']/div[@class='card-text']/div[@class='product-price']/div[@class='h4']/small[@class='is-gray']/del/span[@itemprop='highPrice']").text
    Data = [detailName,detailHighPrice,detailPrice]
    final_list.append(Data)
    print('第'+str(i)+'個detail_list')

print(final_list)
driver.close()

cht_Dic = final_list
columns = ["Model","Price","資費"]
cht_df = pd.DataFrame(cht_Dic , columns=columns)
cht_df.to_csv("CHT.csv",encoding="utf-8-sig",index = False)
# cht_df.to_csv(store_path+"CHT.csv",encoding="utf-8-sig",index = False)
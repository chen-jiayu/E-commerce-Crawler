import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from lxml import html
from time import sleep
import time
# from create_folder import *

# store_path = check_folder()
driver = webdriver.Chrome()
url = 'http://webserver3.crete.com.tw/pro.admin/'
url_list=['show_nb.asp','show_pc.asp','show_cp.asp','show_tb.asp','show_lcd.asp','show_pj.asp']
name_list = ['筆記型電腦','桌上型電腦','手機','平板','LCD','投影機']
model_list = []

for l in range(0,len(url_list)):
    driver.get(url+url_list[l])
    model_total = driver.find_elements_by_xpath("//table[@border='0']/tbody/tr/td/table[@border='0']/tbody/tr[@bgcolor='#3366CC']/td/table/tbody/tr/td/u/b")
    page = int(model_total[1].text)
    total= int(model_total[0].text)
    for k in range(0,page):
        try:
            print(url_list[l],k+1)
            model_yellowBrand = driver.find_elements_by_xpath("//table[@border='0']/tbody/tr/td/table[@border='0']/tbody/tr[@bgcolor='#FFFFBB']/td[3]")
            model_yellowDetail = driver.find_elements_by_xpath("//table[@border='0']/tbody/tr/td/table[@border='0']/tbody/tr[@bgcolor='#FFFFBB']/td/a")
            model_blueBrand = driver.find_elements_by_xpath("//table[@border='0']/tbody/tr/td/table[@border='0']/tbody/tr[@bgcolor='#C7ECFC']/td[3]")
            model_blueDetail = driver.find_elements_by_xpath("//table[@border='0']/tbody/tr/td/table[@border='0']/tbody/tr[@bgcolor='#C7ECFC']/td/a")
            if l == 1:
                model_yellowBrand = driver.find_elements_by_xpath("//table[@border='0']/tbody/tr/td/table[@border='0']/tbody/tr[@bgcolor='#FFFFBB']/td[2]")
                model_blueBrand = driver.find_elements_by_xpath("//table[@border='0']/tbody/tr/td/table[@border='0']/tbody/tr[@bgcolor='#C7ECFC']/td[2]")
            
            lenYellow = len(model_yellowBrand)
            lenBlue = len(model_blueBrand)


            for i in range(0,lenYellow):
                Data = [name_list[l], model_yellowBrand[i].text,model_yellowDetail[i].text]
                model_list.append(Data)
            for i in range(0,lenBlue):
                Data = [name_list[l],model_blueBrand[i].text,model_blueDetail[i].text]
                model_list.append(Data)
            if l == 0 and k == 16:
                driver.back()
                element = driver.find_element_by_xpath("//table[@border='0']/tbody/tr/td/table[@border='0']/tbody/tr[@bgcolor='#3366CC']/td/table/tbody/tr/td/a[contains(text(),'最末頁')]")
                driver.execute_script("arguments[0].click();", element)
                continue
                
            if k == page-1:
                break
        
            if l == 0 and k > 16:
                element = driver.find_element_by_xpath("//table[@border='0']/tbody/tr/td/table[@border='0']/tbody/tr[@bgcolor='#3366CC']/td/table/tbody/tr/td/a[contains(text(),'上一頁')]")
                driver.execute_script("arguments[0].click();", element)
                continue

            element = driver.find_element_by_xpath("//table[@border='0']/tbody/tr/td/table[@border='0']/tbody/tr[@bgcolor='#3366CC']/td/table/tbody/tr/td/a[contains(text(),'下一頁')]")
            driver.execute_script("arguments[0].click();", element)
            time.sleep(1)
        except Exception as e:
            continue
    
    time.sleep(1)

driver.get(url+url_list[0])
element = driver.find_element_by_xpath("//table[@border='0']/tbody/tr/td/table[@border='0']/tbody/tr[@bgcolor='#3366CC']/td/table/tbody/tr/td/a[contains(text(),'最末頁')]")
driver.execute_script("arguments[0].click();", element)

print(model_list)
driver.close()

crete_Dic = model_list
columns = ["Model1","Brand","Model2"]
crete_df = pd.DataFrame(crete_Dic , columns=columns)
crete_df.to_csv("CRETE.csv",encoding="utf-8-sig",index = False)
# crete_df.to_csv(store_path+"CRETE.csv",encoding="utf-8-sig",index = False)
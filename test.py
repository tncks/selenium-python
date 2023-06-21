import time

from timeloop import Timeloop
from datetime import timedelta
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import json
import os

with open("tt.json", "w") as f:
    json.dump([], f)

def write_json(new_data, filename='tt.json'):
    with open(filename, 'r+', encoding='utf-8') as file:
        file_data = json.load(file)
        file_data.append(new_data)
        file.seek(0)
        json.dump(file_data, file, ensure_ascii = False, indent = 4)

haksa_li = []
browser = webdriver.Chrome()
browser.get('https://www.mmu.ac.kr/main/board/302/1')
num=0
print('start while..')
# print while loop started!!;
while num<4:

        try:
            element = WebDriverWait(browser, 10).until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="content"]/div[3]/table/tbody/tr')))

            time.sleep(1)
        
            elem_list= browser.find_element(
                By.CSS_SELECTOR, "div.board")

            items = elem_list.find_elements(By.XPATH, '//*[@id="content"]/div[3]/table/tbody/tr')

            for item in items:
                no = item.find_element(By.CLASS_NAME, 'no').text
                title = item.find_element(By.CLASS_NAME, 'title').text
                
                #print('link is ')
                #print((link))
                #print(type(link))
                #print(type(title))
                name = item.find_element(By.CLASS_NAME, 'name').text
                date = item.find_element(By.CLASS_NAME, 'date').text
                hit = item.find_element(By.CLASS_NAME, 'hit').text
                link = item.find_element(By.CLASS_NAME, 'title').find_element(By.TAG_NAME, 'a').get_attribute('href')

                if no=="공지":
                    if num > 0:
                        continue
                
                
                haksa_li.append({
                    "no": no,
                    "title": title,
                    "name": name,
                    "date": date,
                    "hit": hit,
                    "link": link
                })

                write_json({
                    "no": no,
                    "title": title,
                    "name": name,
                    "date": date,
                    "hit": hit,
                    "link": link
                })

                
            
            
            
            num = num + 1
            print(num, end=' ')
            converted_num = ''.join(list(str(num+1)))
            browser.get('https://www.mmu.ac.kr/main/board/302/'+converted_num)
                
    
        except Exception as e:
            print(e, "Main Error in haksa")

print(".. haksa while loop ended!")
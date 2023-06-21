from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import time
import os

with open("hasung.json", "w") as f:
    json.dump([], f)

def write_json(new_data, filename='hasung.json'):
    with open(filename, 'r+', encoding='utf-8') as file:
        file_data = json.load(file)
        file_data.append(new_data)
        file.seek(0)
        json.dump(file_data, file, ensure_ascii = False, indent = 4)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
#chrome_options.add_argument("--no-sandbox")
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
browser.get('https://www.mmu.ac.kr/main/board/301/1') #haksa notice

num = 0

while num<8:

    try:
        element = WebDriverWait(browser, 10).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="content"]/div[3]/table/tbody/tr')))

        time.sleep(0.5)
    
        elem_list= browser.find_element(
            By.CSS_SELECTOR, "div.board")

        items = elem_list.find_elements(By.XPATH, '//*[@id="content"]/div[3]/table/tbody/tr')

        for item in items:
            no = item.find_element(By.CLASS_NAME, 'no').text
            title = item.find_element(By.CLASS_NAME, 'title').text
            name = item.find_element(By.CLASS_NAME, 'name').text
            date = item.find_element(By.CLASS_NAME, 'date').text
            hit = item.find_element(By.CLASS_NAME, 'hit').text

            if no=="공지":
                if num > 0:
                    continue
            
            write_json({
                "no": no,
                "title": title,
                "name": name,
                "date": date,
                "hit": hit,
            })
        
        
        
        num = num + 1
        print(num, end=' ')
        converted_num = ''.join(list(str(num+1)))
        browser.get('https://www.mmu.ac.kr/main/board/301/'+converted_num)
            
   
    except Exception as e:
        print(e, "Main Error")
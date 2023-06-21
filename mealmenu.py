from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

with open("meal.json", "w") as f:
    json.dump([], f)
with open("meal2.json", "w") as f:
    json.dump([], f)

def write_json(new_data, filename='meal.json'):
    with open(filename, 'r+', encoding='utf-8') as file:
        file_data = json.load(file)
        file_data.append(new_data)
        file.seek(0)
        json.dump(file_data, file, ensure_ascii = False, indent = 4)

browser = webdriver.Chrome()
browser.get('https://www.mmu.ac.kr/main/contents/todayMenu1')
wj = []

n = 0

try:
    temp = []
    element = WebDriverWait(browser, 10).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="content"]/div[3]/div/table/tbody/tr')))
    
    elem_list= browser.find_element(
            By.CSS_SELECTOR, "div.contents812")

    items = elem_list.find_elements(By.XPATH, '//*[@id="content"]/div[3]/div/table/tbody/tr')

    for item in items:
        cols = item.find_elements(By.XPATH, "//*[name()='td']")
        
        i = 0
        for col in cols:
            if i>3:
                temp.append(col.text)
            
            i = i + 1
        
        print("writing to file..")
        print("step", end='')
        print(n)
        wj.append({
                "date": temp[0 + 4*n],
                "m_food": temp[1 + 4*n],
                "l_food": temp[2 + 4*n],
                "d_food": temp[3 + 4*n]
            })
        n = n + 1
        if n > 6:
            break
    
        


except Exception as e:
    print(e, "Main Error")

# meal_collection_name = dbname["gongdaemeals"]
# z = meal_collection_name.delete_many({})
# print(z.deleted_count, " items deleted successfully.")
# print("Again: Data Insertion of GONGDAEMEAL board working,, done.")
# meal_collection_name.insert_many(wj, ordered=False)
#---------------------------------------------------------------------------------


browser.get('https://www.mmu.ac.kr/main/contents/todayMenu2')

n = 0

try:
    print("First done.")
    print("Second process of meal starting...")
    temp = []
    element = WebDriverWait(browser, 10).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="content"]/div[3]/div/table/tbody/tr')))
    
    elem_list= browser.find_element(
            By.CSS_SELECTOR, "div.contents812")

    items = elem_list.find_elements(By.XPATH, '//*[@id="content"]/div[3]/div/table/tbody/tr')

    for item in items:
        cols = item.find_elements(By.XPATH, "//*[name()='td']")
        
        
        
        for col in cols:
            temp.append(col.text)
            
            
        
        print("writing to file..")
        print("step", end='')
        print(n)
        write_json({
                "date": temp[0 + 4*n],
                "m_food": temp[1 + 4*n],
                "l_food": temp[2 + 4*n],
                "d_food": temp[3 + 4*n]
            }, filename='meal2.json')
        n = n + 1
        if n > 6:
            break
    
        


except Exception as e:
    print(e, "Main Error")
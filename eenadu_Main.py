from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd
import random
import os
from datetime import datetime

def TodaysNews(args):
    text4 = []
    Time = []

    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    chrome_options.add_experimental_option("prefs",prefs)
    from selenium.webdriver.support.wait import WebDriverWait
    service = Service()
    options = Options()
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.headless = True
    driver = webdriver.Chrome(service=service, options=options)

    Corresponding_names = {
        "amaravati": "amaravati",
        "anantapur": "anantapur",
        "shri sathya sai": "anantapur",
        "chittoor": "chittoor",
        "tirupati": "chittoor",
        "east godavari": "east-godavari",
        "kakinada": "east-godavari",
        "dr. br ambedkar konaseema": "east-godavari",
        "guntur": "guntur",
        "bapatla": "guntur",
        "badass": "guntur",
        "palnadu": "guntur",
        "krishna": "amaravati",
        "ntr": "amaravati",
        "kurnool": "kurnool",
        "nandyala": "kurnool",
        "brightness": "prakasam",
        "sripotti sriramulu nellore": "nellore",
        "srikakulam": "srikakulam",
        "anakapalli": "visakhapatnam",
        "visakhapatnam": "visakhapatnam",
        "alluri sitaramaraj": "alluri-sitharama-raju",
        "vizianagaram": "vizianagaram",
        "parvathipuram manyam": "parvatipuram-manyam",
        "west godavari": "west-godavari",
        "elur": "west-godavari",
        "ysr": "ysr",
        "brother": "ysr",
        "annamayya": "ysr",
}

    selected_district_lower = args.lower()

    found_match = False

    for key, value in Corresponding_names.items():
        if selected_district_lower == key or selected_district_lower == value:
            found_match = True
            district_name = value
            break
    
    if not found_match:
        print("Error: District name not found in the mapping.")
        return None




    
    url = f"https://www.eenadu.net/andhra-pradesh/districts/{district_name}"
    
    print("Selected District:", district_name)
    print("URL:", url)
    driver.implicitly_wait(15)
    driver.get(url)
    


    try:
        Content_list1 = driver.find_element('xpath','//div[@class="district-more"]')
        Next = [i for i in Content_list1.find_elements('xpath','.//div[@class="district-subdiv dst-hm-bl"]//aside[@class="thumb-content-more district-block-mm box-shadow"]//div[@class="thumb-description"]//a')]
        time.sleep(5)
        content_length = len(Next)
        print(Next)
        print(content_length)
    except Exception as e:
        print(f"An error occurred: {e}")
        time.sleep(2)
        Content_list1 = driver.find_element('xpath','//div[@class="district-more"]')
        Next = [i for i in Content_list1.find_elements('xpath','.//div[@class="district-subdiv dst-hm-bl"]//aside[@class="thumb-content-more district-block-mm box-shadow"]//div[@class="thumb-description"]//a')]
        time.sleep(5)
        content_length = len(Next)
        print(Next)
        print("Fail")

    for z in range(1,content_length,2):
        Content_list1 = driver.find_element('xpath','//div[@class="district-more"]')
        Next = [i for i in Content_list1.find_elements('xpath','.//div[@class="district-subdiv dst-hm-bl"]//aside[@class="thumb-content-more district-block-mm box-shadow"]//div[@class="thumb-description"]//a')]
        print("----", len(Next))
        try:
            Next[z].click()
        except:
            time.sleep(1)
            Next[z].click()
        time.sleep(random.uniform(3,5))
        driver.execute_script("window.stop();")

        try:
            content1 = driver.find_element('xpath', '//div[@class="eng-body grey pub-t"]//span')
            if len(content1.text) == 0:
                Time.append(None)
            else:
                Time.append(content1.text[11:])
            print("1")
        except:
            pass

        try:
            content2 = driver.find_element('xpath', '//div[@class="text-justify"]')
            if len(content2.text) == 0:
                text4.append(None)
            else:
                text4.append(content2.text) 
            print("2")
        except:
            pass
            
      
        
        try:
            driver.quit()
            service = Service()
            options = Options()
            options = webdriver.ChromeOptions()
            options.add_argument("start-maximized")
            options.headless = True
            driver = webdriver.Chrome(service=service, options=options)
            driver.implicitly_wait(15)
            driver.get(url)
            print("back")
                
        except:
            driver.quit()
            service = Service()
            options = Options()
            options = webdriver.ChromeOptions()
            options.add_argument("start-maximized")
            options.headless = True
            driver = webdriver.Chrome(service=service, options=options)
            driver.implicitly_wait(15)
            driver.get(url)

            print("back")  
    
        time.sleep(random.uniform(3, 7))
    driver.quit()
    print("DONE")

    # df = pd.DataFrame({'News': text4,'title':title,'sub':sub,'Time':Time})
    df = pd.DataFrame({'News': text4,'Time':Time})

    folder_path = fr"C:\Users\Administrator.SERVER\Downloads\Python\Data\Eenadu"
    if os.path.exists(folder_path):
        pass
    else:
        os.makedirs(folder_path)

    folder_path1 = fr"C:\Users\Administrator.SERVER\Downloads\Python\Data\Eenadu\{args}"
    if os.path.exists(folder_path1):
        pass
    else:
        os.makedirs(folder_path1)

 
    today_date = datetime.now().strftime('%Y-%m-%d')

 
    file_name = f'Eenadu{today_date}_data.csv'

    
    csv_path = os.path.join(folder_path1, file_name)
    df.to_csv(csv_path, index=False)
    

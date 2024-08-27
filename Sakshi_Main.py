from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd
import random
import os
from datetime import datetime

# selected_district='annamayya'
def TodaysNews(args):
    text4=[]
    Time=[]
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    chrome_options.add_experimental_option("prefs",prefs)
    service = Service()
    # options = Options()
    # options.headless = True    
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(service=service, options=options)
      
    Corresponding_names = {
        "amaravati": "amaravati",
        "anantapur": "ananthapur",
        "shri sathya sai": "sri-sathyasai",
        "chittoor": "chittoor",
        "tirupati": "tirupati",
        "east godavari": "eastgodavari",
        "kakinada": "kakinada",
        "dr. br ambedkar konaseema": "konaseema",
        "guntur": "guntur",
        "bapatla":"bapatla",
        "badass": "bapatla",
        "palnadu": "palnadu",
        "krishna": "krishna",
        "ntr": "ntr",
        "kurnool": "kurnool",
        "nandyala": "nandyala",
        "brightness": "prakasam",
        "sripotti sriramulu nellore": "psr-nellore",
        "srikakulam": "srikakulam",
        "anakapalli": "anakapalle",
        "visakhapatnam": "visakhapatnam",
        "alluri sitaramaraj": "alluri-sitarama-raju",
        "vizianagaram": "vizianagaram",
        "parvathipuram manyam": "parvathipuram-manyam",
        "west godavari": "westgodavari",
        "elur": "eluru",
        "ysr": "ysr",
        "brother": "annamayya",
        "annamayya":"annamayya",
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



    url = f"https://www.sakshi.com/andhra-pradesh/{district_name}"
    print("Selected District:", district_name)
    print("URL:", url)
    # url = TodaysNews(selected_district)
    driver.implicitly_wait(15)
    driver.get(url)

    try:
        Content_list1 = driver.find_element('xpath', '//div[@class="view-content"]')
        elements_in_list1 = Content_list1.find_elements('xpath', '//*[@id="block-system-main"]/div/div/div/div/div')
        Next = [element for i, element in enumerate(elements_in_list1, 1)]
        time.sleep(5)
        content_length = len(Next)
        print(Next)
        print(content_length)
    except Exception as e:
        print(f"An error occurred: {e}")
        time.sleep(2)
        Content_list1 = driver.find_element('xpath', '//div[@class="view-content"]')

        elements_in_list1 = Content_list1.find_elements('xpath', '//*[@id="block-system-main"]/div/div/div/div/div')
        Next = [element for i, element in enumerate(elements_in_list1, 1)]
        time.sleep(5)
        content_length = len(Next)
        print(Next)
        print("Fail")

    z = 0
    while z < content_length:
        try:
            Content_list1 = driver.find_element('xpath', '//div[@class="view-content"]')
            elements_in_list1 = Content_list1.find_elements('xpath', '//*[@id="block-system-main"]/div/div/div/div/div')
            Next = elements_in_list1[z].find_element('xpath', './/div[@class="views-field views-field-title"]//span[@class="field-content"]/a')
            driver.implicitly_wait(15)
            Next.click()
            print("Enter")
            time.sleep(random.uniform(1, 5))

        except:
            time.sleep(random.uniform(1, 5))
            driver.get(url)
            Content_list1 = driver.find_element('xpath', '//div[@class="view-content"]')
            elements_in_list1 = Content_list1.find_elements('xpath', '//*[@id="block-system-main"]/div/div/div/div/div')
            Next = elements_in_list1[z].find_element('xpath', './/div[@class="views-field views-field-title"]//span[@class="field-content"]/a')
            Next.click()
            print("Enter")
            time.sleep(random.uniform(1, 5))

        try:
            content = driver.find_element('xpath', '//div[@class="content"]//div[@class="node node-article clearfix"]')
            if len(content.text) == 0:
                Time.append(None)
                text4.append(None)
            else:
                Time.append(content.text[:19])
                text4.append(content.text[25:].replace('\n', ''))
            print("3")
            
            driver.quit()

            try:
                service = Service()
                # options = Options()
                options = webdriver.ChromeOptions()
                options.add_argument("start-maximized")
                # options.headless = True
                driver = webdriver.Chrome(service=service, options=options)
                driver.implicitly_wait(15)
                driver.get(url)
                print("back")
            except:
                driver.quit()
                service = Service()
                # options = Options()
                options = webdriver.ChromeOptions()
                options.add_argument("start-maximized")
                # options.headless = True
                driver = webdriver.Chrome(service=service, options=options)
                driver.implicitly_wait(15)
                driver.get(url)
                print("back")
        except:
            z=z-1
            driver.implicitly_wait(15)
            driver.get(url)
            print("AD")
        time.sleep(random.uniform(4, 7))    

        z += 1

    driver.quit()
    print("DONE")


    df = pd.DataFrame({'Time': Time, 'News': text4})


    folder_path = fr"C:\Users\Administrator.SERVER\Downloads\Python\Data\Sakshi"
    if os.path.exists(folder_path):
        pass
    else:
        os.makedirs(folder_path)

    folder_path1 = fr"C:\Users\Administrator.SERVER\Downloads\Python\Data\Sakshi\{args}"
    if os.path.exists(folder_path1):
        pass
    else:
        os.makedirs(folder_path1)

 
    today_date = datetime.now().strftime('%Y-%m-%d')

 
    file_name = f'Sakshi_{today_date}_data.csv'

    
    csv_path = os.path.join(folder_path1, file_name)
    df.to_csv(csv_path, index=False)

# TodaysNews('annamayya')
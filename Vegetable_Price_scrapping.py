from selenium import webdriver
import pandas as pd
import time
import random
from selenium.webdriver.chrome.service import Service
service = Service()
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=service, options=options)
delay = random.uniform(2, 5)

# driver = webdriver.Chrome()
driver.get("https://vegetablemarketprice.com/market/andhraPradesh/today")

from_date_link = driver.find_element('xpath', "/html/body/div[2]/div[2]/div[1]/div[2]/div[2]/div")
from_date_link.click()
time.sleep(delay)
Back = driver.find_element('xpath', "/html/body/div[4]/div[2]/div[1]/table/thead/tr[1]/th[1]")
Back.click()
time.sleep(delay)


month=driver.find_element('xpath', "/html/body/div[4]/div[2]/div[1]/table/thead/tr[1]/th[2]")
month=month.text
print(month)

calendar_table = driver.find_element('xpath', '/html/body/div[4]/div[2]/div[1]/table/tbody')


Date=[]
Vegetable = []
Wholesale_Price = []
Retail_Price = []
Shopping_Mall = []


for i in range(1,7):
    for j in range(1,8):
        time.sleep(delay)
        calendar_table = driver.find_element('xpath', '/html/body/div[4]/div[2]/div[1]/table/tbody')

        date_cell = calendar_table.find_element('xpath', f'/html/body/div[4]/div[2]/div[1]/table/tbody/tr[{i}]/td[{j}]')
        data=(date_cell.text)
        if 'weekend off ends available' not in date_cell.get_attribute('class') and 'off ends available' not in date_cell.get_attribute('class') and 'today off ends active start-date active end-date available' not in date_cell.get_attribute('class') and 'off ends off disabled' not in date_cell.get_attribute('class') and 'weekend off ends off disabled' not in date_cell.get_attribute('class') and 'today active start-date active end-date available' not in date_cell.get_attribute('class'):
            date_cell.click()
            time.sleep(delay)

            table = driver.find_element('xpath', '/html/body/div[2]/div[2]/div[1]/div[3]/table/tbody')
            print(table)
            rows = table.find_elements('xpath','//tr[@class="todayVegetableTableRows"]')
            print(len(rows))


            

            for row in rows:
                veg = row.find_element('xpath','./td[2]')
                whole = row.find_element('xpath','./td[3]')
                retail = row.find_element('xpath','./td[4]')
                mall = row.find_element('xpath','./td[5]')
                
    
                Vegetable.append(veg.text)
                Wholesale_Price.append(whole.text)
                Retail_Price.append(retail.text)
                Shopping_Mall.append(mall.text)
                Date.append(data + month)
        else:
            pass
        driver.get("https://vegetablemarketprice.com/market/andhraPradesh/today")
        time.sleep(delay)
        from_date_link = driver.find_element('xpath', "/html/body/div[2]/div[2]/div[1]/div[2]/div[2]/div")
        from_date_link.click() 
        time.sleep(delay)
        Back = driver.find_element('xpath', "/html/body/div[4]/div[2]/div[1]/table/thead/tr[1]/th[1]")
        Back.click()
        
        

    time.sleep(delay)  

df = pd.DataFrame({
    
    'Vegetable': Vegetable,
    'Wholesale_Price': Wholesale_Price,
    'Retail_Price': Retail_Price,
    'Shopping_Mall': Shopping_Mall,
    'Date':Date
})


df.to_csv(f'vegetable_data_{month}.csv', index=False)
print("Done")
driver.quit()

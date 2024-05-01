from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie_click = driver.find_element(By.ID,value="cookie")

items =driver.find_elements(By.CSS_SELECTOR,value="#store div")
item_ids = [item.get_attribute("id") for item in items]
# print(item_ids)


timeout= time.time() + 5 #timer for 5 seconds
five_min = time.time() + 60*5 #timer for 5 minutes


while True:
    cookie_click.click()
    
    #every 5 seconds
    if time.time() > timeout:
        
        #Get all upgrade <b> tags
        all_prices = driver.find_elements(By.CSS_SELECTOR,value="#store b")
        item_price = []
        # prices = [price.get_attribute("id") for price in all_prices]
        # print(prices)
        
        
        #Convert the <b> text into an integer price
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost =  int(element_text.split("-")[1].strip().replace(",",""))
                item_price.append(cost)
                
        #Create dictionary to store items and prices
        cookie_upgrades ={}
        for n in range(len(item_price)):
            cookie_upgrades[item_price[n]] = item_ids[n]
            
        #Get current cookie count
        money_element = driver.find_element(By.ID,value="money").text
        if "," in money_element:
            money_element= money_element.replace(",","")
        cookie_count = int(money_element)
        
        #find upgrades that we can currently afford
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id
                
        #purchase the most expensive affordable upgrade
        highest_price_affordable_upgrade = max(affordable_upgrades)
        print(highest_price_affordable_upgrade)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]
        
        driver.find_element(By.ID,value=to_purchase_id).click()
        
        #Add another 5second until next check
        timeout = time.time() +5
    
    #after 5mins the stop the bot and check the cookies per second count.
    if time.time() > five_min:
        cookies_per_s = driver.find_element(By.ID,value="cps").text
        print(cookies_per_s)
        break        


# driver.quit()
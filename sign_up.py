from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name= driver.find_element(By.XPATH,value='/html/body/form/input[1]')
first_name.send_keys("Nitika")

last_name = driver.find_element(By.XPATH,value='/html/body/form/input[2]')
last_name.send_keys("Dhami")

email_id = driver.find_element(By.XPATH,value='/html/body/form/input[3]')
email_id.send_keys("nitika@yahoo.com")

sign_up = driver.find_element(By.XPATH,value="/html/body/form/button")
sign_up.send_keys(Keys.ENTER)
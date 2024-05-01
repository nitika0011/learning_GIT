from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

wikipedia = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]')
#or
article_count = driver.find_element(By.CSS_SELECTOR,value="#articlecount a")
# print(wikipedia.text)
# print(article_count.text)
# article_count.click()

#Link_text= searches the element by the attribute name given in the website 
article_content = driver.find_element(By.LINK_TEXT,value="Content portals")
# article_content.click()

search_bar = driver.find_element(By.CLASS_NAME,value="cdx-text-input__input")
#sending keyboard input to Selenium
search_bar.send_keys("python",Keys.ENTER)
# search_bar.send_keys(Keys.ENTER)
# search_bar.click()
# search_button = driver.find_element(By.XPATH,value='//*[@id="searchform"]/div/button')
# search_bar.click()


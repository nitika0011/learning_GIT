from selenium import webdriver
from selenium.webdriver.common.by import By
#keep Chrome browser open after program finishes, we have to configure our webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
#---------------scrapping the amazon ---------------------------------------------------------------------------#
# driver.get("https://www.amazon.in/OnePlus-Wireless-Earbuds-Titanium-Playback/dp/B0BYJ6ZMTS/ref=asc_df_B0BYJ6ZMTS/?tag=googleshopdes-21&linkCode=df0&hvadid=649043971410&hvpos=&hvnetw=g&hvrand=197086910495237936&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9061742&hvtargid=pla-2194801394066&mcid=4174a25df3363449bb2bd09c01a155c0&th=1")
# price_dollar = driver.find_element(By.CLASS_NAME,value="a-price-whole")
# print(price_dollar.text)

#--------------------------scrapping the python org website-------------------------------------------------------#

# driver.get("https://www.python.org/")
# search_bar = driver.find_element(By.NAME,value="q")
# print(search_bar.tag_name)
# #or
# print(search_bar.get_attribute("placeholder"))

# button =driver.find_element(By.ID,value="submit")
# print(button.size)

# documentation_link =driver.find_element(By.CSS_SELECTOR, value =".documentation-widget a")
# print(documentation_link.text)

#-------------------------------Using the XPath-----------------------------------------------------------------------#

# bug_link =driver.find_element(By.XPATH,value='//*[@id="content"]/div/section/div[1]/div[3]/p[2]/a')
# print(bug_link.text)



# driver.close()
# driver.quit()
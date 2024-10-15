from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#ID selecter
from selenium.webdriver.common.by import By
import time

# driver = webdriver.Chrome()
# driver.get("http://www.python.org")
# assert "Python" in driver.title
# elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys("pycodfidfhfhn")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# time.sleep(6)


driver = webdriver.Chrome()
query='laptop'
driver.get(f"https://www.daraz.pk/catalog/?spm=a2a0e.tm80335142.search.d_go&q=laptop")
elem = driver.find_element(By.CLASS_NAME, "Bm3ON")
#print(elem.text)
print(elem.get_attribute("outerHTML"))
time.sleep(4)

driver.close()
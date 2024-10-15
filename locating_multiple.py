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
for i in range(1,10):
    driver.get(f"https://www.daraz.pk/catalog/?page={i}&q=laptop&spm=a2a0e.tm80335142.search.d_go")
    elems = driver.find_elements(By.CLASS_NAME, "Bm3ON")

    # print(elems)
    print(f"{len(elems)} items found")
    # print(elem.get_attribute("outerHTML"))
    for elem in elems:
        print(elem.text)
    time.sleep(2)

    driver.close()
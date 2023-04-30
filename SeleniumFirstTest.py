from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://google.com")
search = driver.find_element(By.NAME, "q")
search.click()
search.clear()
search.send_keys("cat")
search.send_keys(Keys.ENTER)
driver.close()

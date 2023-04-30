from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
user_name = driver.find_element(By.ID, "user-name")
user_name.click()
user_name.clear()
user_name.send_keys("standard_user")
password = driver.find_element(By.ID, "password")
password.click()
password.clear()
password.send_keys("secret_sauce")
login = driver.find_element(By.ID, "login-button")
login.click()
driver.close()

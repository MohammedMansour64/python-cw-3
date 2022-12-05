from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option("detach" , True)

PATH = "C:\Program Files (x86)\chromedriver_win32\chromedriver.exe"

driver = webdriver.Chrome()
driver = webdriver.Chrome(options=chromeOptions, executable_path="path/to/executable")
driver.get("https://lab.joincoded.com/login")


email = driver.find_element(By.NAME , "email")
password = driver.find_element(By.NAME , "password")
button = driver.find_element(By.XPATH , """//*[@id="root"]/div/div/div[2]/div/div[2]/form/div[3]/button""")

password.send_keys("xMHMDGAME32")
email.send_keys("shalia.kwt@outlook.com")
button.click()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import getpass

email=raw_input('Enter your Email/User_name==>')
password=getpass.getpass('Enter your password==> ')
print('Dont worry we dont save you password...may be we could :)')
driver = webdriver.Firefox(executable_path='./geckodriver')
driver.get("https://www.facebook.com/")
username = driver.find_element_by_id("email")
password1 = driver.find_element_by_id("pass")
username.send_keys(email)
password1.send_keys(password)
driver.find_element_by_id("loginbutton").click()

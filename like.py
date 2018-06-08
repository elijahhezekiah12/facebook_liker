from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import getpass
import time

#Taking input from user
email=raw_input('Enter your Email/User_name:   ')
password=getpass.getpass('Enter your password:    ')
print('Dont worry we dont save you password...may be we could :)')

#connecting firefox webdriver
driver = webdriver.Firefox(executable_path='./geckodriver')
driver.get("https://www.facebook.com/")

#finding email and password box
username = driver.find_element_by_id("email")
password1 = driver.find_element_by_id("pass")

#passing email and password to box
username.send_keys(email)
password1.send_keys(password)

#clicking login button
driver.find_element_by_id("loginbutton").click()

#passing esc key to remove any pop up windows
webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()

for i in range(1,1000):
    driver.execute_script("window.scrollTo(0, (document.body.scrollHeight-200));")
    try:
        driver.find_element_by_class_name("_1mto").click()
    except:
        pass

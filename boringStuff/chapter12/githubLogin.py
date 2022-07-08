from selenium import webdriver
from selenium.webdriver.common.by import By
import  pyinputplus as pyip

browser = webdriver.Firefox()
browser.get('https://github.com/login')
userElem = browser.find_element(By.ID, 'login_field')
username = input('Enter your username or email:\n')
userElem.send_keys(username)

passwordElem = browser.find_element(By.ID, 'password')
password = pyip.inputPassword('Enter your password:\n')
passwordElem.send_keys(password)
passwordElem.submit()
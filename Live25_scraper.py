from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import datetime

browser = webdriver.Chrome() #replace with .Firefox(), or with the browser of your choice
url = "https://25live.collegenet.com/uc/#space_search[1]"
browser.get(url) #navigate to the page
delay = 10

try:
    #Loading page
    myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'sentenceNav_SearchGo')))
    #Filling out Location field
    search_for_location = browser.find_element_by_id('space_search_keyword')
    search_for_location.clear()
    search_for_location.send_keys('Lindner')
    #Opening Date Search Bar
    #browser.find_element_by_link_text('Mon May 20 2019 — Sun May 26 2019').click()
    browser.find_element_by_id('daterange').click()
    #Loading the date selector
    try:
        myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.NAME, 'inputStart')))
    except:
        print('Not found after 10')
    #Entering dates
    start_date = browser.find_element_by_name('inputStart')
    start_date.send_keys(Keys.BACKSPACE*20)
    start_date.send_keys('Mon May 20 2019')
    end_date =browser.find_element_by_name('inputEnd')
    end_date.send_keys(Keys.BACKSPACE*20)
    end_date.send_keys('Mon May 20 2019')
    #clicking done button
    done = browser.find_element_by_class_name('daterangepickerFinish')
    done.click()
    submit_button = browser.find_element_by_class_name('sentenceNav_SearchGo')
    submit_button.click()
    print("Yay")
except TimeoutException:
    print ("Loading took too much time!")


print('Search Completed')
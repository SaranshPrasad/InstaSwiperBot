# import libraries 
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import pyautogui

# Input username and password manually
username = input("Enter username :- ")
password = input("Enter password :- ")

# setup driver 
driver = webdriver.Chrome()

# get instagram login url
driver.get("https://www.instagram.com/")
# Wait to load 
time.sleep(5)


# find elements and log into instagram 
driver.find_element(by=By.NAME , value='username').send_keys(username)
time.sleep(2)
driver.find_element(by=By.NAME , value='password').send_keys(password)
time.sleep(2)
driver.find_element(by=By.XPATH , value='/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button').click()
time.sleep(5)

# ignore notification 
driver.find_element(by=By.XPATH, value='/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]').click()
time.sleep(2)
# click on reels 
driver.find_element(by=By.XPATH, value='//*[@aria-label="Reels"]').click()
time.sleep(2)
# unmute reel
driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[1]/div/div/div/div/div/div/div/div/div/div/div[1]/div[1]/div').click()

# function for logout
def logout():
    driver.find_element(by=By.XPATH , value='/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[3]/span/div/a/div').click()
    driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div[1]/div/div[8]/div[1]/div/div/div[1]/div/div')

# function for swipe 
def swipe():
    #locate to center of screen
    pyautogui.moveTo(1033,515)
    time.sleep(8)
    pyautogui.scroll(-500)

# max time to use this tool
timer = 360


# loop 
while True:
    swipe()
    if timer > 0:
        swipe()
    else:
        logout()    
    timer = timer - 1 


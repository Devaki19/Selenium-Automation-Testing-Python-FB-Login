from selenium import webdriver
from _ast import arguments
import time
from selenium.webdriver.common import action_chains


class login():
    driver = webdriver.Chrome(executable_path= 'C:\\Program Files\\Selenium\\chromedriver.exe')
    driver.maximize_window()
    driver.delete_all_cookies()
    driver.get("https://www.springboards.in/")
    selectCourse = driver.find_element("xpath", "//*[@id='main-toolbar']/div/div/app-horizontal-menu/a[3]/span[3]") #clickcourse
    driver.execute_script("arguments[0].click()", selectCourse)
    print("select courses")
    
    course = driver.find_element("xpath","//*[@id='mat-menu-panel-2']/div/app-horizontal-menu/a[2]")       #select diploma
    driver.execute_script("arguments[0].click()", course) 
    print("selected diploma course")
   
    cyberSecurityCourse = driver.find_element("xpath", "//*[@id='mat-menu-panel-10']/div/app-horizontal-menu/a[1]")
    driver.execute_script("arguments[0].click()", cyberSecurityCourse)
    print("open registration form")
    

    
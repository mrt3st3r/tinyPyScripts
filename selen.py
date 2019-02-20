from selenium import webdriver
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


def elemIsPresent(elem):
    if elem is not None:
        print("We found an element >>> " + elem.text)
    else:
        print('Cannot find the element :(')


class Testing():
    def test(self):
        chromePath = '/Users/asgarh/Downloads/chromedriver'
        filepath = 'file:///Users/asgarh/Documents/page.htm'
        base_url = 'https://learn.letskodeit.com/p/practice'
        baseUrl = "https://letskodeit.teachable.com/pages/practice"

        driver = webdriver.Chrome(chromePath)
        driver.get(filepath)

        #  select bmw from radioButtons using selecty by ID
        elementById = driver.find_element(By.ID, "bmwradio")
        elementById.click()
        elemIsPresent(elementById)

        # select Benz from the dopDown list by xpath
        dropDownElementByXpath = Select(driver.find_element(By.XPATH, "//select[@id='carselect']"))
        dropDownElementByXpath.select_by_visible_text('Benz')

        # type in 'some text ' in the input filed
        elementByID2 = driver.find_element(By.ID, "displayed-text")
        elementByID2.clear()
        elementByID2.send_keys("Kian Asgarian")
        elemIsPresent(elementByID2)

        checkCheckbox = driver.find_element(By.ID, 'name')
        checkCheckbox.clear()
        checkCheckbox.send_keys('Negar Moeini')
        elemIsPresent(checkCheckbox)

        findAllElement = driver.find_elements(By.CLASS_NAME, "inputs")
        for i in findAllElement:
            print(f"elem is: {i}")
        print('size of th elements: ' + str(len((findAllElement))))

        findAllElements = driver.find_elements(By.TAG_NAME, "td")
    
        print('size of th elements: ' + str(len((findAllElements))))

        # elementByLinkText = driver.find_element(By.LINK_TEXT, "Login")
        # elemIsPresent(elementByLinkText)


cc = Testing()
cc.test()

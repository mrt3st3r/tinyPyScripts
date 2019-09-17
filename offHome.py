 
 
from selenium import webdriver
import time

myCameras = ["https://www.trafficnz.info/camera/view/80",
"https://www.trafficnz.info/camera/view/110",
"https://www.trafficnz.info/camera/view/100",
"https://www.trafficnz.info/camera/view/120",
"https://www.trafficnz.info/camera/view/121",
"https://www.trafficnz.info/camera/view/123",
"https://www.trafficnz.info/camera/view/124"]

def offHome():

    global myCameras
    driver = webdriver.Chrome()
    print("Testing Started!")
    while 1:
        try:
            for camera in myCameras:
                driver.get(camera)
                time.sleep(5)
        except KeyboardInterrupt:
            print("See you tomorrow!")
            driver.close()
            driver.quit()


def goingToWork():
    global myCameras
    myCameras.reverse()
    driver = webdriver.Chrome()
    print("Testing Started!")
    while 1:
        try:
            for camera in myCameras:
                driver.get(camera)
                time.sleep(5)
        except KeyboardInterrupt:
            print("See you tomorrow!")
            driver.close()
            driver.quit()
offHome()
# goingToWork()

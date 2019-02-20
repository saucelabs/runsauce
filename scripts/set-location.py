import unittest
import os
import time
from appium import webdriver
from appium.webdriver.extensions.location import Location
from selenium.common.exceptions import WebDriverException

caps = {}
caps['appiumVersion'] = "1.16.0"
#caps['appium_version'] = {"appium-url":"https://github.com/appium/appium-build-store/releases/download/broken/appium-patched.zip"}
caps['automationName'] = 'uiautomator2'
caps['deviceName'] = "Android GoogleAPI Emulator" # "Android Emulator"
caps['deviceOrientation'] = "portrait"
caps['app'] = "http://appium.s3.amazonaws.com/ContactManager.apk"
caps['platformVersion'] = "9.0"
caps['platformName'] = "Android"
SAUCE_USERNAME = os.environ['SAUCE_USERNAME']
SAUCE_ACCESS_KEY = os.environ['SAUCE_ACCESS_KEY']
#host = "http://admin:147a1148-a221-4e3b-a1df-987fd51c5eea@ondemand.staging.saucelabs.net/wd/hub" # Staging
#host = ("http://%s:%s@ondemand.eu-central-1.saucelabs.com/wd/hub" % (SAUCE_USERNAME, SAUCE_ACCESS_KEY)) # Frankfurt
host = ("http://%s:%s@ondemand.saucelabs.com/wd/hub" % (SAUCE_USERNAME, SAUCE_ACCESS_KEY)) # Prod
#host = "http://localhost:4723/wd/hub"
driver = webdriver.Remote(host, caps)
result = driver.set_location(49, -123, 0)
print(driver.location)

driver.quit()
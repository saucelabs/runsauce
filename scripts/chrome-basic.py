import unittest
import os
from appium import webdriver

SAUCE_USERNAME = os.environ['SAUCE_USERNAME']
SAUCE_ACCESS_KEY = os.environ['SAUCE_ACCESS_KEY']
caps = {}
caps['appiumVersion'] = "1.16.0"
caps['automationName'] = 'uiautomator2'
caps['deviceName'] = "Android GoogleAPI Emulator"
caps['deviceOrientation'] = "portrait"
caps['browserName'] = "Chrome"
caps['url'] = "chrome://version"
caps['platformVersion'] = "9.0"
caps['platformName'] = "Android"
#host = "http://admin:147a1148-a221-4e3b-a1df-987fd51c5eea@ondemand.staging.saucelabs.net/wd/hub" # Staging
#host = ("http://%s:%s@ondemand.eu-central-1.saucelabs.com/wd/hub" % (SAUCE_USERNAME, SAUCE_ACCESS_KEY)) # Frankfurt
host = ("http://%s:%s@ondemand.saucelabs.com/wd/hub" % (SAUCE_USERNAME, SAUCE_ACCESS_KEY)) # Prod
#host = 'http://admin:0e779f56-385a-41be-a562-6f6908bf5acf@localhost:4444/wd/hub'
driver = webdriver.Remote(host, caps)

driver.get('chrome://version')
result = driver.page_source
print(result)

driver.quit()
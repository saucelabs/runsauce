import unittest
import os
from appium import webdriver

SAUCE_USERNAME = os.environ['SAUCE_USERNAME']
SAUCE_ACCESS_KEY = os.environ['SAUCE_ACCESS_KEY']
caps = {}
#appium_version = {}
#appium_version['appium-url'] = 'https://www.dropbox.com/s/d94pw66c0z9tkd9/appium-vFakeVersion200.tar.bz2?dl=1'
#caps['appium_version'] = appium_version
caps['deviceName'] = "iPhone Simulator"
caps['browserName'] = "Safari"
caps['url'] = "http://www.google.com"
caps['platformVersion'] = "12.4"
caps['platformName'] = "iOS"
caps['appiumVersion'] = "1.16.0"
#host = "http://admin:147a1148-a221-4e3b-a1df-987fd51c5eea@ondemand.staging.saucelabs.net/wd/hub" # Staging
#host = ("http://%s:%s@ondemand.eu-central-1.saucelabs.com/wd/hub" % (SAUCE_USERNAME, SAUCE_ACCESS_KEY)) # Frankfurt
#host = ("http://%s:%s@ondemand.saucelabs.com/wd/hub" % (SAUCE_USERNAME, SAUCE_ACCESS_KEY)) # Prod
#host = 'http://admin:0e779f56-385a-41be-a562-6f6908bf5acf@localhost:4444/wd/hub'
#host = "http://admin:0e779f56-385a-41be-a562-6f6908bf5acf@ondemand.dpgrahamwdapreb146146.ktb.blocks.saucelabs.net/wd/hub" # Cluster
#host = "http://localhost:4723/wd/hub"
host = "http://admin:0e779f56-385a-41be-a562-6f6908bf5acf@ondemand.10.254.246.125.xip.io:4444/wd/hub"
driver = webdriver.Remote(host, caps)
print('Getting google')
driver.get('http://www.google.com')
result = driver.page_source
print(result)
print('Got it')

driver.quit()
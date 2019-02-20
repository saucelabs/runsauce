import unittest
import os
from appium import webdriver

caps = {}
#caps['appiumVersion'] = "1.15.0"
caps['automationName'] = 'uiautomator2'
caps['deviceName'] = "Android GoogleAPI Emulator" # "Android Emulator"
caps['deviceOrientation'] = "portrait"
caps['appium_version'] = {"appium-url":"https://github.com/appium/appium-build-store/releases/download/broken/appium-patched.zip"}
caps['app'] = "http://appium.s3.amazonaws.com/ContactManager.apk"
caps['platformVersion'] = "9.0"
caps['platformName'] = "Android"
SAUCE_USERNAME = os.environ['SAUCE_USERNAME']
SAUCE_ACCESS_KEY = os.environ['SAUCE_ACCESS_KEY']
#host = "http://admin:147a1148-a221-4e3b-a1df-987fd51c5eea@ondemand.staging.saucelabs.net/wd/hub" # Staging
#host = ("http://%s:%s@ondemand.eu-central-1.saucelabs.com/wd/hub" % (SAUCE_USERNAME, SAUCE_ACCESS_KEY)) # Frankfurt
host = ("http://%s:%s@ondemand.saucelabs.com/wd/hub" % (SAUCE_USERNAME, SAUCE_ACCESS_KEY)) # Prod
driver = webdriver.Remote(host, caps)

result = driver.execute_script('mobile: shell', {
    'command': 'dumpsys',
    'args': ['package', 'com.google.android.gms'],
    'includeStderr': True,
    'timeout': 5000
})
print(result)

driver.quit()
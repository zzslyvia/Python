import os
from time import sleep
import unittest

from appium import webdriver

PATH = lambda p:os.path.abspath(
    os.path.join(os.path.dirname(__file__),p)
    )

THINK_TIME = 5,

class SimpleSeleroidTests(unittest,TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVerion'] = '4.1'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['automationName'] = 'selendroid'
        desired_caps['app'] = PATH(
            '../../../sample-code/apps/ApiDemos/bin/ApiDemos-debug.apk'
            )

        self.driver = webdriver.Remote('http://localhost:4723/wb/hub',desired_caps)
    
    def tearDown(self):
        self.driver.quit()


    def test_seledroid(self):
        e1 = self.driver.find_element_by_name("Animation")
        
        self.assertEqual('Animation',e1.text)

        e1 = self.driver.find_element_by_name("App")
        e1.click()
        sleep(THINK_TIME)

        els = self.driver.find_element_by_class_name("android.widget.TextView")
        self.assertLessEqual(30,len(els))

        self.driver.find_element_by_name('Action Bar')

        self.driver.back()
        sleep(THINK_TIME)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleSeleroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

# -*- coding: utf-8 -*-

def get_test_config():
    config = {
        'platformName': 'Android',
        'platformVersion': '6.0 Marshmallow',
        'deviceName': '9999SKOFRC6TN7SO',
        'app': "G:\\packages\\app-release2.4.10_legu_signed_zipalign.apk",
        'newCommandTimeout': 30,    
        'automationName': 'Appium'
    }

    return config

def get_uri():
    return "http://localhost:4723/wd/hub"
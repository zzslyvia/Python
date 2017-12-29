# -*- coding: utf-8 -*-

from appium import webdriver
import test_config
from unittest import TestCase
from selenium.webdriver.common.by import By
import unittest
import time
import os

class MtcTest(TestCase):
    
    def setUp(self):
        config = test_config.get_test_config()
        uri = test_config.get_uri()
        self.driver = webdriver.Remote(uri, config)
        
    def test_login(self):
        # 在这里写自己的测试用例
        
        # time.sleep(2)
        # self.driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "测试")]').click()
        # time.sleep(10)
        
        self.swipe_percent(0.9, 0.5, 0.1, 0.5)
        time.sleep(1)
        self.swipe_percent(0.9, 0.5, 0.1, 0.5)
        time.sleep(1)
        
        # self.driver.find_element_by_id("com.test:id/home_start").click()
        # time.sleep(1)
        # self.driver.find_element_by_id("com.test:id/btn_login").click()
        # time.sleep(1)
        
        # self.driver.find_element_by_id("com.test:id/userName").click()
        # time.sleep(1)
        # self.enter_numbers("431381")        
        # time.sleep(1)

        # self.driver.find_element_by_id("com.test:id/password").click()
        # time.sleep(1)
        # self.enter_numbers("1234")       
        # time.sleep(1)
        
        # self.driver.find_element_by_id("com.test:id/btn_next_step").click()
        # time.sleep(5)
        # self.driver.contexts
        # self.driver.current_context
        # self.driver.switch_to.contexts('WEBVIEW')
        # self.driver.page_source
        # element.get_attribute('text')
        # element.text
        # self.driver.find_element_by_id(id)
        # self.driver.find_elements_by_id(id)
        # self.driver.find_element_by_xpath(xpath)
        # self.driver.find_element_by_class_name(class)
        # self.driver.find_elment(by,value)
        # self.driver.tap([(x,y)],time)

        # self.driver.swipe(x1,y1,x2,y2,time)
        # self.driver.flick(x1,y1,x2,y2)
        
        # self.driver.send_keys()
        # self.driver.set_text()

        # self.drvier.get_screenshot_as_file(filename)

        
        # x=self.driver.get_window_size()['width']
        # y=self.driver.get_window_size()['height']
        # self.driver.get_window_size(width,height)
        # self.driver.get_window_position()

        # self.driver.scroll(ele1,ele2)

        # self.driver.drag_and_drop(ele1,ele2)
        # # 缩小
        # self.driver.pinch(ele)
        # # 放大
        # self.driver.zoom(ele)
        # # 重启
        # self.driver.reset()

        # self.driver.hide_keyboard()

        # # 长按住键盘
        # self.driver.long_press_keycode(keycode)

        # self.push_file(path)
        # self.pull_file(path)
        # self.pull_folder(path)

        # self.driver.install_app(path)
        # self.driver.remove_app(app_id)

        # # 启动
        # self.driver.launch_app()
        # self.driver.close_app()
        # self.driver.start_activity(package,start_activity)

        # self.driver.current_activity

        # self.driver.lock(time)

        # self.driver.shake()
        # self.driver.open_notifications()

        # self.driver.network_connectinon()

# from appium.webdriver.connectiontype import ConnectionType

# self.driver.set_network_connection(ConnectionType.AIRPLANE_MODE)

# # 手机输入法

# self.driver.available_ime_engines

# self.driver.is_ime_active()

# self.driver.get_settings()
# self.driver.update_settings(settings)

# # 开关定位服务 
# self.toggle_location_services()
        
    def enter_numbers(self, number_str):
        for i in range(len(number_str)):
            self.driver.find_element_by_name(number_str[i]).click()

    def tearDown(self):
        self.driver.quit()

    def swipe_percent(self, percent_start_x, percent_start_y, percent_end_x, percent_end_y):
        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']
        self.driver.swipe(width * percent_start_x, height * percent_start_y, width * percent_end_x, height * percent_end_y)


# -*- coding: UTF-8 -*-
#-------------------------------------------------------------------------------
# Name:        模块2
# Purpose:
#
# Author:      qcshi
#
# Created:     06/08/2017
# Copyright:   (c) qcshi 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import sys
import webbrowser
import unittest, time, re
from selenium import webdriver
#from selenium.webdriver.common.action_chains import ActionChains
import unittest
from pytesser import *
from PIL import Image
import os
import pdb



##class Login(unittest.TestCase):


class LoginAndOut():
    
##   self.verificationErrors = []
##   self.accept_next_alert = True'''
    #破解登陆界面的验证码
    def imageconvert(self,driver):
        i=driver.find_element_by_id("verify")
        driver.save_screenshot('a.png')
        ##action=ActionChains(driver).move_to_element(i)
        left = int(i.location['x'])
        top = int(i.location['y'])
        right = int(i.location['x'] + i.size['width'])
        bottom =int( i.location['y'] + i.size['height'])

        im = Image.open('a.png')
        im = im.crop((left, top, right, bottom))
        im.save(r'D:\Testing datas\python\image\getImage.jpg')
        time.sleep(2)
        img=Image.open(r"D:\Testing datas\python\image\getImage.jpg")
        imgry=img.convert('L')
        threshold=140
        table=[]
        for x in range(256):
            if x<threshold:
                table.append(0)
            else:
                table.append(1)
        out=imgry.point(table,'1')
        text=image_to_string(out)
        print text
        return text
        #登陆平台
    def test_login(self,CaptchaUrl,UserName,Password):
        
        #aptchaUrl='http://test.ewaytec2001.cn/qyh/nwcmwpt/login.jsp'  ##http://test.ewaytec2001.cn/   http://www.esyun.cn/nwcmwpt/login.jsp
        driver= webdriver.Chrome()
        driver.implicitly_wait(30)
        driver.get(CaptchaUrl)
        time.sleep(3)

        while driver.current_url==CaptchaUrl:
              driver.find_element_by_id("userName").clear()
              driver.find_element_by_id("userName").send_keys(UserName)
              driver.find_element_by_id("password").clear()
              driver.find_element_by_id("password").send_keys(Password)
              text= LoginAndOut().imageconvert(driver)
              time.sleep(1)
              driver.find_element_by_id("securityCode").send_keys(text)
              time.sleep(2)
        return driver
        #退出
    def test_out(self,driver):
        driver.find_element_by_id("curUserActLink").click()
        print("hahha")
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div/div[1]/div/span/ul/li/ul/li[3]/a").click()
        driver.close()
        print ("主人,程序已经运行完毕!")



##        driver.find_element_by_id("curUserActLink").click()
##        print("hahha")
##        time.sleep(2)
##        driver.find_element_by_xpath("/html/body/div/div[1]/div/span/ul/li/ul/li[3]/a").click()
##        driver.close()
##    def tearDown(self):
##        print("one case")
##        self.driver.close()
##        self.assertEqual([], self.verificationErrors)
##    def add(self,a,b):
##        print(a+b)
##if __name__ == '__main__':
##    unittest.main()

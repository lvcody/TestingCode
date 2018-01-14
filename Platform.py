# -*- coding: UTF-8 -*-
#-------------------------------------------------------------------------------
# Name:        模块3
# Purpose:
#
# Author:      qcshi
#
# Created:     03/12/2017
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
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import random

class Platform():
    #业务域
    def test_Ywy(self,driver):
        driver.find_element_by_xpath("//*[@id='mCSB_1_container']/ul/li[1]/a").click()
        driver.switch_to_frame("frmMain")
        driver.find_element_by_xpath("//*[@id='form']/div[2]/h1/button[1]").click()
        driver.find_element_by_css_selector("#domainName").send_keys(u"业务域1")
        driver.find_element_by_id("domainDescription").send_keys(u"业务域描述")
        driver.find_element_by_css_selector("#form > div.topbar.clearfix > div > button.orange").click()
        driver.find_element_by_css_selector("body > div.l-dialog.l-dialog-win > table > tbody > tr:nth-child(2) > td.l-dialog-cc > div > div.l-dialog-buttons > div > div.l-dialog-btn > div.l-dialog-btn-inner").click()
        driver.find_element_by_id("keyword").send_keys(u"业务域1")
        driver.find_element_by_xpath("//*[@id='form']/div[2]/div/div/div/button/img").click()
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='domaingrid|2|r1001|c105']/div").click()
        driver.find_element_by_css_selector("#timeContent > div:nth-child(1) > a").click()
        driver.find_element_by_css_selector("body > div.l-dialog > table > tbody > tr:nth-child(2) > td.l-dialog-cc > div > div.l-dialog-buttons > div > div:nth-child(2) > div.l-dialog-btn-inner").click()
        s1=Select(driver.find_element_by_id("addDay"))
        s1.select_by_value("02")
        driver.find_element_by_css_selector("#addHour").clear()
        driver.find_element_by_css_selector("#addHour").send_keys(u"12")
        time.sleep(2)
        driver.find_element_by_css_selector("#addMinute").clear()
        driver.find_element_by_css_selector("#addMinute").send_keys(u"30")
        time.sleep(2)
        driver.find_element_by_css_selector("#timeDialogContent > div.block.common-form > div:nth-child(1) > button").click()
        driver.find_element_by_css_selector("#timeDialogContent > div.block.common-form > div:nth-child(4) > button:nth-child(1)").click()
        print("添加定时时间成功!")
        driver.find_element_by_css_selector("body > div.l-dialog > table > tbody > tr:nth-child(2) > td.l-dialog-cc > div > div.l-dialog-buttons > div > div.l-dialog-btn > div.l-dialog-btn-inner").click()
        # driver.find_element_by_id("keyword").clear()
        # driver.find_element_by_id("keyword").send_keys(u"业务域1")
        # driver.find_element_by_xpath("//*[@id='form']/div[2]/div/div/div/button/img").click()
        # time.sleep(2)
        # driver.find_element_by_xpath("//*[@id='domaingrid|1|r1001|c102']/div/spann").click()
        # driver.find_element_by_css_selector("#form > div.topbar.clearfix > h1 > button.red").click()
        driver.switch_to.parent_frame()
    #微信公众号
    def test_Gzhao(self,driver):
        n=0
        while n==0:
            try:
                n=1
                driver.find_element_by_css_selector("#mCSB_1_container > ul > li:nth-child(2) > a").click()
                driver.switch_to_frame("frmMain")
                time.sleep(2)
                driver.find_element_by_css_selector("button.green").click()
                driver.find_element_by_id("openId").clear()
                driver.find_element_by_id("openId").send_keys("1111")
                #driver.find_element_by_id("accountName").clear()
                driver.find_element_by_id("accountName").send_keys(u"秋秋")
                driver.find_element_by_id("appid").clear()
                driver.find_element_by_id("appid").send_keys("2222")
                driver.find_element_by_id("appSecret").clear()
                driver.find_element_by_id("appSecret").send_keys("3333")
                driver.find_element_by_id("accountDesc").clear()
                driver.find_element_by_id("accountDesc").send_keys("1111")
                time.sleep(2)
                driver.find_element_by_css_selector("#SWFUpload_0").click()
                time.sleep(2)
                os.system(r"C:\upfile.exe")
                time.sleep(5)
                driver.find_element_by_css_selector("button.orange").click()
                driver.find_element_by_xpath("/html/body/div[3]/table/tbody/tr[2]/td[2]/div/div[2]/div/div[1]/div[3]").click()
                #搜索与删除
                driver.find_element_by_id("keyword").send_keys(u"秋秋")
                driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div/div/button").click()
                time.sleep(2)
                driver.find_element_by_xpath("/html/body/div[2]/div/div[4]/div/div/div[3]/div[2]/div/table/tbody/tr/td[2]/div/span").click()
                driver.find_element_by_css_selector("#form > div.topbar.clearfix > h1 > button.red").click()
                #driver.find_element_by_xpath("/html/body/div[4]/table/tbody/tr[2]/td[2]/div/div[3]/div/div[2]/div[3]").click()
                driver.find_element_by_css_selector("body > div.l-dialog > table > tbody > tr:nth-child(2) > td.l-dialog-cc > div > div.l-dialog-buttons > div > div:nth-child(2) > div.l-dialog-btn-inner").click()
                driver.find_element_by_xpath("/html/body/div[4]/table/tbody/tr[2]/td[2]/div/div[2]/div/div[1]/div[3]").click()
                driver.switch_to.parent_frame()
            except Exception as e:
                print e
                n=0
                driver.switch_to.parent_frame()
                continue
    #应用池管理
    def test_Plugin_Pool_Manage(self,driver):
        #driver.find_element_by_css_selector("#mCSB_1_container > ul > li.Global.active > a").click()
        #driver.find_element_by_link_text(u"插件池管理").click()
        driver.find_element_by_xpath("//*[@id='mCSB_1_container']/ul/li[4]/a").click()
        driver.find_element_by_link_text(u"插件接入").click()
        driver.switch_to_frame("frmMain")
     
        #新增
        driver.find_element_by_class_name("green").click()
        driver.find_element_by_id("appCode").send_keys(u"test")
        driver.find_element_by_id("appName").send_keys(u"测试1")
        driver.find_element_by_id("chooseVisibleOrganTag").click()
        driver.find_element_by_id("visibleOrganTreeId_1_check").click()
        driver.find_element_by_css_selector("#form > div.block.common-form.fixed > table > tbody > tr:nth-child(6) > th > label").click
        driver.find_element_by_name("busBasicInfo.backManageAdd").send_keys("https://www.baidu.com/")
        driver.find_element_by_class_name("orange").click()
        time.sleep(5)
        driver.find_element_by_class_name("orange").click()
        driver.find_element_by_class_name("l-dialog-btn-inner ").click()
        #搜索与删除
        # n=0
        # while n<2:
        time.sleep(2)
        driver.find_element_by_id("keyword").clear()
        driver.find_element_by_id("keyword").send_keys(u"测试1")
        driver.find_element_by_id("keyword").send_keys(Keys.ENTER)
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='appMangerGrid|1|r1001|c102']/div/span").click()
        driver.find_element_by_class_name("red").click()
        #driver.find_element_by_class_name("l-dialog-btn-inner").click()
        driver.find_element_by_css_selector("body > div.l-dialog > table > tbody > tr:nth-child(2) > td.l-dialog-cc > div > div.l-dialog-buttons > div > div:nth-child(2) > div.l-dialog-btn-inner").click()
        time.sleep(3)
        driver.find_element_by_css_selector("body > div.l-dialog.l-dialog-win > table > tbody > tr:nth-child(2) > td.l-dialog-cc > div > div.l-dialog-buttons > div > div.l-dialog-btn > div.l-dialog-btn-inner").click()
            #n=n+1
        driver.switch_to.parent_frame()


    #员工帐号和通讯录
    def test_EmployeeManage(self,driver):
        
        #driver.find_element_by_link_text("员工账号和通讯录").click()
        driver.find_element_by_css_selector("#mCSB_1_container > ul > li:nth-child(5) > a").click()
        driver.switch_to_frame("frmMain")
        time.sleep(2)
        
        driver.find_element_by_css_selector("#form > div.topbar.clearfix > h1 > button.green.zerominw").click()
        driver.find_element_by_name("emp.empName").send_keys(u"测试用户")
        driver.find_element_by_id("emp_gender2").click()
        driver.find_element_by_id("birthday").send_keys("2018-01-01")
        s2=Select(driver.find_element_by_id("politicalStatus"))
        s2.select_by_value("99")
        s3=Select(driver.find_element_by_id("positionLevel"))
        s3.select_by_value("99")
        driver.find_element_by_name("emp.mobilePhone").send_keys("159998"+str(random.randint(10000,99999)))
        driver.find_element_by_name("emp.nickName").send_keys(u"测试用户")
        driver.find_element_by_class_name("orange").click()
        driver.find_element_by_class_name("l-dialog-btn-inner ").click()

        #搜索
        time.sleep(2)
        driver.find_element_by_id("keyword").clear()
        driver.find_element_by_id("keyword").send_keys(u"测试用户")
        driver.find_element_by_id("keyword").send_keys(Keys.ENTER)
        #锁定和解锁
        time.sleep(3)
        driver.find_element_by_class_name("l-grid-row-cell-btn-checkbox").click()
        driver.find_element_by_css_selector("#form > div.topbar.clearfix > h1 > button:nth-child(5)").click()
        driver.find_element_by_xpath("/html/body/div[8]/table/tbody/tr[2]/td[2]/div/div[2]/div/div[1]/div[3]").click()
        time.sleep(2)
        driver.find_element_by_class_name("l-grid-row-cell-btn-checkbox").click()
        driver.find_element_by_css_selector("#form > div.topbar.clearfix > h1 > button:nth-child(6)").click()
        driver.find_element_by_xpath("/html/body/div[8]/table/tbody/tr[2]/td[2]/div/div[2]/div/div[1]/div[3]").click()
        #分配部门
        time.sleep(2)
        driver.find_element_by_class_name("l-grid-row-cell-btn-checkbox").click()
        driver.find_element_by_id("updateOrganBtn").click()
        driver.find_element_by_id("updateOrganTree_5_span").click()
        driver.find_element_by_css_selector("body > div.l-dialog > table > tbody > tr:nth-child(2) > td.l-dialog-cc > div > div.l-dialog-buttons > div > div:nth-child(2) > div.l-dialog-btn-inner").click()
        driver.find_element_by_class_name("l-dialog-btn-inner ").click()

        #解除绑定
        time.sleep(2)
        driver.find_element_by_class_name("l-grid-row-cell-btn-checkbox").click()
        driver.find_element_by_id("unbindid").click()
        driver.find_element_by_css_selector("body > div.l-dialog > table > tbody > tr:nth-child(2) > td.l-dialog-cc > div > div.l-dialog-buttons > div > div:nth-child(2) > div.l-dialog-btn-inner").click()
        driver.find_element_by_class_name("l-dialog-btn-inner ").click()
        

        #管理标签

        #新增用户
        driver.find_element_by_id("manageLabelId").click()
        time.sleep(2)
        driver.find_element_by_id("addMemberClick").click()
        driver.find_element_by_id("ui-id-3").click()
        driver.find_element_by_id("pub_person_condition2").send_keys(u"测试用户")
        driver.find_element_by_id("pub_person_search").click()
        time.sleep(2)
        #driver.find_element_by_css_selector("#pub_person_grid\7c 1\7c r1001\7c c101 > div > span").click()
        driver.find_element_by_xpath("//*[@id='pub_person_grid|1|r1001|c101']/div/span").click()
        driver.find_element_by_id("pub_selected_add").click()
        #driver.find_element_by_css_selector("#jbox-state-state0 > div.jbox-button-panel > button:nth-child(2))").click()
        driver.find_element_by_xpath("//*[@id='jbox-state-state0']/div[2]/button[1]").click()
        driver.find_element_by_css_selector("#jbox-state-state0 > div.jbox-button-panel > button").click()
        #移除用户
        time.sleep(1)
        #driver.find_element_by_css_selector("#memberGrid_0\7c 1\7c r1001\7c c102 > div > span").click()
        driver.find_element_by_xpath("//*[@id='memberGrid_0|1|r1001|c102']/div/span").click()
        driver.find_element_by_id("delMemberClick").click()
        driver.find_element_by_css_selector("#jbox-state-state0 > div.jbox-button-panel > button.jbox-button.jbox-button-focus").click()
        driver.find_element_by_css_selector("#jbox-state-state0 > div.jbox-button-panel > button").click()
        time.sleep(1)
        driver.find_element_by_id("backClick").click()


        #删除用户
        time.sleep(2)
        driver.find_element_by_id("keyword").clear()
        driver.find_element_by_id("keyword").send_keys(u"测试用户")
        driver.find_element_by_id("keyword").send_keys(Keys.ENTER)
        time.sleep(2)
        driver.find_element_by_class_name("l-grid-row-cell-btn-checkbox").click()
        driver.find_element_by_css_selector("#form > div.topbar.clearfix > h1 > button.red.zerominw").click()
        driver.find_element_by_css_selector("body > div.l-dialog > table > tbody > tr:nth-child(2) > td.l-dialog-cc > div > div.l-dialog-buttons > div > div:nth-child(2) > div.l-dialog-btn-inner").click()
        driver.find_element_by_class_name("l-dialog-btn-inner ").click()

        
        driver.switch_to.parent_frame()
        


    #企业号平台的应用管理    
    def test_Yygl(self,driver):
        i=0
        while i<=2:
            try:
                driver.find_element_by_xpath("//*[@id='mCSB_1_container']/ul/li[2]/a").click()
                driver.find_element_by_css_selector("#mCSB_1_container > ul > li.Global.active > ul > li:nth-child(2) > a").click()
                driver.switch_to_frame("frmMain")
                time.sleep(2)
                driver.find_element_by_id("keyword").send_keys(u"应用矩阵")
                driver.find_element_by_css_selector("#form > div.topbar.clearfix > div > div > div > button").click()
                time.sleep(2)
                #driver.find_element_by_xpath("//*[@id='maingrid|2|r1001|c10']/div/a[2]").click()
                driver.find_element_by_link_text(u"主页配置").click()
                time.sleep(2)
                driver.find_element_by_link_text(u"应用配置").click()
                #driver.find_element_by_css_selector("#tabs > li.active > a").click()
                time.sleep(3)
                driver.find_element_by_css_selector("#homeAgentAddBtn > button").click()
                driver.find_element_by_css_selector("#name").send_keys(u"子平台"+str(i))
                driver.find_element_by_css_selector("#SWFUpload_0").click()
                time.sleep(2)
                os.system(r"C:\upfile.exe")
                time.sleep(5)
                driver.find_element_by_id("organName").click()
                driver.find_element_by_css_selector("#treeDemo_1_span").click()
                driver.find_element_by_css_selector("#url").send_keys("https://www.baidu.com/")
                driver.find_element_by_css_selector("#news_count").clear()
                driver.find_element_by_css_selector("#news_count").send_keys(u"30")
                driver.find_element_by_css_selector("#act_count").clear()
                driver.find_element_by_css_selector("#act_count").send_keys(u"50")
                driver.find_element_by_id("description").send_keys(u"哈哈哈")
                driver.find_element_by_xpath("//*[@id='form']/div[3]/table/tbody/tr[9]/td/div/button[1]").click()
                #river.find_element_by_css_selector("#form > div.block.common-form.fixed > table > tbody > tr:nth-child(9) > td > div > button.orange").click()
                driver.find_element_by_css_selector("body > div.l-dialog.l-dialog-win > table > tbody > tr:nth-child(2) > td.l-dialog-cc > div > div.l-dialog-buttons > div > div.l-dialog-btn > div.l-dialog-btn-inner").click()
                i=i+1
                driver.refresh()
            except Exception as e:
                 print i
                 print e
                 driver.switch_to.parent_frame()
                 continue
        print("循环执行完毕")

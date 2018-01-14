# -*- coding: UTF-8 -*-
#-------------------------------------------------------------------------------
# Name:        模块1
# Purpose:
#
# Author:      szh
#
# Created:     06/08/2017
# Copyright:   (c) qcshi 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#coding:utf-8
import sys
import webbrowser
import unittest, time, re
from selenium import webdriver
#from selenium.webdriver.common.action_chains import ActionChains
import unittest
import os

class Plugin_Nw():
    #进入插件
    def FindPlugin(self,driver,PluginName):
        driver.find_element_by_xpath("//*[@id='mCSB_1_container']/ul/li[3]/a").click()
        driver.switch_to_frame("frmMain")
        time.sleep(5)
        driver.find_element_by_id("keyword").send_keys(PluginName)
        driver.find_element_by_xpath("//*[@id='form']/div[2]/div/div/div/button").click()
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='appMangerGrid|2|r1001|c105']/div/a").click()
        time.sleep(2)
        #服务号
    def Meeting(self,driver):
        Plugin_Nw().FindPlugin(driver,u"会议签到")
        driver.find_element_by_xpath("//*[@id='title_m']/span/a").click()
        driver.find_element_by_id("txtTitle").send_keys(u"会议活动1")
        driver.find_element_by_id("txtPublish").send_keys(u"秋秋")
        ##driver.find_element_by_id("txtBeginTime").click()
        time.sleep(1)
        ##driver.find_element_by_id("dpTodayInput").click()
        driver.find_element_by_id("txtBeginTime").send_keys("2017-12-21 17:26")
        time.sleep(1)
        ##driver.find_element_by_id("txtEndTime").click()
        driver.find_element_by_id("txtEndTime").send_keys("2017-12-22 17:26")
        time.sleep(1)
        ##driver.find_element_by_id("dpTodayInput").click()
        driver.find_element_by_id("txtAddress").send_keys(u"会议室1")
        driver.find_element_by_id("ChooseStaff_txtAttendUser").click()
        driver.find_element_by_id("ChooseStaff_rdSelftOrgan").click()
        driver.find_element_by_id("ChooseStaff_treeEnterprise_1_check").click()
        driver.find_element_by_id("ChooseStaff_btnToRight").click()
        driver.find_element_by_id("ChooseStaff_btnSave").click()
        driver.switch_to_frame("xhe0_iframe")
        #driver.find_element_by_xpath("/html/body").send_keys(u"简介内容")
        driver.find_element_by_css_selector("html body.editMode").click()
        time.sleep(2)
        driver.find_element_by_css_selector("html body.editMode").send_keys(u"简介内容")
        driver.switch_to.parent_frame()
        driver.find_element_by_id("btnSave2").click()
        driver.find_element_by_xpath("/html/body/div[7]/div[3]/div/button").click()
        driver.switch_to.parent_frame()
        time.sleep(5)

    def GameAct(self,driver):
        Plugin_Nw().FindPlugin(driver,u"润游戏+")
        i=18
        while i<20:
            try:
                driver.find_element_by_id("add").click()
                driver.find_element_by_id("name").send_keys(u"游戏"+str(i))
                driver.find_element_by_id("SWFUpload_0").click()
                os.system(r"C:\upfile.exe")
                time.sleep(1)
                driver.find_element_by_id("SWFUpload_1").click()
                os.system(r"C:\upfile.exe")
                driver.switch_to_frame("ueditor_0")
                driver.find_element_by_css_selector("body").send_keys(u"哈哈hahhahaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaahhahhah哈哈哈哈哈啊哈哈哈啊哈哈哈哈哈啊哈哈哈")
                driver.switch_to.parent_frame()
                driver.find_element_by_id("url").send_keys(u"http://test.ewaytec2001.cn/login/mainAction.shtml")
                time.sleep(1)
                driver.find_element_by_css_selector("#gameActContent > div.but-box > a:nth-child(1)").click()
                driver.find_element_by_css_selector("#jbox-state-state0 > div.jbox-button-panel > button").click()
                i=i+1
               
            except Exception as e:
                print e
                driver.find_element_by_css_selector("#title_m > a").click()
                continue

        driver.switch_to.parent_frame()


    def VoteType(self,driver):
        Plugin_Nw().FindPlugin(driver,u"会议签到java") 



        
        


#encoding=utf-8
#-------------------------------------------------------------------------------
# Name:        模块1
# Purpose:
#
# Author:      szh
#
# Created:     16/09/2017
# Copyright:   (c) qcshi 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys
import webbrowser
import unittest, time, re
from selenium import webdriver
#from selenium.webdriver.common.action_chains import ActionChains
import unittest
from LoginAndOut import LoginAndOut
from Plugin_Nw import Plugin_Nw
from  Platform import *
#from Platform import Platform
import os
import urllib2
import urllib
import cookielib
from pytesser import *
from PIL import Image
import pdb
--哈哈

L=LoginAndOut()
P=Platform()
W=Plugin_Nw()
#try:
driver=L.test_login('http://test.ewaytec2001.cn/nwcmwpt/login.jsp','qc','1qaz@WSX')
	#P.test_Ywy(driver)
	#P.test_Yygl(driver)
	#P.test_Gzhao(driver)
	#W.Meeting(driver)
	#W.GameAct(driver)
	#W.VoteType(driver)
	#L.test_out(driver)
	#P.test_Plugin_Pool_Manage(driver)

P.test_EmployeeManage(driver)
#except Exception as e:
                #print e
                #L.test_out(driver)
L.test_out(driver)
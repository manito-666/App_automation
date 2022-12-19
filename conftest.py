import os
import pytest
import time
from appium import webdriver
from common.mylog import log
from common.operate import Operates
@pytest.fixture()
def start(android_setting):
    #登录前置操作
    global driver
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',android_setting)

    d=os.popen("adb devices")
    f=d.read()
    if "devices" in str(f):
        log.info("当前运行的操作系统为Android")
        log.info("========测试开始========")
    elif f==None:
        log.info("设备异常或无设备连接")

    else:
        log.info('当前运行的操作系统为IOS')
    return Operates(driver)

@pytest.fixture()
def close():
    yield driver
    time.sleep(2)
    driver.quit()
    log.info("========测试结束========")



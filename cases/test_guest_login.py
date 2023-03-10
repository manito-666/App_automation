#coding=utf-8
import os,sys
import allure
import pytest
Path = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(Path)[0]
sys.path.append(rootPath)
from common.mylog import log
from time import sleep
from common.read_data import ReadFileData
#demo登录
testelement =ReadFileData('login.yaml').get_yaml_data()
class Test_Vlogin():
    @allure.epic("IH项目使用")
    @allure.feature("功能点：guest登录")
    @allure.story("guest登录成功后退出")
    @allure.title("guest登录")
    @allure.description("测试一下游客登录是否正常")
    def test_guest_login(self,start,close):
        self.d=start
        loc = testelement["login_element"]
        loc1 = tuple(loc[0])
        self.d.click(loc1)
        sleep(2)
        log.info("选择项目")
        loc2= tuple(loc[1])
        self.d.click(loc2)
        sleep(1)
        log.info("点击项目")
        sleep(2)
        loc3 = tuple(loc[2])
        self.d.click(loc3)
        log.info("点击初始化")
        sleep(3)
        loc4 = tuple(loc[3])
        self.d.click(loc4)
        sleep(2)
        log.info("点击登录")
        loc5 = tuple(loc[4])
        self.d.click(loc5)
        sleep(2)
        log.info("点击游客登录")
        loc6 = tuple(loc[5])
        self.d.click(loc6)
        sleep(3)
        log.info("点击进入游戏")
        try:
            loc7= tuple(loc[6])
            m=str(self.d.get_text(loc7))
            sleep(3)
            assert "退出" in m
            log.info("测试登录成功，文本为：{}".format(m))
        except Exception as e:
            log.error("测试失败: " + format(e))
            self.d.get_windows_img()
        loc8 = tuple(loc[7])
        self.d.click(loc8)
        log.info("点击退出登录")



if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_guest_login"])


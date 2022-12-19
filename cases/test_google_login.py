#coding=utf-8
from common.mylog import log
from time import sleep
from common.read_data import ReadFileData
import allure
import pytest
testelement =ReadFileData('login.yaml').get_yaml_data()

class Test_Glogin():
    @allure.epic("IH项目使用")
    @allure.feature("功能点：google账号登录")
    @allure.story("google登录成功后退出")
    @allure.title("google登录")
    @allure.description("测试一下google登录是否正常")
    def test_google_login(self,start,close):
        self.d=start
        loc=testelement["google_login"]
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
        log.info("点击google登录")

        loc6=tuple(loc[5])
        self.d.click(loc6)
        sleep(2)
        log.info("选择账号")
        try:
            loc7 = tuple(loc[6])
            self.d.click(loc7)
            sleep(3)
            log.info("点击进入游戏")
            loc8= tuple(loc[7])
            result=self.d.get_text(loc8)
            sleep(3)
            assert "退出游戏" in result
            log.info("测试google登录成功，文本为：{}".format(result))
        except Exception as e:
            log.error("测试失败: " + format(e))
            self.d.get_windows_img()
        loc9 = tuple(loc[8])
        self.d.click(loc9)
        log.info("点击退出登录")



if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_google_login"])


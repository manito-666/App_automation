#coding=utf-8
from common.mylog import log
from time import sleep
from common.read_data import ReadFileData
import allure
import pytest
#demo登录
testelement =ReadFileData('login.yaml').get_yaml_data()
class Test_Mlogin():
    @allure.epic("IH项目使用")
    @allure.feature("功能点：mail登录")
    @allure.story("mail登录成功后退出")
    @allure.title("mail登录")
    @allure.description("测试一下mail登录是否正常")
    def test_guest_login(self,start,close):
        self.d=start
        loc=testelement["mail_login"]
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
        log.info("点击邮箱登录")
        m=tuple(testelement['account'][0])
        loc6 = tuple(loc[5])
        self.d.click(loc6)
        sleep(2)
        loc7=tuple(loc[6])
        sleep(3)
        self.d.input(loc7,text=m[0])
        log.info("输入邮箱")
        sleep(2)
        loc8 = tuple(loc[7])
        self.d.click(loc8)
        sleep(3)
        self.d.input(loc8, text=m[1])
        log.info("输入密码")
        loc9 = tuple(loc[8])
        self.d.click(loc9)
        sleep(3)
        log.info("点击登录")
        loc10 = tuple(loc[9])
        self.d.click(loc10)
        sleep(3)
        log.info("点击进入游戏")
        try:
            loc11= tuple(loc[10])
            m=str(self.d.get_text(loc11))
            sleep(3)
            if m in "退出":
                log.info("测试登录成功，文本为：{}".format(m))
        except Exception as e:
            log.error("测试失败: " + format(e))
            self.d.get_windows_img()
        loc12 = tuple(loc[11])
        self.d.click(loc12)
        log.info("点击退出登录")



if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_guest_login"])


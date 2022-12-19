#coding=utf-8
import allure
import time,os,sys
Path = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(Path)[0]
sys.path.append(rootPath)
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from common.mylog import log
from conf.config import ImagePath
from selenium.common.exceptions import ElementNotVisibleException
from appium.webdriver.common.touch_action import TouchAction
class LocatorTypeError(Exception):
    pass
class ElementNotFound(Exception):
    pass

class Operates():
    # 初始化页面的操作
    def __init__(self,driver):
        """
        构造函数，创建必要的实例变量
        """
        self.driver = driver
        self.log = log # 初始化一个log对象

    def click(self, locator):
        if not isinstance(locator, tuple):
            raise LocatorTypeError("参数类型错误，locator必须是turper类型：loc = ('id','value1')")
        else:
            self.log.info("正在定位元素信息：定位方式->%s,value值->%s" % (locator[0], locator[1]))
        try:
            self.driver.find_element(*locator).click()
        except Exception:
            self.log.error("定位点击元素失败！")

    def click_ele_exist(self, locator):
        try:
            self.driver.find_element(locator)
            btns = self.driver.find_elements(locator)
            # 如果出现用户协议弹出按钮
            if btns:
                btns[0].click()
        except Exception:
            self.log.error("定位有时出现的点击元素失败！")


    def find(self, locator):
        if not isinstance(locator, tuple):
            raise LocatorTypeError("参数类型错误，locator必须是turper类型：loc = ('id','value1')")
        else:
            self.log.info("正在定位元素信息：定位方式->%s,value值->%s" % (locator[0], locator[1]))
        """定位到元素，返回元素对象，没定位到，Timeout异常"""
        try:
            ele = WebDriverWait(self.driver, 30,0.5).until(EC.presence_of_element_located(*locator))
        except TimeoutException as msg:
            raise ElementNotFound("定位元素出现超时！")
        return ele

    def input(self,locator,text = ""):
        '''输入文本'''
        ele = self.find(locator)
        if ele.is_displayed():
            ele.send_keys(text)
        else:
            self.get_windows_img()
            raise ElementNotVisibleException("元素不可见或者不唯一无法输入")


    def get_text(self, locator):
        """
        获取文本元素
        :param locator:
        :return:
        """
        if not isinstance(locator, tuple):
            raise LocatorTypeError("参数类型错误，locator必须是turper类型：loc = ('id','value1')")
        else:
            self.log.info("正在定位元素信息：定位方式->%s,value值->%s" % (locator[0], locator[1]))
        try:
            t = self.find(*locator).text
            return t
        except:
            self.log.info("获取文本元素失败，返回''")


    def getElements(self, *locator):
        """
        根据某种方式定位到多个元素
        :return:
        """
        try:
            eles = self.driver.find_elements(*locator)
        except Exception:
            self.log.error("定位多个元素失败！")
        else:
            return eles

    def new_swap(self, start_x, start_y, end_x, end_y):
        """
        重新疯转swap()函数
        滑动页面
        :param start_x: 当前位置的横坐标
        :param start_y: 当前位置的竖坐标
        :param end_x: 滑动后位置的横坐标
        :param end_y: 滑动后位置的竖坐标
        :return:
        """
        try:
            self.driver.swap(start_x, start_y, end_x, end_y)
        except Exception:
            self.log.error("滑动页面失败！")

    def new_keyEvent(self, key):
        """
        重新封装keyEvent()函数
        根据不同的键值，来确定系统的操作
        :param key:
        :return:
        """
        try:
            self.driver.keyevent(key)
        except Exception:
            self.log.error("系统键操作失败！")


    def get_windows_img(self):
        """截图操作"""

        file_path=ImagePath
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            log.error("截图已保存在：" + file_path)
        except NameError as e:
            self.get_windows_img()

    # def key_input(self,nuber):
    #     keycode = {}
    #     keycode['0'] = '7'
    #     keycode['1'] = '8'
    #     keycode['2'] = '9'
    #     keycode['3'] = '10'
    #     keycode['4'] = '11'
    #     keycode['5'] = '12'
    #     keycode['6'] = '13'
    #     keycode['7'] = '14'
    #     keycode['8'] = '15'
    #     keycode['9'] = '16'
    #     keycode['a'] = '29'
    #     keycode['b'] = '30'
    #     keycode['c'] = '31'
    #     keycode['d'] = '32'
    #     keycode['e'] = '33'
    #     keycode['f'] = '34'
    #     keycode['g'] = '35'
    #     keycode['h'] = '36'
    #     keycode['i'] = '37'
    #     keycode['j'] = '38'
    #     keycode['k'] = '39'
    #     keycode['l'] = '40'
    #     keycode['m'] = '41'
    #     keycode['n'] = '42'
    #     keycode['o'] = '43'
    #     keycode['p'] = '44'
    #     keycode['q'] = '45'
    #     keycode['r'] = '46'
    #     keycode['s'] = '47'
    #     keycode['t'] = '48'
    #     keycode['u'] = '49'
    #     keycode['v'] = '50'
    #     keycode['w'] = '51'
    #     keycode['x'] = '52'
    #     keycode['y'] = '53'
    #     keycode['z'] = '54'
    #     keycode['@'] = '77'
    #     keycode['#'] = '18'
    #     keycode['+'] = '81'
    #     keycode['-'] = '69'
    #     keycode['*'] = '17'
    #     keycode['/'] = '76'
    #     keycode['='] = '70'
    #     print(self.driver.available_ime_engines)
    #     m = nuber
    #     self.driver.activate_ime_engine('com.netease.nemu_vinput.nemu/com.android.inputmethodcommon.SoftKeyboard')  # 激活键盘
    #     for i in m:
    #         self.driver.press_keycode(keycode[i])

    def quit(self):
        """
        退出浏览器
        :return:
        """
        try:
            self.driver.quit()
            self.log.info("退出成功！")
        except Exception:
            self.log.error("退出失败！")

# 向上滑动屏幕
def swipe_to_up(self):
    window_size = self.driver.get_window_size()
    width = window_size.get("width")
    height = window_size.get("height")
    self.driver.swipe(width / 2, height * 3 / 4, width / 2, height / 4, 500)

# 向下滑动屏幕
def swipe_to_down(self):
    window_size = self.driver.get_window_size()
    width = window_size.get("width")
    height = window_size.get("height")
    self.driver.swipe(width / 2, height / 4, width / 2, height * 3 / 4, 500)

# 向左滑动屏幕
def swipe_to_left(self):
    window_size = self.driver.get_window_size()
    width = window_size.get("width")
    height = window_size.get("height")
    self.driver.swipe(width / 4, height / 2, width * 3 / 4, height / 2, 500)

# 向右滑动屏幕
def swipe_to_right(self):
    window_size = self.driver.get_window_size()
    width = window_size.get("width")
    height = window_size.get("height")
    self.driver.swipe(width * 4 / 5, height / 2, width / 5, height / 2, 500)

# 长按元素
def long_press(self, type, loc):
    if type == 'id':
        element = self.driver.find_element_by_id(loc)
        TouchAction(self.driver).long_press(element).perform()
    elif type == 'xpath':
        element = self.driver.find_element_by_xpath(loc)
        TouchAction(self.driver).long_press(element).perform()
    elif type == 'class_name':
        element = self.driver.find_element_by_class_name(loc)
        TouchAction(self.driver).long_press(element).perform()
    elif type == 'text':
        element = self.driver.file_detector_context(loc)
        TouchAction(self.driver).long_press(element).perform()


# 点击坐标
def touch_tap(self, x, y, duration=50):
    width = self.driver.get_window_size()['width']
    height = self.driver.get_window_size()['height']
    a = (float(x) / width) * width
    x1 = int(a)
    b = (float(y) / height) * height
    y1 = int(b)
    self.driver.tap([(x1, y1), (x1, y1)], duration)


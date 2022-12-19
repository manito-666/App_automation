import os

proDir = os.path.split(os.path.realpath(__file__))[0]
prj=os.path.abspath(os.path.join(os.path.dirname("__file__"),os.path.pardir))


DataPath = os.path.join(prj,'datas','desired_caps.yaml')  # yaml个数的测试数据的存放路径

LogPath = os.path.join(prj,'datas','log/')     # 日志文件存放路径

ImagePath = os.path.join(prj,'datas','picture/')    # 截图存放路径

appium_log=os.path.join(prj,'datas','appium_log/')

cases_path=os.path.join(prj,'cases')

report_path=os.path.join(prj,'datas','report/')
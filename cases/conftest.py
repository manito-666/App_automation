import pytest
from common.read_data import ReadFileData

# 配置app的各种连接信息
@pytest.fixture(scope='session')
def android_setting():
    data = ReadFileData('desired_caps.yaml').get_yaml_data()
    desired_caps = {}
    desired_caps['platformName'] = data['platformName']
    desired_caps['platformVersion'] = data['platformVersion']
    desired_caps['deviceName'] = data['deviceName']
    desired_caps['appPackage'] = data['appPackage']
    desired_caps['appActivity'] = data['appActivity']
    desired_caps['automationName'] = data['automationName']
    desired_caps['focusable'] = data['focusable']
    return desired_caps


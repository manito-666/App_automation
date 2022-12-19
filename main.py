import pytest
from common.mylog import log
from conf.config import *
from common.check_port import check_port
import glob


if __name__ == '__main__':

    log.info("%s  --alluredir=./datas/report" % cases_path)
    # number = glob.glob(pathname='cases/test_*.py')
    pytest.main(["-qs","./cases/", "--alluredir", "./datas/report/allure-results"])
    os.popen("allure generate ./datas/report/allure-results/ -o ./datas/report/allure-report/ --clean")
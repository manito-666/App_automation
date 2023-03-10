import subprocess,os,sys
from time import ctime
import multiprocessing
Path = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(Path)[0]
sys.path.append(rootPath)
from conf.config import appium_log

def appium_start(host,port):
    bootstrap_port=str(port+1)
    cmd='appium -a '+ host +' -p '+ str(port) +' -bp '+ str(bootstrap_port)

    print('%s at %s'%(cmd,ctime()))
    subprocess.Popen(cmd,shell=True,stdout=open(appium_log+str(port)+'.log','a'),stderr=subprocess.STDOUT)
appium_process=[]
for i in range(2):
    host = '127.0.0.1'
    port=4723+2*i
    appium=multiprocessing.Process(target=appium_start,args=(host,port))
    appium_process.append(appium)

if __name__ == '__main__':
    for appium in appium_process:
        appium.start()

    for appium in appium_process:
        appium.join()
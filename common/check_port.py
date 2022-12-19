# -*- coding:utf-8 -*-
import socket
import os,sys
Path = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(Path)[0]
sys.path.append(rootPath)
from common.mylog import log
from common.Appium_start import appium_start

def check_port(host,port):
# 检查端口是否被占用

    #创建socket对象
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        s.connect((host,port))
        s.shutdown(2) #表示将来禁止读和写
    except OSError as msg:
        print("port %s is available !" % port)
        return True
    else:
        print("port %s already in use! " %port)
        realease_macport(port)
        return False




def realease_macport(port):
    cmd1='lsof -i tcp:{}'.format(port)
    result=os.popen(cmd1).read()
    if str(port) and 'LISTEN' in result:
        i=result.find('PID')-1
        start = i +result.index('\n')
        end = result.index('\n')+14
        pid = result[start:end]
        cmd_kill = 'sudo kill -9 -pid %s' % pid
        os.popen(cmd_kill)
        print("已解除PID:{}端口使用".format(pid))

    else:
        print('port %s is available !' % port)



def release_windport(port):
    """释放指定的端口"""
    cmd_find = 'netstat -aon | findstr {}'.format(port)  # 查找对应端口的pid
    print(cmd_find)

    # 返回命令执行后的结果
    result = os.popen(cmd_find).read()
    print(result)

    if str(port) and 'LISTENING' in result:
        # 获取端口对应的pid进程
        i = result.index('LISTENING')
        start = i + len('LISTENING') + 7
        end = result.index('\n')
        pid = result[start:end]
        cmd_kill = 'taskkill -f -pid %s' % pid  # 关闭被占用端口的pid
        print(cmd_kill)
        os.popen(cmd_kill)
    else:
        print('port %s is available !' % port)

if __name__ == '__main__':
    host = '127.0.0.1'
    port = 4723
    check_port(host,port)

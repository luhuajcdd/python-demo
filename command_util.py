# -*- coding:utf-8  -*-
import os
import subprocess


def cd_pwd(dir):
    """
    if dir.find('/') == 0:
        dir = dir[1:len(dir)]
        print(dir)
        """
    # 进入打包目录
    print(os.system('pwd'))
    os.chdir(dir)
    print(os.system('pwd'))


def command_finish(subproc, desc):
    while True:
        res = subproc.poll()
        if res == 0 or res == -9:
            print("%s end " % desc)
            break
        elif res is not None:
            raise Exception("error: res = %s" % res)


def command_execute(command, desc):
    p = subprocess.Popen(command,
                         0,
                         shell=True,
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    command_finish(p, desc)

# -*- coding:utf-8  -*-

import os            #导入os方法
import subprocess
print('test')
os.chdir('../android/Branches/release/5.0.0/Android4.3.0-20180509')
print(os.system('pwd'))
cmd='./pack2.sh  /Users/sangfor/Documents/138pack/android-4.3 pocket-release-5.0.0-105527.apk release 5.0.0 64 YES NONE'
#cmd='./test_shell.sh'
n=os.system(cmd) #调用shell脚本

print(n)
print('执行完毕')

print('subprocess')
p = subprocess.Popen(cmd, shell=True, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
curline = p.stdout.readline()


while(curline != ""):
	print (curline)
	curline = p.stdout.readline()
p.wait()
print (p.returncode)
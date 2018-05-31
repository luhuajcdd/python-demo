# -*- coding:utf-8  -*-
import os
import subprocess
import c_p

#result=os.popen('cd ./cmddir')

#print(result.read())

os.chdir('E:/Documents/autopack/Branches/release/5.0.0/Android4.3.0-20180509')
print('get svn version')
print(os.system("svnversion -c "))
print(os.system("svnversion -c |sed 's/^.*://' |sed 's/[A-Z]*$//'"))
code_version=os.popen("svnversion -c |sed 's/^.*://' |sed 's/[A-Z]*$//'",'r',-1)
print(code_version.read())

print()

c = c_p.consumer()
c_p.produce(c)


def printPwd():
    print(os.system('pwd'))

def printLs():
    print(os.system('ls'))

printPwd()

ret = os.chdir('cmddir')
print(ret)
p=subprocess.Popen("ls -l", shell=True,stdin=subprocess.PIPE, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
(stdout,errout) = p.communicate()
print(stdout)
print(errout)
print()

p=subprocess.Popen("rm -rf *", shell=True,stdin=subprocess.PIPE, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
(stdout,errout) = p.communicate()
print(stdout)
print(errout + '\r')

subprocess.Popen("mkdir "+ "a/b".replace("/","\\"),shell=True,
                             stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)

printPwd()

printLs()

print(os.chdir('..'))

printLs()


print('\n subprocess  start ')
cd = subprocess.call(['cd','cmddir'],shell=False)
printPwd()
printLs()




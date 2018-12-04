# -*- coding:utf-8  -*-
import os
import platform
import subprocess

import command_util


def isWindows():
    sysstr = platform.system()
    return sysstr == "Windows"

def isLinuxOrMac():
    sysstr = platform.system()
    return sysstr == "Linux" or sysstr == "Darwin"

'''
    清空打包目录
'''
def clear_pack_and_create_new_dir(full_build_type):
    print("clear_pack_and_create_new_dir  dirs %s" % full_build_type)
    if os.path.exists(full_build_type):
        # 目录存在 删除
        print("delete path : " + full_build_type)
        p = subprocess.Popen("rm -rf " + full_build_type, shell=True,
                             stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
        command_util.command_finish(p,"delete path " + full_build_type)
    #创建新的目录

    create_dirs(full_build_type)


def create_dirs(full_build_type):
    create_dir = None
    if isWindows():
        create_dir = subprocess.Popen("mkdir " + full_build_type.replace("/", "\\"), shell=True,
                                      stdin=subprocess.PIPE,
                                      stdout=subprocess.PIPE,
                                      stderr=subprocess.PIPE)
    elif isLinuxOrMac():
        create_dir = subprocess.Popen("mkdir -p " + full_build_type, shell=True,
                                      stdin=subprocess.PIPE,
                                      stdout=subprocess.PIPE,
                                      stderr=subprocess.PIPE)
    else:
        print("没有处理逻辑：")
    if create_dir:
        command_util.command_finish(create_dir, "create dir " + full_build_type)


def checkout_and_get_code_version(svn_path):
    p = subprocess.Popen("svn checkout " + svn_path, shell=True)
    command_util.command_finish(p, "checkout %s finished! " % svn_path)

    command_util.cd_pwd(svn_path[svn_path.rindex('/') + 1:len(svn_path)])
    version = get_svn_version(svn_path)
    print('code version = %s ' % version)
    return version


def get_svn_version(svn_path):
    code_version = os.popen("svnversion -c |sed 's/^.*://' |sed 's/[A-Z]*$//'", 'r', -1)
    version = code_version.read().strip()
    return version


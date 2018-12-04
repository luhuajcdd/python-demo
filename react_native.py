# -*- coding:utf-8  -*-

'''
   处理react-native代码
'''
import command_util
import subprocess
import os

import file_util


# react_native_code_path = '/Users/sangfor/Documents/autopack/android-ios-common-code/'
# rn_project_name = 'sms_v2'
import svn


def checkout_code(svn_path):
    checkout_command = 'svn checkout ' + svn_path
    os.system(checkout_command)
    print('chechout %s success' % svn_path)

    command_util.cd_pwd(svn_path[svn_path.rindex('/') + 1:len(svn_path)])
    version = svn.get_svn_version(svn_path)
    print('rn: code version = %s ' % version)


def rn_build():
    npm_install = 'npm install'
    os.system(npm_install)
    print('npm install end')

def get_bundle_file(svn_path, rn_code_path, pack_dir, project_name):
    project_full_dir = chechout_or_update_and_install(svn_path, rn_code_path)

    file_util.mkdir('./output/bundle/')
    file_util.mkdir('./output/res/')
    os.system("rm -rf ./output/bundle/*")

    # 生成bundle文件
    command_create_android_bundle = 'react-native bundle --entry-file index.android.js --platform android --dev false --bundle-output ./output/bundle/moa.bundle --assets-dest ./output/res/'
    os.system(command_create_android_bundle)

    # 拷贝到打包工程下
    cp_bundle = "cp -r %s %s" % ('./output/bundle/', pack_dir + '/' + project_name + '/bussiness_modules/rn/src/main/assets/')
    os.system(cp_bundle)
    cp_res = "cp -r %s %s" % ('./output/res/', pack_dir + '/' + project_name + '/bussiness_modules/rn/src/main/res/')
    os.system(cp_res)

    # 回到打包目录
    command_util.cd_pwd(pack_dir + '/' + project_name)
    return project_full_dir


def chechout_or_update_and_install(svn_path, rn_code_path):
    react_native_code_path = rn_code_path
    # 工程名
    rn_project_name = svn_path[svn_path.rfind('/') + 1:]
    project_full_dir = react_native_code_path + rn_project_name
    # 进入react-native 代码目录
    if os.path.exists(project_full_dir):
        command_util.cd_pwd(project_full_dir)
        # 更新代码
        os.system("svn update")
        print('svn update success! %s' % svn_path)
    else:
        command_util.cd_pwd(react_native_code_path)
        checkout_code(svn_path)
        command_util.cd_pwd(rn_project_name)
    rn_build()

    return project_full_dir


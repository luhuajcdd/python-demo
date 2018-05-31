# -*- coding:utf-8  -*-

# python pack.py  svn_path=svn://200.200.107.201/moa/moa/moa1.1/Branches/android/Android4.3.0-20180509 build=beta pack_dir=/Users/sangfor/Documents/138pack/android-4.3 version=5.0.0 version_code=64 modify_config_ip=YES custom_app_name=NONE
# python pack.py  svn_path=svn://200.200.107.201/moa/moa/moa1.1/Branches/android/Android4.3.0-20180509 build=release pack_dir=/138pack/android-4.3 version=5.0.0 version_code=64 modify_config_ip=YES custom_app_name=NONE
import os
import AndroidPackEntity
import build_src
import command_util
import svn

# 解析参数
from android_pack import AndroidPack

packEntity = AndroidPackEntity.PackEnity()
packEntity.parse_and_init()

# 全局变量
basePath='/Users/sangfor/Documents'
curdir=basePath  + '/autopack'
#verdir='/Users/sangfor/Documents/autopack/version/'
#releasedir='/Users/sangfor/Documents/138pack/autopack/'

command_util.cd_pwd(curdir)

'''
-打包类型:
    -  {定制 or Pocket or kdcloud}
    -  {主干 or 分支}
    -  {release or beta}
'''
def add_dir(parent,child):
    return parent + '/' + child

def get_value(param):
    return param[1]
def get_key(param):
    return param[0]

def get_full_build_type():
    build_full_path = ""

    if get_key(build_src.is_android(packEntity.svn_path)):
        build_full_path=add_dir(build_full_path,get_value(build_src.is_android(packEntity.svn_path)))
    elif get_key(build_src.is_ios(packEntity.svn_path)):
        build_full_path = add_dir(build_full_path,get_value(build_src.is_ios(packEntity.svn_path)))
    else:
        pass

    if get_key(build_src.is_branch(packEntity.svn_path)):
        build_full_path=add_dir(build_full_path,get_value(build_src.is_branch(packEntity.svn_path)))
    elif get_key(build_src.is_trunk(packEntity.svn_path)):
        build_full_path = add_dir(build_full_path,get_value(build_src.is_trunk(packEntity.svn_path)))
    else:
        pass

    build_full_path = add_dir(build_full_path, packEntity.build_type)

    return build_full_path

full_build_type = get_full_build_type()

#打包大版本 = version
full_build_type = add_dir(full_build_type, packEntity.version)

#svn.clear_pack_and_create_new_dir(full_build_type)

# 进入打包目录
print("%s %s" %(os.path.pardir.strip(),full_build_type.strip()))
command_util.cd_pwd(full_build_type)

'''
 checkout code
 打包代码version , 获取代码的svn版本号
'''
code_version = svn.checkout_and_get_code_version(packEntity.svn_path)

'''
    build-info = {release/beta}{version}{code-version} 关于界面显示的内容
    package-name = {Pocket/kdcloud/定制}{release/beta}{version}{code-version}.apk
'''
package_name='pocket-%s-%s-%s.apk' % (packEntity.build_type,packEntity.version,code_version)
print(package_name)

"""
    调用打包脚本
"""
def pack():
    if get_key(build_src.is_android(packEntity.svn_path)):
        androidPack = AndroidPack(basePath + packEntity.pack_file_dir,
                                  package_name,
                                  packEntity.build_type,
                                  packEntity.version,
                                  packEntity.version_code,
                                  packEntity.modify_config_ip,
                                  packEntity.custom_app_name)
        androidPack.pack()


pack()

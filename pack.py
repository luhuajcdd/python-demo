# -*- coding:utf-8  -*-

# python pack.py  svn_path=svn://200.200.107.201/moa/moa/moa1.1/Branches/android/Android4.3.0-20180509 product=pocket build=beta pack_dir=/Users/sangfor/Documents/138pack/android-4.3 version=5.0.0 version_code=64 modify_config_ip=YES custom_app_name=NONE
# python pack.py  svn_path=svn://200.200.107.201/moa/moa/moa1.1/Branches/android/Android4.3.0-20180509 product=pocket build=release pack_dir=/138pack/android-4.3 version=5.0.0 version_code=64 modify_config_ip=YES custom_app_name=NONE
import os
import AndroidPackEntity
import build_src
import command_util
import svn
import react_native

# 解析参数
from android_pack import AndroidPack
from config import ConfigSingleton

packEntity = AndroidPackEntity.PackEnity()
packEntity.parse_and_init()

# 全局变量
config = ConfigSingleton()
basePath = config.base_dir
packEntity.pack_file_dir = basePath + packEntity.pack_file_dir
curdir = basePath + '/autopack'
# verdir='/Users/sangfor/Documents/autopack/version/'
# releasedir='/Users/sangfor/Documents/138pack/autopack/'


command_util.cd_pwd(curdir)

'''
-打包类型:
    -  {定制 or Pocket or kdcloud}
    -  {主干 or 分支}
    -  {release or beta}
'''


def add_dir(parent, child):
    return parent + '/' + child


def get_value(param):
    return param[1]


def get_key(param):
    return param[0]


def get_full_build_type():
    build_full_path = ""

    if get_key(build_src.is_android(packEntity.svn_path)):
        build_full_path = add_dir(build_full_path, get_value(build_src.is_android(packEntity.svn_path)))
    elif get_key(build_src.is_ios(packEntity.svn_path)):
        build_full_path = add_dir(build_full_path, get_value(build_src.is_ios(packEntity.svn_path)))
    else:
        pass

    if get_key(build_src.is_branch(packEntity.svn_path)):
        build_full_path = add_dir(build_full_path, get_value(build_src.is_branch(packEntity.svn_path)))
    elif get_key(build_src.is_trunk(packEntity.svn_path)):
        build_full_path = add_dir(build_full_path, get_value(build_src.is_trunk(packEntity.svn_path)))
    else:
        pass

    build_full_path = add_dir(build_full_path, packEntity.build_type)

    return build_full_path


full_build_type = get_full_build_type()
full_build_type = full_build_type[1:]

# 打包大版本 = version
full_build_type = add_dir(full_build_type, packEntity.version)

svn.clear_pack_and_create_new_dir(full_build_type)

# 工程名
project_name = packEntity.svn_path[packEntity.svn_path.rfind('/') + 1:]

# 进入打包目录
print("%s %s" % (os.path.pardir.strip(), full_build_type.strip()))
command_util.cd_pwd(full_build_type)

'''
 checkout code
 打包代码version , 获取代码的svn版本号
'''
code_version = svn.checkout_and_get_code_version(packEntity.svn_path)

'''
  1. 更新react-native代码
  2. 生成bundle文件
  3. 拷贝到打包工程下
'''
pack_dir = curdir + '/' + full_build_type
project_full_dir = react_native.get_bundle_file(packEntity.rn_svn_path, packEntity.rn_code_path, pack_dir, project_name)

command_util.cd_pwd(project_full_dir)
rn_code_version = svn.get_svn_version(packEntity.rn_svn_path)
command_util.cd_pwd(pack_dir + '/' + project_name)
print('rn: code version = %s ' % rn_code_version)

if int(rn_code_version) > int(code_version):
    code_version = rn_code_version

'''
    build-info = {release/beta}{version}{code-version} 关于界面显示的内容
    package-name = {Pocket/kdcloud/定制}{release/beta}{version}{code-version}.apk
'''
package_name = '%s-%s-%s-%s.apk' % (packEntity.product, packEntity.build_type, packEntity.version, code_version)
print(package_name)

"""
    调用打包脚本
"""


def pack():
    if get_key(build_src.is_android(packEntity.svn_path)):
        androidPack = AndroidPack(packEntity.pack_file_dir,
                                  packEntity.product,
                                  package_name,
                                  packEntity.build_type,
                                  packEntity.version,
                                  packEntity.version_code,
                                  packEntity.modify_config_ip,
                                  packEntity.custom_app_name,
                                  code_version)
        androidPack.pack()


pack()

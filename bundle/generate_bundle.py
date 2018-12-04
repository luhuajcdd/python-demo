# -*- coding:utf-8  -*-
import sys

sys.path.append("..")
import command_util
import subprocess
import os

import file_util
import svn
from bundle.bundle_entity import BundleEntity

#开始执行
bundle_entity = BundleEntity()
bundle_entity.parse_and_init()

base_path = bundle_entity.bundle_base_dir
# 存放bundle文件目录
bundle_dir = base_path + 'bundle/'
# 打包bundle文件目录
react_native_code_path = bundle_entity.rn_code_dir

pocket_version = bundle_entity.pocket_version

output_bundle_dir = react_native_code_path + "output/bundle/"
output_res_dir = react_native_code_path + "output/res/"

'''
    生产android的bundle文件
'''


def generate_android_bundle():
    # 进入react-native 代码目录
    command_util.cd_pwd(react_native_code_path)

    rm_file = 'rm -rf %s*' % bundle_dir
    delete_bundle = subprocess.Popen(rm_file, shell=True,
                                     stdin=subprocess.PIPE,
                                     stdout=subprocess.PIPE,
                                     stderr=subprocess.PIPE)

    # 更新代码
    p = subprocess.Popen("svn update", shell=True)
    # command_util.command_finish(p, "update finished! ")

    code_version = os.popen("svnversion -c |sed 's/^.*://' |sed 's/[A-Z]*$//'", 'r', -1)
    version = code_version.read().strip()

    file_util.mkdir(output_bundle_dir)
    file_util.mkdir(output_res_dir)

    # 生成bundle文件
    command_create_android_bundle = 'react-native bundle --entry-file index.android.js --platform android --dev false --bundle-output ./output/bundle/android-%s-%s.bundle --assets-dest ./output/res/' \
                                    % (pocket_version, version)
    os.system(command_create_android_bundle)

    # 拷贝到打包工程下
    cp_bundle = "mv %s %s" % ('./output/bundle/android-%s-%s.bundle' % (pocket_version, version),
                              bundle_dir + 'android-%s-%s.bundle' % (pocket_version, version))
    os.system(cp_bundle)

    # 回到bundle目录
    command_util.cd_pwd(base_path)


generate_android_bundle()

if svn.isWindows():
    command_str = "upload_and_encrypt.sh"
elif svn.isLinuxOrMac():
    command_str = "./upload_and_encrypt.sh"

os.system(command_str)

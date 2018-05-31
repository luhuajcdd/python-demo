# -*- coding:utf-8  -*-
import os

from config import ConfigSingleton


def backPackage(package_name):
    name_pre = package_name[:package_name.rfind('-')]
    print(name_pre)
    config = ConfigSingleton();
    rm_files="rm -rf %s%s" % (config.back_up_dir+name_pre,'*')
    print(rm_files)
    os.system(rm_files)
    cp_package="cp \\\\200.200.107.38\\pack\\android-4.3\\pocket-release-5.0.0-105569.apk %s" % config.back_up_dir
    os.system(cp_package)



backPackage("pocket-release-5.0.0-105569.apk")

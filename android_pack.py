# -*- coding:utf-8  -*-
import os
import subprocess

import command_util
import file_util
import svn
from config import ConfigSingleton


class AndroidPack(object):

    def __init__(self,pack_file_dir,product,package_name,build_type,version,version_code,modify_config_ip,custom_app_name):
        self.pack_file_dir = pack_file_dir
        self.product = product
        self.package_name = package_name
        self.build_type = build_type
        self.version = version
        self.version_code = version_code
        self.modify_config_ip = modify_config_ip
        self.custom_app_name = custom_app_name


    def pack(self):
        # chmod 0777 ./MOApack.sh
        chmod_pack_shell = 'chmod 0777 ./pack_%s.sh' % (self.product)
        res = os.system(chmod_pack_shell)
        print("chmod res = %s" % res)

        # 打包命令 pack.sh
        command_param = " %s %s %s %s %s %s %s" % (self.pack_file_dir,self.package_name,self.build_type,
                                                          self.version,self.version_code,self.modify_config_ip,
                                                          self.custom_app_name)
        if svn.isWindows():
            command_str="pack_%s.sh %s " % (self.product,command_param)
        elif svn.isLinuxOrMac():
            command_str = "./pack_%s.sh %s " % (self.product,command_param)
        else:
            print("error: 没有对应平台的脚本")
            return

        print(command_str)
        res = os.system(command_str)  # 调用shell脚本
        print(res)
        if res == 0:
            print('打包完毕')
            self.back_package()
        else:
            print("error")

    def back_package(self):
        package_name = self.package_name;
        name_pre = package_name[:package_name.rfind('-')]
        print(name_pre)
        config = ConfigSingleton();
        product_name = package_name[:package_name.find('-')]
        back_up_dir = config.back_up_dir + product_name + "/"
        file_util.mkdir(back_up_dir)
        rm_files = "rm -rf %s%s" % (back_up_dir + name_pre, '*')

        print(rm_files)
        os.system(rm_files)
        cp_package = "cp %s/%s  %s" % (self.pack_file_dir,self.package_name,back_up_dir)
        print(cp_package)
        os.system(cp_package)
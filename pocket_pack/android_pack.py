# -*- coding:utf-8  -*-
import subprocess

import command_util
import svn


class AndroidPack(object):

    def __init__(self,pack_file_dir,package_name,build_type,version,version_code,modify_config_ip,custom_app_name):
        self.pack_file_dir = pack_file_dir
        self.package_name = package_name
        self.build_type = build_type
        self.version = version
        self.version_code = version_code
        self.modify_config_ip = modify_config_ip
        self.custom_app_name = custom_app_name


    def pack(self):
        # chmod 0777 ./MOApack.sh

        # 打包命令 pack.sh
        command_param = " %s %s %s %s %s %s %s" % (self.pack_file_dir,self.package_name,self.build_type,
                                                          self.version,self.version_code,self.modify_config_ip,
                                                          self.custom_app_name)
        if svn.isWindows():
            command_str="sh -x pack.sh %s " % command_param
        elif svn.isLinuxOrMac():
            command_str = "./pack.sh %s " % command_param

        print(command_str)
        p = subprocess.Popen(command_str, shell=True,
                             stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)

        p.wait()
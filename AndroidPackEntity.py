# -*- coding:utf-8  -*-

import argparse

class PackEnity:
    def __init__(self):
        self.svn_path=None
        self.pack_file_dir = None
        self.product = None
        self.build_type = None
        self.version = None
        self.version_code = None
        self.modify_config_ip = None
        self.custom_app_name = None
        self.rn_svn_path = None
        self.rn_code_path = None

    def parse_and_init(self):
        self.init_param(self.parse())

    def parse(self):
        # 解析命令参数
        parser = argparse.ArgumentParser(description='manual to this script')
        parser.add_argument('svn_path', type=str, default = None)
        parser.add_argument('product', type=str, default=None)
        parser.add_argument('build', type=str, default=None)
        parser.add_argument('pack_dir', type=str, default=None)
        parser.add_argument('version', type=str, default=None)
        parser.add_argument('version_code', type=str, default=None)
        parser.add_argument('modify_config_ip', type=str, default=None)
        parser.add_argument('custom_app_name', type=str, default=None)
        parser.add_argument('rn_svn_path', type=str, default=None)
        parser.add_argument('rn_code_path', type=str, default=None)
        args = parser.parse_args()

        print('\n 输入参数：')
        print(' %s \n %s \n  %s \n %s \n %s \n %s \n %s \n %s \n %s \n %s' % (args.svn_path, args.pack_dir,args.product, args.build, args.version, args.version_code, args.modify_config_ip, args.custom_app_name,args.rn_svn_path,args.rn_code_path))
        return args

    def get_value(self,key_value):
        if key_value is None:
            return
        array_map = key_value.split('=')
        if array_map:
            if array_map[1]:
                return array_map[1]
            else:
                print(' %s 没有设置值' % array_map[0])
        else:
            return ""

    def init_param(self, args):
        if args is None:
            print("error args is None")
            return
        self.svn_path=self.get_value(args.svn_path)
        self.pack_file_dir=self.get_value(args.pack_dir)
        self.product = self.get_value(args.product)
        self.build_type=self.get_value(args.build)
        self.version=self.get_value(args.version)
        self.version_code=self.get_value(args.version_code)
        self.modify_config_ip=self.get_value(args.modify_config_ip)
        self.custom_app_name=self.get_value(args.custom_app_name)
        self.rn_svn_path=self.get_value(args.rn_svn_path)
        self.rn_code_path=self.get_value(args.rn_code_path)

        print('value: ')
        print(' %s \n %s \n %s \n %s \n %s \n %s \n %s \n %s \n %s \n %s' % (self.svn_path, self.pack_file_dir,self.product,self.build_type, self.version, self.version_code, self.modify_config_ip, self.custom_app_name,self.rn_svn_path,self.rn_code_path))


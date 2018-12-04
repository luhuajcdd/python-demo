# -*- coding:utf-8  -*-
import argparse


class BundleEntity:
    def __init__(self):
        self.bundle_base_dir = None
        self.rn_code_dir = None
        self.pocket_version = None

    def parse_and_init(self):
        self.init_param(self.parse())

    def parse(self):
        # 解析命令参数
        parser = argparse.ArgumentParser(description='manual to this script')
        parser.add_argument('bundle_base_dir', type=str, default=None)
        parser.add_argument('rn_code_dir', type=str, default=None)
        parser.add_argument('pocket_version', type=str, default=None)
        args = parser.parse_args()

        print('\n 输入参数：')
        print(' %s \n %s \n  %s ' % (args.bundle_base_dir, args.rn_code_dir, args.pocket_version))
        return args

    def get_value(self, key_value):
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
        self.bundle_base_dir = self.get_value(args.bundle_base_dir)
        self.rn_code_dir = self.get_value(args.rn_code_dir)
        self.pocket_version = self.get_value(args.pocket_version)

        print('value: ')
        print(' %s \n %s \n  %s' % (self.bundle_base_dir, self.rn_code_dir, self.pocket_version))

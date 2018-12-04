# -*- coding:utf-8  -*-
import os
import sys

import configparser
import threading
class ConfigSingleton(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        pass

    def parser(self):
        cur_dir = os.path.dirname(__file__)
        file_name = cur_dir + '/pack.cfg'
        if not os.path.exists(file_name):
            print("%s not exist, and exit()" % file_name)
            sys.exit(1)
            return
        # 生成config对象
        conf = configparser.ConfigParser()
        # 用config对象读取配置文件
        conf.read(file_name)
        self.back_up_dir = conf.get("back_up", "back-up-dir")
        self.base_dir = conf.get("pack","base-dir")
        print("config info = ", self.base_dir, self.back_up_dir)

    def __new__(cls, *args, **kwargs):
        if not hasattr(ConfigSingleton, "_instance"):
            with ConfigSingleton._instance_lock:
                if not hasattr(ConfigSingleton, "_instance"):
                    ConfigSingleton._instance = object.__new__(cls)
                    ConfigSingleton._instance.parser()
        return ConfigSingleton._instance


if __name__ == '__main__':
    config = ConfigSingleton();
    print(config.back_up_dir)
    config1 = ConfigSingleton();
    config2 = ConfigSingleton();
    print(config,config1,config2)
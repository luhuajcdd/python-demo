# -*- coding:utf-8  -*-
import os
import subprocess

import command_util
import file_util
import svn
from config import ConfigSingleton


class AndroidPack(object):

    def __init__(self, pack_file_dir, product, package_name, build_type, version, version_code, modify_config_ip, custom_app_name, svn_code_version):
        self.pack_file_dir = pack_file_dir
        self.product = product
        self.package_name = package_name
        self.build_type = build_type
        self.version = version
        self.version_code = version_code
        self.modify_config_ip = modify_config_ip
        self.custom_app_name = custom_app_name
        self.svn_code_version = svn_code_version

    def pack(self):
        # chmod 0777 ./MOApack.sh
        chmod_pack_shell = 'chmod 0777 ./pack_%s.sh' % (self.product)
        res = os.system(chmod_pack_shell)
        print("chmod res = %s" % res)

        # 打包命令 pack.sh
        command_param = " %s %s %s %s %s %s %s %s" % (self.pack_file_dir, self.package_name, self.build_type,
                                                      self.version, self.version_code, self.modify_config_ip,
                                                      self.custom_app_name, self.svn_code_version)
        if svn.isWindows():
            command_str = "pack_%s.sh %s " % (self.product, command_param)
        elif svn.isLinuxOrMac():
            command_str = "./pack_%s.sh %s " % (self.product, command_param)
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
        cp_package = "mv %s/%s  %s/%s" % (self.pack_file_dir, self.package_name, back_up_dir, self.package_name)
        print(cp_package)
        os.system(cp_package)

    def pack_before(self):
        self.reverse_file()
        self.modify_app_name()
        self.beta_configure()
        self.release_configure()

    def beta_configure(self):
        if self.build_type.contain('beta'):
            print("beta configure")
            cur_dir = os.path.curdir
            file_util.replace(cur_dir + "/pocket_pack.sh", 'sdk.dir=\/Users\/sangfor\/Documents', 'sdk.dir=\/Users\/sangfor\/Desktop\/soft\/android')
            file_util.replace(cur_dir + "/common/src/main/java/com/sangfor/pocket/utils/AndroidUtils.java", 'CLIENT_DEV_TYPE = 0', 'CLIENT_DEV_TYPE = 6')
            command_util.command_execute('cp -f common/src/main/res/drawable-hdpi/icon_beta.png	common/src/main/res/drawable-hdpi/app_launcher.png', '')
            command_util.command_execute('cp -f common/src/main/res/drawable-ldpi/icon_beta.png	common/src/main/res/drawable-ldpi/app_launcher.png', '')
            command_util.command_execute('cp -f common/src/main/res/drawable-mdpi/icon_beta.png	common/src/main/res/drawable-mdpi/app_launcher.png', '')
            command_util.command_execute('cp -f common/src/main/res/drawable-xhdpi/icon_beta.png	common/src/main/res/drawable-xhdpi/app_launcher.png', '')
            command_util.command_execute('cp -f common/src/main/res/drawable-xxhdpi/icon_beta.png	common/src/main/res/drawable-xxhdpi/app_launcher.png', '')
            file_util.replace(cur_dir + "common/src/main/java/com/sangfor/pocket/utils/AndroidUtils.java",
                              'APP_VERSION_DETAIL = \"version_detail_flag\"',
                              'APP_VERSION_DETAIL = \"v' + self.version + ' Build-' + self.svn_code_version + ' Beta"')

    def release_configure(self):
        if self.build_type.contain('release'):
            print("release configure")
            cur_dir = os.path.curdir
            file_util.replace(cur_dir + "common/src/main/java/com/sangfor/pocket/utils/AndroidUtils.java",
                              'APP_VERSION_DETAIL = \"version_detail_flag\"',
                              'APP_VERSION_DETAIL = \"v' + self.version + ' Build-' + self.svn_code_version + ' Beta"')
            # 删除vpn的配置
            command_util.command_execute('sed -i ""  "s/compile(name: \'vpn\', ext: \'aar\')//" app/build.gradle', '')
            command_util.command_execute('rm -f app/libs/vpn.aar', '')

    def modify_app_name(self):
        # 修改应用的名字
        if self.custom_app_name:
            print("自定义应用名 %s" % self.custom_app_name)
            print("开始修改应用名")
            command_util.command_execute('grep -rl \'口袋助理\' ./app | xargs sed -i "" \'s/口袋助理/'"$customer_app_name"'/\'', "")
            command_util.command_execute('grep -rl \'口袋助理\' ./baseapp | xargs sed -i "" \'s/口袋助理/'"$customer_app_name"'/\'', "")
            command_util.command_execute('grep -rl \'口袋助理\' ./common | xargs sed -i "" \'s/口袋助理/'"$customer_app_name"'/\'', "")

    def reverse_file(self):
        # 恢复修改的文件
        command_util.command_execute('svn cleanup', "")
        command_util.command_execute('svn revert host_kdzl/src/main/AndroidManifest.xml', "")
        command_util.command_execute('svn revert common/src/main/java/com/sangfor/pocket/utils/AndroidUtils.java', "")
        command_util.command_execute('svn revert app/build.gradle', "")
        command_util.command_execute('svn revert local.properties', "")
        command_util.command_execute('svn revert common/src/main/res/drawable-hdpi/app_launcher.png', "")
        command_util.command_execute('svn revert common/src/main/res/drawable-ldpi/app_launcher.png', "")
        command_util.command_execute('svn revert common/src/main/res/drawable-mdpi/app_launcher.png', "")
        command_util.command_execute('svn revert common/src/main/res/drawable-xhdpi/app_launcher.png', "")
        command_util.command_execute('svn revert common/src/main/res/drawable-xxhdpi/app_launcher.png', "")
        command_util.command_execute('svn update', "")


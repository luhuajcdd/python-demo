# -*- coding:utf-8  -*-

'''
   处理react-native代码
'''
import command_util
import subprocess
import os

react_native_code_path='/Users/sangfor/Documents/autopack/android-ios-common-code/sms_v2'
def get_bundle_file(pack_dir,project_name):
	# 进入react-native 代码目录
	command_util.cd_pwd(react_native_code_path)
	
	# 更新代码
	p = subprocess.Popen("svn update", shell=True)
    #command_util.command_finish(p, "update finished! ")
	
	# 生成bundle文件
	command_create_android_bundle='react-native bundle --entry-file index.android.js --platform android --dev false --bundle-output ./output/bundle/moa.bundle --assets-dest ./output/res/'
	create_android_bundle = subprocess.Popen(command_create_android_bundle, shell=True,
						stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE)
						
	# 拷贝到打包工程下
	cp_bundle="cp -r %s %s" % ('./output/bundle/',pack_dir+'/'+project_name+'/bussiness_modules/rn/src/main/asserts/')
	os.system(cp_bundle)
	cp_res="cp -r %s %s" % ('./output/res/',pack_dir+'/'+project_name+'/bussiness_modules/rn/src/main/res/')
	os.system(cp_res)
	
	#回到打包目录
	command_util.cd_pwd(pack_dir+'/'+project_name)
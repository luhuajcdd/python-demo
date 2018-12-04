# -*- coding:utf-8 -*- 
import os
import command_util
import argparse
import subprocess
import sys

import react_native
from config import ConfigSingleton

#解析传递过来的参数
'''
1.打包类型，正式版、企业版、cal包
2.取代码的目录，即svn地址
3.打包完成后，拷贝的目录(一般指向107.38上的共享目录，即可以通过http来下载)
4.打包的版本号
5.vercode，这个android才有
6.打一些定制包的时候，替换一下名字
'''
svn_path=None
pack_dir = None
product = None
build = None
version = None
custom_name = None
#取本地一些配置、或者后续拼接的参数
'''
1.当前运行目录
2.代码下载目录
3.证书、keystore目录（如果有)
'''
config=ConfigSingleton()
cur_dir=config.base_dir+"autopack/"
src_dir=config.base_dir+"autopack/"


#S 工具函数
def get_value(key_value):
	if key_value is None:
		return ""
	array = key_value.split('=')
	if array:
		if array[1]:
			return array[1]
		else:
			return ""
	else:
		return ""
		
def add_dir(parent,child):
	return parent+"/"+child

def get_platform(srcpath):
	if srcpath.lower().find('android') > -1:
		return 'android'
	elif srcpath.lower().find('ios') > -1:
		return 'ios'
	else:
		return ""
		
def get_buildtype(srcpath):
	if srcpath.lower().find('branches') > -1:
		return 'Branches'
	elif srcpath.lower().find('trunk') > -1:
		return 'Trunk'
	else:
		return ""
#E 工具函数
#S 解析命令行参数		
def get_cmd_args():
	parser = argparse.ArgumentParser(description='manual to this script')
	parser.add_argument('svn_path', type=str, default = None)
	parser.add_argument('product', type=str, default=None)
	parser.add_argument('build', type=str, default=None)
	parser.add_argument('pack_dir', type=str, default=None)
	parser.add_argument('version', type=str, default=None)
	parser.add_argument('custom_name',type=str,default=None)
	parser.add_argument('rn_svn_path',type=str,default=None)
	parser.add_argument('rn_code_path',type=str,default=None)
	args = parser.parse_args()
	#print('\n 输入参数：')
	#print('%s\n%s\n%s\n%s\n%s' % (args.svn_path, args.pack_dir,args.product, args.build, args.version))
	svn_path = get_value(args.svn_path)
	build = get_value(args.build)
	pack_dir = get_value(args.pack_dir)
	product = get_value(args.product)
	version = get_value(args.version)
	custom_name= get_value(args.custom_name)
	rn_svn_path= get_value(args.rn_svn_path)
	rn_code_path= get_value(args.rn_code_path)
	#print('svnpath=%s\npack_dir=%s\nprocut=%s\nbuild=%s\nversion=%s' %(svn_path,pack_dir,product,build,version))
	return svn_path,pack_dir,product,build,version,custom_name,rn_svn_path,rn_code_path
#E 解析命令行参数

def exec_pack(src_dir,product,cur_dir,build,svn_path,pack_dir,version,custom_name,rn_code_path):
	'''chmod_rnconfih_shell = 'chmod 0777 ./RNReactNative/configure.sh'
	res = os.system(chmod_rnconfih_shell)
	print("chmod RN config res = %s" % res)

	rnconfih_shell = 'cd ./RNReactNative/ && ./configure.sh'
	res = os.system(rnconfih_shell)

	print("RN config res = %s" % res)'''
	chmod_pack_shell = 'chmod 0777 ./%s_pack.sh' % (product)
	res = os.system(chmod_pack_shell)
	print("chmod res = %s" % res)
	sys.stdout.flush()
	# 打包命令 pack.sh
	command_param = " %s %s %s %s %s %s %s" % (cur_dir,src_dir,build,pack_dir,version,rn_code_path,custom_name)
	command_str = "./%s_pack.sh %s " % (product,command_param)
	print(command_str)
	res = os.system(command_str)  # 调用shell脚本
	#print(res)
	if res == 0:
		print('Build packet succeed.')
		#self.back_package()
	else:
		print("Build packet fail:errno=%d" % (res))
	return res

def ios_pack():
	print("############## ios pack start ##############")
	global pack_dir
	global src_dir
	global svn_path
	global product
	global build
	global version
	global custom_name
	svn_path,pack_dir,product,build,version,custom_name,rn_svn_path,rn_code_path = get_cmd_args()
	pack_dir = add_dir(config.base_dir,pack_dir)
	print('svnpath=%s\npack_dir=%s\nprocut=%s\nbuild=%s\nversion=%s\ncustom_name=%s' %(svn_path,pack_dir,product,build,version,custom_name))
	src_dir = src_dir+add_dir(get_platform(svn_path),get_buildtype(svn_path)) + "/" + build
	print("src_dir=%s" % (src_dir))
	sys.stdout.flush()
	#检测当前平台&build类型的目录是否存在，没有则创建
	if not os.path.exists(src_dir):
		res  =subprocess.Popen("mkdir -p " + src_dir, shell=True,
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
		command_util.command_finish(res, "create dir " + src_dir)
	src_dir = add_dir(src_dir,version)
	#检测当前版的目录是否存在，如果存在，则先清空
	if os.path.exists(src_dir):
		res  =subprocess.Popen("rm -rf " + src_dir, shell=True,
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
		command_util.command_finish(res, "delete dir " + src_dir)
	
	res  =subprocess.Popen("mkdir -p " + src_dir, shell=True,
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
	command_util.command_finish(res, "create dir " + src_dir)
	#进入打包目录
	command_util.cd_pwd(src_dir)
	#checkout代码到当前目录
	res = subprocess.Popen("svn checkout " + svn_path+" .", shell=True)
	command_util.command_finish(res, "checkout ")

	rn_full_path = react_native.chechout_or_update_and_install(rn_svn_path,rn_code_path);
	command_util.cd_pwd(src_dir)

	return  exec_pack(src_dir,product,cur_dir,build,svn_path,pack_dir,version,custom_name,rn_full_path)

if __name__ == '__main__':
	res = ios_pack()
	sys.exit(res)

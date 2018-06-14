# -*- coding:utf-8  -*-

'''
    云办公 配置类
    1. 分享： 微信 key = wx93dcd36a0bf70586
'''
import sys

SUCCESS = 1
ERROR = -1


# ---------------------------方法区--------------------------------------------
def replace(file, old_str, new_str):
    """
    替换文件中的字符串
    :param file:文件名
    :param old_str:就字符串
    :param new_str:新字符串
    :return:
    """
    file_data = ""
    with open(file, 'r', encoding='UTF-8') as f:
        has_replace_string = False;
        counter = 0
        for line in f:
            if old_str in line:
                has_replace_string = True;
                counter = counter + 1;
                line = line.replace(old_str, new_str)
            file_data += line
        if has_replace_string:
            print("success file=%s, old=%s, new=%s, has = %s, counter=%s " % (
            file, old_str, new_str, has_replace_string, counter))
        else:
            print("failed XXX-----------------XXX file=%s, old=%s, new=%s, has = %s, counter=%s " % (
            file, old_str, new_str, has_replace_string, counter))
            return ERROR
    with open(file, "w", encoding="UTF-8") as f:
        write_result = f.write(file_data)
        print("write write result = %s " % write_result)
    return SUCCESS

def get_line(file,str):
    '''
    获取指定内容的行数
    :param file:
    :param str:
    :return:[]:int
    '''
    lines = []
    line_num = 1
    with open(file, 'r', encoding='UTF-8') as f:
        for line in f:
            if str in line:
                lines.append(line_num)
            line_num = line_num + 1
    return lines

def del_line(file,lines):
    '''
    删除指定的行
    :param file:
    :param lines:行数
    :return:[]: booleans
    '''
    results=[]
    line_num = 1
    file_data = ""
    print("param: del lines = %s" % (lines,))
    with open(file, 'r', encoding='UTF-8') as f:
        for line in f:
            if line_num in lines:
                results.append(True)
                line=' '
            line_num += 1
            file_data += line
    with open(file, "w", encoding="UTF-8") as f:
        write_result = f.write(file_data)
        print("write write result = %s " % write_result)
    return results

def del_content(file,str):
    lines = get_line(file, str)
    if lines:
        for line in lines:
            del_results = del_line(file, (line - 1, line, line + 1, line + 2))
            if del_results:
                print("success : del results = %s " % del_results)
            else:
                print("failed XXX----------------------------XXX: file = %s, str = %s" % (file,str))
                sys.exit(0)
    else:
        print("failed XXX----------------------------XXX: file = %s, str = %s, lines = null" % (file, str))
        sys.exit(0)
    print()

def check_result(result):
    if result == ERROR:
        sys.exit(0)
    print()
# --------------------------------------------------------------------------------------------------
result = 0
# 分享： 微信 key wx93dcd36a0bf70586

result = replace("./thirdlib/src/main/java/com/sangfor/thirdlib/wxapi/WXConfig.java", 
                    "wx8bdda473e43d8cb6",
                    "wx93dcd36a0bf70586")
check_result(result)

#QQ 分享 QQ_KEY
result = replace("./baseapp/src/main/java/com/sangfor/pocket/common/FunctionConfig.java",
                    "1103126222",
                    "1106465152")
check_result(result)
#邀请同事，分享到微信,短信，qq时，把里面的下载链接改为:http://cloud.kdzl.cn/d
result = replace("./baseapp/src/main/java/com/sangfor/pocket/common/FunctionConfig.java",
                    "http://kd77.cn/d",
                    "http://cloud.kdzl.cn/d")
check_result(result)

# 换地图key， -- 更新高德地图key
result = replace("./thirdlib/src/main/AndroidManifest.xml",
                    "edf0ff7ed48f60b052e0a0ac06e5a476",
                    "abbbc0ec44b119a52c5cbac355e410b4")
check_result(result)

#更新腾讯定位key
result = replace("./thirdlib/src/main/AndroidManifest.xml",
                 "CABBZ-ODPWI-HNOG4-5A7W4-RME75-GTFL4",
                 "BEPBZ-LEX3F-CFAJK-NNPHV-XE6QO-FTFFI")
check_result(result)

#各平台推送，百度，华为，魅族 相关配置
#百度推送 key
result = replace("./app/src/main/AndroidManifest.xml",
                    "TCNyOM7inmR7ik0rFxDFYOHS",
                    "rToqPNYzvrABg8c2OckCIL5d")
check_result(result)
#华为推送 key
result = replace("./app/src/main/AndroidManifest.xml",
                    "10192007",
                    "100092425")
check_result(result)
# 魅族推送 key
result = replace("./baseapp/src/main/java/com/sangfor/pocket/moapush/service/MeiZuPushManager.java",
                    "110062",
                    "111307")
check_result(result)
result = replace("./baseapp/src/main/java/com/sangfor/pocket/moapush/service/MeiZuPushManager.java",
                    "d55e99a36038436f91759eac61aa2cf2",
                    "a8bc15f89e1c4a95b2a07ae10e66b649")
check_result(result)

# 修改：applicationId
result = replace("./conf.gradle",
                    "\"com.sangfor.pocket\"",
                    "\"com.sangfor.PocketBackup\"")
check_result(result)
# 更新脚本文件-换包名脚本
result = replace("./common/src/main/java/com/sangfor/pocket/common/BaseFunctionConfig.java",
                    "\"com.sangfor.pocket\"",
                    "\"com.sangfor.PocketBackup\"")
check_result(result)
#修改所有action，provider和permission的 name 前缀为com.sangfor.PocketBackup
result = replace("./app/src/main/AndroidManifest.xml",
                    "com.sangfor.pocket.",
                    "com.sangfor.PocketBackup.")
check_result(result)
result = replace("./app/src/main/AndroidManifest.xml",
                    ".com.sangfor.pocket",
                    ".com.sangfor.PocketBackup")
check_result(result)
# 更新新的打包keystore
result = replace("./app/build.gradle",
                    "sangfor_and.keystore",
                    "pocket_office.jks")
check_result(result)
result = replace("./app/build.gradle",
                    "System.env.AndKeyStorePass",
                    "System.env.AndKeyStorePass_office")
check_result(result)
result = replace("./app/build.gradle",
                    "System.env.AndKeyStoreAlias",
                    "System.env.AndKeyStoreAlias_office")
check_result(result)
result = replace("./app/build.gradle",
                    "System.env.AndKeyPass",
                    "System.env.AndKeyPass_office")
check_result(result)

#修改固定ip 和域名
result = replace("./common/src/main/java/com/sangfor/pocket/constants/BaseCommonConstants.java",
                    "svr#.kd77.cn",
                    "svr.c.kdzl.cn")
check_result(result)
result = replace("./common/src/main/java/com/sangfor/pocket/constants/BaseCommonConstants.java",
                    "118.190.92.194",
                    "118.190.167.142")
check_result(result)
result = replace("./common/src/main/java/com/sangfor/pocket/constants/BaseCommonConstants.java",
                    "public static final String PUBLIC_CLOUD_IP2",
                    "//public static final String PUBLIC_CLOUD_IP2")
check_result(result)
result = replace("./common/src/main/java/com/sangfor/pocket/constants/BaseCommonConstants.java",
                    "public static final String PUBLIC_CLOUD_IP3",
                    "//public static final String PUBLIC_CLOUD_IP3")
check_result(result)
result = replace("./common/src/main/java/com/sangfor/pocket/connect/InitConfigData.java",
                    "FixedIp fixedIp2 =",
                    "/*FixedIp fixedIp2 =")
check_result(result)
result = replace("./common/src/main/java/com/sangfor/pocket/connect/InitConfigData.java",
                    "fixedIpList.add(fixedIp3);",
                    "fixedIpList.add(fixedIp3);*/")
check_result(result)
result = replace("./common/src/main/java/com/sangfor/pocket/connect/InitConfigData.java",
                    "DnsCacheManagement.IpProperty ipProperty2 =",
                    "/*DnsCacheManagement.IpProperty ipProperty2 =")
check_result(result)
result = replace("./common/src/main/java/com/sangfor/pocket/connect/InitConfigData.java",
                    "ipProperties.add(ipProperty3);",
                    "ipProperties.add(ipProperty3);*/")
check_result(result)

#帮助里面去掉两项：1)使用是否有储存空间、人数、时间的限制？ 2):怎么登陆网页版后台?
del_content("./app/src/main/assets/help_and_feedback_more_help.json","怎么登陆网页版后台？")
del_content("./app/src/main/assets/help_and_feedback_home.json","使用是否有储存空间、人数、时间的限制?")



'''
# 
result = replace("./app/src/main/java/com/sangfor/pocket/common/FunctionConfig.java",
                    "",
                    "")
check_result(result)
'''

print(result)


#!/bin/sh

#例子: /Users/sangfor/Documents/autopack/ pocket-4.3.0-10201.apk beta 4.3.0 65 NO NON
#apk的存放目录
package_dir=$1
#apk 名字
package_name=$2
# package 表示  release or beta
package_build_flag=$3
#apk的版本号 例如：5.0.0
versionName=$4
#apk中manifest的code 例如：55 是整数类型，且逐渐增加
versionCode=$5
#登录界面是否可以选择IP   YES:不能选 NO:可以选
cancelConfigureIp=$6
#自定义应用名字  例如 NON:默认名字;
customer_app_name=$7

#--------------------------------------------------------------------------------
#恢复文件
svn cleanup
svn revert app/src/main/AndroidManifest.xml
svn revert common/src/main/java/com/sangfor/pocket/utils/AndroidUtils.java
svn revert app/build.gradle
svn revert local.properties
svn revert common/src/main/res/drawable-hdpi/app_launcher.png
svn revert common/src/main/res/drawable-ldpi/app_launcher.png
svn revert common/src/main/res/drawable-mdpi/app_launcher.png
svn revert common/src/main/res/drawable-xhdpi/app_launcher.png
svn revert common/src/main/res/drawable-xxhdpi/app_launcher.png
svn update

#---------------------------------------------------------------------------------
#修改应用的名字
if [ "$customer_app_name"x != "NONE"x ];then
    echo "########### 自定义应用名为：$customer_app_name#############"
    echo "grep -rl '口袋助理' ./app | xargs sed -i "" 's/口袋助理/$customer_app_name/'"
    grep -rl '口袋助理' ./app | xargs sed -i "" 's/口袋助理/'"$customer_app_name"'/'
	grep -rl '口袋助理' ./baseapp | xargs sed -i "" 's/口袋助理/'"$customer_app_name"'/'
    grep -rl '口袋助理' ./common | xargs sed -i "" 's/口袋助理/'"$customer_app_name"'/'
    echo "########### 修改应用名结束 #############"
else
    #没有配置自定义应用名
    echo "########### 无需修改应用名#############"
fi

#---------------------------------------------------------------------------------
build=`svnversion -c |sed 's/^.*://' |sed 's/[A-Z]*$//'`  


if [ "$package_build_flag"x = "beta"x ];then
	echo "########### Beta package.#############"
	#replace device type
	sed -i "" 's/CLIENT_DEV_TYPE = 0/CLIENT_DEV_TYPE = 6/' common/src/main/java/com/sangfor/pocket/utils/AndroidUtils.java
	#replace icon
	cp -f common/src/main/res/drawable-hdpi/icon_beta.png	common/src/main/res/drawable-hdpi/app_launcher.png
	cp -f common/src/main/res/drawable-ldpi/icon_beta.png	common/src/main/res/drawable-ldpi/app_launcher.png
	cp -f common/src/main/res/drawable-mdpi/icon_beta.png	common/src/main/res/drawable-mdpi/app_launcher.png
	cp -f common/src/main/res/drawable-xhdpi/icon_beta.png	common/src/main/res/drawable-xhdpi/app_launcher.png
	cp -f common/src/main/res/drawable-xxhdpi/icon_beta.png	common/src/main/res/drawable-xxhdpi/app_launcher.png
	sed -i ""  's/APP_VERSION_DETAIL = \"version_detail_flag\"/APP_VERSION_DETAIL = "v'"$versionName"' Build-'"$build"' Beta"/' common/src/main/java/com/sangfor/pocket/utils/AndroidUtils.java
	verlog="./lastestverbeta.log"
else
	echo "########## Publish package.#############"
	sed -i ""  's/APP_VERSION_DETAIL = \"version_detail_flag\"/APP_VERSION_DETAIL = "v'"$versionName"' Build-'"$build"'"/' common/src/main/java/com/sangfor/pocket/utils/AndroidUtils.java
	verlog="./lastestver.log"
	#删除vpn的配置
    sed -i ""  "s/compile(name: 'vpn', ext: 'aar')//" app/build.gradle
    rm -f app/libs/vpn.aar
    echo "成功删除vpn配置"
fi
sed -i ""  's/SVN_NAME = \"[a-zA-Z0-9\.]\{1,\}\"/SVN_NAME = "'"$build"'"/' common/src/main/java/com/sangfor/pocket/utils/AndroidUtils.java

sed -i ""  's/versionName=\"[a-zA-Z0-9\.]\{1,\}\"/versionName="'"$versionName"'"/' app/src/main/AndroidManifest.xml
sed -i ""  's/versionCode=\"[a-zA-Z0-9\.]\{1,\}\"/versionCode="'"$versionCode"'"/' app/src/main/AndroidManifest.xml
sed -i ""  's/android:debuggable=\"true\"//' app/src/main/AndroidManifest.xml

sed -i ""  's/versionName.*/versionName	"'"$versionName"'"/' app/build.gradle
sed -i ""  "s/versionCode.*/versionCode	$versionCode/" app/build.gradle

sed -i ""  's/sdk.dir.*/sdk.dir=\/Users\/sangfor\/Documents\/sdk/' local.properties

sed -i ""  "s/boolean DEBUG = true/boolean DEBUG = false/" common/src/main/java/com/sangfor/pocket/common/BaseFunctionConfig.java


#--------------------------------------------------------------------------------------------------------------------------------------------------
#设置IP配置不启用
if [ "$cancelConfigureIp"x = "YES"x ];then
    sed -i ""  's/IS_SHOW_CUSTOMER_CONFIGURE_IP = \"YES\"/IS_SHOW_CUSTOMER_CONFIGURE_IP = \"NO\"/' common/src/main/java/com/sangfor/pocket/utils/AndroidUtils.java
    echo "IS_SHOW_CUSTOMER_CONFIGURE_IP = NO"
else
    echo "IS_SHOW_CUSTOMER_CONFIGURE_IP = YES"
fi

dos2unix app/src/main/AndroidManifest.xml
dos2unix app/build.gradle
dos2unix local.properties

cp -af /Users/sangfor/Documents/autopack/keystore/sangfor_and.keystore app/sangfor_and.keystore
if [ $? -ne 0 ];then
	echo "copy keystoe fail."
	exit 1
fi
echo "copy keystore success."


cat thirdlib/src/main/AndroidManifest.xml | grep -A1 "edf0ff7ed48f60b052e0a0ac06e5a476" | grep "\-\-"
if [ $? -eq 0 ];then
	echo "error,may be you use debug map key."
	exit 1
fi
gradle clean assemblerelease

if [ $? -eq 0 ];then
	echo "######## android pack done ############"
	echo $svnv > $verlog
        
	cp -f app/build/outputs/apk/app-prod-release.apk "$package_dir/$package_name"

	echo "#Check AndroidManifest:"
	grep -C1 "android:versionCode" app/src/main/AndroidManifest.xml
	echo "#Check gradle.build:"
	grep -C2 "versionCode" app/build.gradle
	echo "#Check AndroidUtil.java:"
	grep -C2 "SVN_NAME =" common/src/main/java/com/sangfor/pocket/utils/AndroidUtils.java
	exit 0
else
	exit 1
fi

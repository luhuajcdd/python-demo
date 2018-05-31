#!/bin/sh

LOGFILE=packlog/pack.ver
dir="$1"
key=`echo $dir | md5`
if [ -f packlog/$key ];then
	rm -f packlog/$key
fi
newver=`svnversion $dir -c |sed 's/^.*://' |sed 's/[A-Z]*$//'`
oldver=`cat $LOGFILE | grep $key | awk -F= '{print $2}'`
echo "oldver=$oldver"
if [ "$oldver"x = ""x ];then
	oldver=$((newver-500))
fi
echo "newver=$newver"
if [ "$newver"x = ""x ];then
	echo "Get version log fail."
	exit 0;
fi
svn log $dir -r $oldver:$newver | while read line;
do
	if [ "$line"x = ""x ];then
		continue;
	fi
	if [ "$line"x = "------------------------------------------------------------------------"x ];then
		continue;
	fi
	if [ "${line:0:1}"x = "r"x ];then
		author=`echo $line | awk -F\| '{print $2}'`
		continue;
	fi
	echo $author:$line >> packlog/$key
done
cat $LOGFILE | grep $key
if [ $? -eq 0 ];then
	sed -i "" "s/$key.*/$key=$newver/" $LOGFILE
else
	echo "$key=$newver" >> $LOGFILE
fi

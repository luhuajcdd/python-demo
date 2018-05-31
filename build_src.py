# -*- coding:utf-8  -*-

def is_android(path):
    android = "android"
    return path.find(android) > -1,android

def is_ios(path):
    ios="ios"
    return path.find(ios) > -1,ios

def is_branch(path):
    branches = "Branches"
    return path.find(branches) > -1,branches

def is_trunk(path):
    trunck = "Trunk"
    return path.find(trunck) > -1,trunck


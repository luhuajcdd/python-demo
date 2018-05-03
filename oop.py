#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'oop programming'

__author__ = 'Tony.Lu'

class Student(object):
	def __init__(self,name,score):
		self.__name = name
		self.score = score

tony = Student('tony',99)


print('tony.score = %s ' % tony.score)
print('tony.name = %s ' % tony._Student__name) #不建议这样获取私有变量



class Student(object):
    count = 10

    def __init__(self, name):
        self.name = name
        Student.count = Student.count + 1

    @property
    def get_score(self):
    	return self.score

    @property.setter
    def set_score(self,score):
    	if not isinstance(score,int):
    		raise ValueError('score must be an integer!')
    	if score < 0 or score > 100:
    		raise ValueError('score must between 0 ~ 100!')
    	self.score = score

print('类 count = %s ' % Student.count)

stu = Student('Tony')
print('实例 count = %s ' % stu.count)

print('类 count = %s ' % Student.count)


#使用__slots__      __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

stu.set_score(90);
print('分数 = %s ' % stu.get_score())

stu.set_score(190);
print('分数 = %s ' % stu.get_score())
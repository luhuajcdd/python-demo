# -*- coding: utf-8 -*-

#--------定义函数--------------------
def add( a,  b):
	c = a + b;
	print('a + b = %d' % c)

add(1,2)


# ---------------返回值------------------
def returnValue(a,b):
	return a + b

print(returnValue(3,4))



import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print(x,y)


def returnMultiValue():
	return 3, 4

a, b = returnMultiValue()
print(returnMultiValue)
print("x = %s,b = %s" % (a, b))


#---------------空函数
def nullMethod():
	pass
nullMethod()

#---------------传入List
def argsList(l=[]):
	l.append('add one');	
	return l
print(argsList())



#-----------------可变参数
def variableParam(numbers):

	sum = 0
	for n in numbers:
		sum += n;

	print('sum = %s' % sum)

variableParam((1,2,3,4,5))

def variableParam2(*numbers):

	sum = 0
	for n in numbers:
		sum += n;

	print('sum = %s' % sum)

lnumbers = [1,2,3,4,5,6]
variableParam2(*lnumbers)
variableParam2(*(1,2))


#---------------关键字参数
def person(name, age, **kv):
	print("name = ",name,"age = ",age,"kv = ",kv)

person('Michael', 30)
person('tony',31,city='shenzhen')

#---------------命名关键字参数


#---------------参数组合
def contain(a,b,c,*t,**d):
	print(a,b,c,t,d)

contain(1,2,3,[1,2],key='value')
contain(1,2,'3',[1,2],key='value')
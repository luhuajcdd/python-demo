# -*- coding:utf-8  -*-

#--------------高阶函数---------------
#   高阶函数   map
def square(x):
	return x * x

r = map(square,[1,2,3,4,5])

print(r)

#   高阶函数   reduce
def add(x, y):
	return x + y

print(reduce(add,(1,2,3,4)))

def fn(x, y):
    return x * 10 + y

def char2num(s):
	digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
	return digits[s]

print(map(char2num,'1234'))
print(reduce(fn, map(char2num,'12')))
print(int('12'))

#   高阶函数   filter
def is_odd(n):
	return n%2 == 1

print(list(range(50)))
print(filter(is_odd,list(range(50)))) 
list1 = [1,2,3]
print(filter(is_odd,list1)) 
print(filter(is_odd,[1,2,3]))


#   高阶函数   sorted
print(sorted([36, 5, -12, 9, -21]))
print(sorted([36, 5, -12, 9, -21],key=abs))
print(sorted([36, 5, -12, 9, -21],key=abs,reverse=True))



#-----------------返回函数
def lazy_sum(*args):
	def sun():
		ax = 0
		for x in args:
			ax = ax + x
		return ax
	return sun
lf2 = lazy_sum(1,2,3)
print(lf2())

lf = lazy_sum(*list(range(10)))
print(lf())

# 闭包
def count():
	def f(j):
		return lambda : j * j
	fs = []
	for x in range(1,4):
		fs.append(f(x))

	return fs;

f1, f2, f3 = count()
print('f1 = %s , f2 = %s, f3 = %s ' % (f1(),f2(),f3()))

#----匿名函数
print(map(lambda x : x * x ,range(5)))


#------------------装饰器

import time
import functools
def log(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			start = time.time()
			print()
			fun = func(*args,**kw)
			end = time.time()
			print('%s : %s() ,time = %s' % (text, func.__name__, end - start))
			return fun
		return wrapper
	return decorator

from advancedfeature import fib
@log('test decorator excute')
def now():
	fib(10)
	return time.time()

f = now
print(f.__name__)
print(f())

#--------------------------------偏函数
def int2(x, base=2):
	return int(x,base)

print(int2('101010101'))

int2To10 = functools.partial(int,base = 2)
if __name__=='__main__':
	print(int2To10('101010111'))


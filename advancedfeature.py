# -*- coding: utf-8 -*-

#-----------切片
list1 = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

subL = list1[0:2]

print(subL)


int100 = list(range(100))

print(int100)

print(int100[:10])
print(int100[-10:])
print(int100[10:20])
print(int100[::3])

tupleTest = (range(10))
print(tupleTest)
print(tupleTest[:3])

print('abcdefg'[2:5])
print('abcdefg'[2:10])
print(len('abcdefg'[2:10]))


#----------------迭代
listIterator = list(range(10))
for x in listIterator:
	print('x = %s'  % x);
print()

for index,value in enumerate(listIterator):
	print('index = %s, value = %s' % (index, value))


print()
disIterator = {'a':1,'b':2}
for x in disIterator:
	print('x = %s'  % x);

for k,v in disIterator.items():
	print('k = %s, v = %s'  % (k,v));


from collections import Iterable
print(isinstance('abc',Iterable))
print(isinstance({'a':1},Iterable))
print(isinstance((1,2,3),Iterable))
print(isinstance(123,Iterable))


#--------------------列表生成
genrateList1 = list(range(2,10))
print(genrateList1)

genrateList2 = [x*x for x in range(10)]
print(genrateList2)

genrateList3 = [x*x for x in range(10) if x % 2 == 0 ]
print(genrateList3)

genrateList4 = [ m + n  for m in 'abc' for n in ('1','2','3')]
print(genrateList4)

import os
allfile = [d for d in os.listdir('.')]
print(allfile)

listStr1 = ['Hello', 'World', 'IBM', 'Apple']
listCharTolower = [s.lower() for s in listStr1]
print(listCharTolower)



#------------------生成器
generator1 = (x*x for x in range(3))
print(generator1)
for g in generator1:
	print('g = %s' % g)

import time;
start = time.time()
def fib(max):
	n,a,b = 0,0,1
	while n < max:
		print(b)
		a, b = b, a + b
		n = n + 1
	return 'done'

if __name__=='__main__':
	fib(10)
end = time.time();
print('time = %s' % (end - start))


start2 = time.time()
def fib2(max):
	n,a,b = 0,0,1
	while n < max:
		yield(b)
		a, b = b, a + b
		n = n + 1

if __name__=='__main__':
	for x in fib2(10):
		print(x)
end2 = time.time();
print('time = %s' % (end2 - start2))
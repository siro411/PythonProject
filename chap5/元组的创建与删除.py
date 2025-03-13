t=('hello',[10,20,30],'world')
print(t)
t=tuple('helloworld')
print(t)

t=tuple([10,20,30,40])
print(t)
print('10在元组中是否存在：',(10 in t))
print('10在元组中是不存在：',(10 not in t))
print('最大值：',max(t))
print('最小值：',min(t))
print('t.index(10):',t.index(10))
print('t.count:',t.count(10))

t=(10)
print(t,type(t))

#元组中只有一个元素，逗号不能省
y=(10,)
print(y,type(y))

del t
#print(t)
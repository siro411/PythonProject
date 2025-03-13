s='helloworld'
print('e在helloworld中存在吗',('e' in s))
print('v在helloworld中存在吗',('v' in s))

print('e在helloworld中不存在吗',('e' not in s))
print('v在helloworld中不存在吗',('v' not in s))

#内置函数
print('len():',len(s))
print('max():',max(s))
print('min():',min(s))

#序列对象的方法，使用序列的名称，打点调用
print('s.index():',s.index('o'))
#print('s.index():',s.index('v')) ValueError：substring not found 报错原因是v在字符串中根本不存在，不存在所以找不到
print('s.count():',s.count('o'))
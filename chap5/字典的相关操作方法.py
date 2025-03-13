d={1001:'小乖',1002:'小坏',1003:'胖乖'}
d[1004]='老坏'
print(d)

keys=d.keys()
print(keys)
print(list(keys))
print(tuple(keys))

values=d.values()
print(values)
print(list(values))
print(tuple(values))

# 如何将字典中的数据转换成key-value的形式,以元组的方式进行展现
lst=list(d.items())
print(lst)

d=dict(lst)
print(d)

print(d.pop(1001))
print(d)

print(d.pop(1008,'不存在'))
print(d.popitem())
print(d)

d.clear()
print(d)

print(bool(d)) #空字典的bool值是False
